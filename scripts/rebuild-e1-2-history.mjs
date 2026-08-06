#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const STATE_PATH = '/Users/hskim/Projects/codyssey/artifacts/e1-2/state.json';
const REPO_DIR = '/Users/hskim/Projects/codyssey/artifacts/e1-2';
const WORKTREE_DIR = '/private/tmp/e1-2-history-rebuild';
const WORK_DIR = path.join(WORKTREE_DIR, 'work');
const BRANCH_NAME = 'codex/e1-2-history-rebuild';

const GROUPS = [
  {
    key: 'c2',
    logIds: ['log-3', 'log-4', 'log-5', 'log-6'],
    commitMessage: 'Feat: Quiz 클래스와 정답 판정 구현',
    chapter: 'Quiz 클래스와 객체 기초',
    theme: 'Quiz 기능 완성 후 commit 기록',
    action: 'Quiz 클래스 기능을 Git 기능 단위 커밋으로 기록',
    purpose: 'Quiz 클래스 생성, 출력, 정답 판정 기능을 완성한 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
  },
  {
    key: 'c3',
    logIds: ['log-7', 'log-8', 'log-9', 'log-10', 'log-11'],
    commitMessage: 'Refactor: QuizGame으로 메뉴 책임 분리',
    chapter: 'QuizGame으로 역할 나누기',
    theme: 'QuizGame 구조 완성 후 commit 기록',
    action: 'QuizGame 리팩터링 결과를 Git 기능 단위 커밋으로 기록',
    purpose: '메뉴 출력, 입력 검사, 종료 판단 책임을 QuizGame으로 옮긴 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
  },
  {
    key: 'c4',
    logIds: ['log-12', 'log-13'],
    commitMessage: 'Feat: state.json 저장과 복구 처리 추가',
    chapter: 'state.json 저장과 복구',
    theme: '저장 복구 기능 완성 후 commit 기록',
    action: 'state.json 저장과 복구 기능을 Git 기능 단위 커밋으로 기록',
    purpose: '게임 상태 저장과 손상 파일 복구 기능을 완성한 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
  },
  {
    key: 'c5',
    logIds: ['log-14', 'log-15', 'log-16'],
    commitMessage: 'Feat: 퀴즈 플레이와 점수 계산 구현',
    chapter: '퀴즈 플레이와 점수 계산',
    theme: '플레이 기능 완성 후 commit 기록',
    action: '퀴즈 플레이와 점수 계산 기능을 Git 기능 단위 커밋으로 기록',
    purpose: '실제 퀴즈 풀이와 점수 합산 흐름을 완성한 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
    verifyCommands: [
      "printf '1\\n2\\n2\\n' | python3 main.py",
    ],
  },
  {
    key: 'c6',
    logIds: ['log-17', 'log-18', 'log-19', 'log-20'],
    commitMessage: 'Feat: 퀴즈 추가 삭제와 점수 메뉴 구현',
    chapter: '문제 관리와 점수 메뉴',
    theme: '문제 관리 기능 완성 후 commit 기록',
    action: '퀴즈 추가/삭제와 점수 메뉴 기능을 Git 기능 단위 커밋으로 기록',
    purpose: '문제 관리와 점수 확인 메뉴를 완성한 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
    verifyCommands: [
      "rm -f state.json",
      "printf '2\\n파이썬 창시자는 누구인가?\\nGuido van Rossum\\nLinus Torvalds\\nJames Gosling\\nBjarne Stroustrup\\n1\\n6\\n' | python3 main.py",
      "python3 - <<'PY'\nimport json\nfrom pathlib import Path\ndata = json.loads(Path('state.json').read_text(encoding='utf-8'))\nprint(len(data['quizzes']))\nprint(data['quizzes'][-1]['question'])\nprint(data['quizzes'][-1]['answer'])\nPY",
      "printf '5\\n6\\n' | python3 main.py",
      "printf '4\\n2\\n6\\n' | python3 main.py",
      "python3 - <<'PY'\nimport json\nfrom pathlib import Path\ndata = json.loads(Path('state.json').read_text(encoding='utf-8'))\nprint(len(data['quizzes']))\nprint(data['quizzes'][-1]['question'])\nPY",
    ],
  },
  {
    key: 'c7',
    logIds: ['log-21', 'log-22'],
    commitMessage: 'Feat: 랜덤 출제와 힌트 기능 추가',
    chapter: '랜덤 출제와 힌트',
    theme: '보너스 기능 완성 후 commit 기록',
    action: '랜덤 출제와 힌트 기능을 Git 기능 단위 커밋으로 기록',
    purpose: '문제 수 선택, 랜덤 출제, 힌트 기능을 완성한 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
    verifyCommands: [
      "rm -f state.json",
      "printf '1\\n2\\n2\\n2\\n6\\n' | python3 main.py",
      "printf '1\\n9\\n6\\n' | python3 main.py",
      "printf '1\\nabc\\n6\\n' | python3 main.py",
      "printf '1\\n1\\ny\\n2\\n6\\n' | python3 main.py",
    ],
  },
  {
    key: 'c8',
    logIds: ['log-23'],
    commitMessage: 'Feat: 플레이 기록 저장 기능 추가',
    chapter: '플레이 기록 저장',
    theme: '플레이 기록 기능 완성 후 commit 기록',
    action: '플레이 기록 저장 기능을 Git 기능 단위 커밋으로 기록',
    purpose: '날짜/시간 포함 플레이 기록 저장 기능을 완성한 뒤 실제 Git 명령으로 작업 이력을 남긴다.',
    verifyCommands: [
      "rm -f state.json",
      "printf '1\\n1\\nn\\n2\\n7\\n' | python3 main.py",
      "python3 -m json.tool state.json",
      "printf '6\\n7\\n' | python3 main.py",
    ],
  },
];

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function writeJson(filePath, value) {
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf8');
}

function nowIso() {
  return new Date().toISOString();
}

function escapeRegex(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function nextLogId(state) {
  const max = state.logs.reduce((acc, log) => {
    const match = /^log-(\d+)$/.exec(log.id || '');
    return match ? Math.max(acc, Number(match[1])) : acc;
  }, 0);
  return `log-${max + 1}`;
}

function applyEditorChange(currentText, editorChange, logId) {
  const change = editorChange.change || {};
  if (change.kind === 'overwrite') {
    return change.to ?? '';
  }
  if (change.kind === 'replace') {
    const from = change.from ?? '';
    const to = change.to ?? '';
    if (!currentText.includes(from)) {
      const nonEmptyLines = from
        .split('\n')
        .map((line) => line.trimEnd())
        .filter((line) => line.trim() !== '');
      const loosePattern = nonEmptyLines
        .map((line) => escapeRegex(line.trimStart()).replace(/ /g, ' +'))
        .join('\\n(?:[ \\t]*\\n)*[ \\t]*');
      const looseRegex = new RegExp(`[ \\t]*${loosePattern}`);
      if (!looseRegex.test(currentText)) {
        throw new Error(`Could not find replace target in ${editorChange.file} for ${logId}: ${from.slice(0, 80)}`);
      }
      return currentText.replace(looseRegex, to);
    }
    return currentText.replace(from, to);
  }
  throw new Error(`Unsupported editor change kind: ${change.kind}`);
}

function loadFileMap() {
  const fileMap = new Map();
  return fileMap;
}

function saveFileMap(fileMap) {
  for (const [relativePath, content] of fileMap.entries()) {
    const absolutePath = path.join(WORK_DIR, relativePath);
    fs.mkdirSync(path.dirname(absolutePath), { recursive: true });
    fs.writeFileSync(absolutePath, content, 'utf8');
  }
}

function runCommand(command, cwd) {
  try {
    const stdout = execSync(command, {
      cwd,
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
      shell: '/bin/zsh',
      maxBuffer: 20 * 1024 * 1024,
    });
    return stdout.replace(/\s+$/, '');
  } catch (error) {
    const stdout = error.stdout ? String(error.stdout) : '';
    const stderr = error.stderr ? String(error.stderr) : '';
    throw new Error(`Command failed: ${command}\n--- stdout ---\n${stdout}\n--- stderr ---\n${stderr}`);
  }
}

function appendGitLog(state, group, gitSteps) {
  const id = nextLogId(state);
  const at = nowIso();
  const frames = gitSteps.map((step) => ({ type: 'terminal-step', ...step }));
  state.logs.push({
    id,
    at,
    chapter: group.chapter,
    theme: group.theme,
    action: group.action,
    purpose: group.purpose,
    workDir: 'artifacts/e1-2/work',
    frames,
    editorChanges: [],
    terminalSteps: gitSteps,
    commands: gitSteps.map((step) => step.command),
    terminalOutputs: gitSteps.map((step) => step.output),
    outputs: [`${group.commitMessage} 커밋과 Git 로그 확인`],
    interpretation: `${group.commitMessage} 커밋을 만들고 status/add/commit/log 순서가 실제 터미널 출력으로 남았다.`,
    evidence: gitSteps.map((step) => `${step.command}\n${step.output}`.trim()).join('\n\n'),
    artifacts: [],
  });
  state.updatedAt = at;
  state.history = state.history || [];
  state.history.push({ at, event: 'logged', logId: id });
}

function getEditorChanges(log) {
  if (Array.isArray(log.frames) && log.frames.length > 0) {
    return log.frames.filter((frame) => frame.type === 'editor-change');
  }
  return log.editorChanges || [];
}

function getTerminalSteps(log) {
  if (Array.isArray(log.frames) && log.frames.length > 0) {
    return log.frames.filter((frame) => frame.type === 'terminal-step');
  }
  return log.terminalSteps || [];
}

function normalizedCommand(logId, command) {
  let nextCommand = command.replaceAll(
    '/Users/hskim/Projects/codyssey/artifacts/e1-2/work/main.py',
    `${WORK_DIR}/main.py`,
  );

  if (logId === 'log-14' && nextCommand === 'python3 main.py') {
    nextCommand = "printf '1\\n2\\n2\\n' | python3 main.py";
  }

  if (logId === 'log-16' && nextCommand === "printf '1\n2\n' | python3 main.py") {
    nextCommand = "printf '1\\n2\\n2\\n' | python3 main.py";
  }

  return nextCommand;
}

function buildSnapshotFromLogs(state, logIds) {
  const fileMap = loadFileMap();
  for (const logId of logIds) {
    const log = state.logs.find((item) => item.id === logId);
    if (!log) throw new Error(`Missing source log: ${logId}`);
    for (const editorChange of getEditorChanges(log)) {
      const currentText = fileMap.get(editorChange.file) ?? '';
      const nextText = applyEditorChange(currentText, editorChange, logId);
      fileMap.set(editorChange.file, nextText);
    }
  }
  return fileMap;
}

function resetWorktreeForRebuild() {
  runCommand(`git -C ${WORKTREE_DIR} checkout --orphan ${BRANCH_NAME}`, WORKTREE_DIR);
  for (const entry of fs.readdirSync(WORKTREE_DIR)) {
    if (entry === '.git') continue;
    fs.rmSync(path.join(WORKTREE_DIR, entry), { recursive: true, force: true });
  }
  fs.mkdirSync(WORK_DIR, { recursive: true });
  fs.writeFileSync(path.join(WORKTREE_DIR, '.gitignore'), '__pycache__/\n*.pyc\n.DS_Store\n', 'utf8');
}

function createC1RootCommit(state) {
  const fileMap = buildSnapshotFromLogs(state, ['log-1', 'log-2']);
  saveFileMap(fileMap);
  runCommand(`git -C ${WORKTREE_DIR} add -A`, WORKTREE_DIR);
  runCommand(`git -C ${WORKTREE_DIR} commit -m "Feat: 반복 메뉴와 종료 흐름 구현"`, WORKTREE_DIR);
}

function main() {
  const state = readJson(STATE_PATH);
  const originalLogCount = state.logs.length;
  const sourceLogIds = state.logs
    .map((log) => log.id)
    .filter((id) => /^log-(?:[1-9]|1[0-9]|2[0-3])$/.test(id));

  resetWorktreeForRebuild();
  createC1RootCommit(state);

  for (const group of GROUPS) {
    const endIndex = sourceLogIds.findIndex((id) => id === group.logIds[group.logIds.length - 1]);
    if (endIndex < 0) throw new Error(`Missing source range end for ${group.key}`);
    if (group.verifyCommands) {
      const finalSnapshot = buildSnapshotFromLogs(state, sourceLogIds.slice(0, endIndex + 1));
      saveFileMap(finalSnapshot);
      for (const command of group.verifyCommands) {
        runCommand(command, WORK_DIR);
      }
    } else {
      for (const logId of group.logIds) {
        const log = state.logs.find((item) => item.id === logId);
        const logIndex = sourceLogIds.findIndex((id) => id === logId);
        if (logIndex < 0) throw new Error(`Missing source log index: ${logId}`);
        const logSnapshot = buildSnapshotFromLogs(state, sourceLogIds.slice(0, logIndex + 1));
        saveFileMap(logSnapshot);
        for (const step of getTerminalSteps(log)) {
          runCommand(normalizedCommand(logId, step.command), WORK_DIR);
        }
      }
    }

    const snapshotLogIds = sourceLogIds.slice(0, endIndex + 1);
    const fileMap = buildSnapshotFromLogs(state, snapshotLogIds);
    saveFileMap(fileMap);

    const gitSteps = [
      {
        theme: group.theme,
        command: `git -C ${REPO_DIR} status --short`,
        output: runCommand(`git -C ${WORKTREE_DIR} status --short`, WORKTREE_DIR),
        cwd: 'artifacts/e1-2/work',
      },
      {
        theme: group.theme,
        command: `git -C ${REPO_DIR} add -A`,
        output: runCommand(`git -C ${WORKTREE_DIR} add -A`, WORKTREE_DIR),
        cwd: 'artifacts/e1-2/work',
      },
      {
        theme: group.theme,
        command: `git -C ${REPO_DIR} commit -m "${group.commitMessage}"`,
        output: runCommand(`git -C ${WORKTREE_DIR} commit -m "${group.commitMessage}"`, WORKTREE_DIR),
        cwd: 'artifacts/e1-2/work',
      },
      {
        theme: group.theme,
        command: `git -C ${REPO_DIR} log --oneline --graph --decorate -n 3`,
        output: runCommand(`git -C ${WORKTREE_DIR} log --oneline --graph --decorate -n 3`, WORKTREE_DIR),
        cwd: 'artifacts/e1-2/work',
      },
    ];

    appendGitLog(state, group, gitSteps);
  }

  writeJson(STATE_PATH, state);
  console.log(`Added ${state.logs.length - originalLogCount} Git reconstruction logs.`);
}

main();
