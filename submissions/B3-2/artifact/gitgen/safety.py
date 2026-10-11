"""전송 직전 마스킹·파일 제외·전송량 제한."""
from dataclasses import dataclass
from pathlib import PurePosixPath
import re

PATTERNS = (
    (r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\s\S]*?(?:-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\Z)', '[REDACTED PRIVATE KEY]'),
    (r'\b(?:sk-[A-Za-z0-9_-]{8,}|gh[pousr]_[A-Za-z0-9_]{8,}|github_pat_[A-Za-z0-9_]{8,}|AKIA[A-Z0-9]{16})\b', '[REDACTED TOKEN]'),
    (r'(?im)((?:[\w-]*(?:api[_-]?key|token|secret|password)[\w-]*)["\x27]?\s*[:=]\s*)[^\r\n]+', r'\1[REDACTED SECRET]'),
    (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '[REDACTED EMAIL]'),
    (r'\b01[016789][- ]?\d{3,4}[- ]?\d{4}\b', '[REDACTED PHONE]'),
    (r'(?i)(Bearer\s+)[A-Za-z0-9._~+/-]+=*', r'\1[REDACTED TOKEN]'),
)


def mask(text: str, secrets: tuple[str, ...] = ()) -> str:
    for secret in secrets:
        if secret:
            text = text.replace(secret, '[REDACTED KEY]')
    for pattern, replacement in PATTERNS:
        text = re.sub(pattern, replacement, text)
    return text


def sensitive_file(path: str) -> bool:
    name = PurePosixPath(path).name.lower()
    return name == '.env' or name.startswith('.env.') or name.endswith(('.pem', '.key', '.p12', '.pfx')) or name in {'credentials', 'id_rsa', 'id_ed25519'}


@dataclass(frozen=True)
class SafeInput:
    diff: str
    omitted_files: int
    truncated: bool


def prepare_diff(diff: str, *, enabled: bool, max_files: int, max_lines: int,
                 secrets: tuple[str, ...] = ()) -> SafeInput:
    if not enabled:
        # 실행 중인 API Key 자체는 OFF에서도 절대 전달하지 않는다.
        for secret in secrets:
            if secret:
                diff = diff.replace(secret, '[REDACTED KEY]')
        return SafeInput(diff, 0, False)
    chunks = re.split(r'(?m)(?=^diff --git )', diff)
    kept, omitted = [], 0
    count = 0
    for chunk in chunks:
        if not chunk.strip():
            continue
        # +++/--- 헤더에서 경로 확인. 공백·따옴표를 포함하는 경로도 처리.
        paths = re.findall(r'(?m)^(?:\+\+\+|---) (?:[ab]/)?(.+)$', chunk)
        header = chunk.splitlines()[0]
        unsafe_header = bool(re.search(r'(?:/|\s)(?:\.env(?:\.[^\s"]*)?|[^\s"]+\.(?:pem|key|p12|pfx))(?:"|\s|$)', header, re.I))
        if unsafe_header or any(sensitive_file(p.strip('"').split('\t')[0]) for p in paths) or 'GIT binary patch' in chunk or 'Binary files ' in chunk:
            omitted += 1
            continue
        if count >= max_files:
            omitted += 1
            continue
        count += 1
        kept.append(chunk)
    # 줄 제한 전에 마스킹해 비밀키 블록이 중간에서 잘리지 않도록 한다.
    redacted = mask(''.join(kept), secrets)
    lines = redacted.splitlines()
    return SafeInput('\n'.join(lines[:max_lines]), omitted, len(lines) > max_lines or omitted > 0)
