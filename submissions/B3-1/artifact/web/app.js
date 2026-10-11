const button = document.querySelector('#check');
const status = document.querySelector('#status');
button.addEventListener('click', async () => {
  button.disabled = true;
  status.textContent = '확인 중…';
  try {
    const response = await fetch('/health', { signal: AbortSignal.timeout(5000), cache: 'no-store' });
    const body = await response.text();
    if (!response.ok || body.trim() !== 'OK') throw new Error('Unexpected health response');
    status.textContent = `정상 · HTTP ${response.status} · ${body.trim()}`;
  } catch {
    status.textContent = '상태 확인 실패 · 잠시 후 다시 확인해 주세요.';
  } finally {
    button.disabled = false;
  }
});
