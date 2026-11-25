(() => {
  const styles = document.createElement('style');
  styles.textContent = `
    .terminal-demo-launch{position:fixed;left:24px;bottom:24px;z-index:30;border:1px solid #7bbada;border-radius:999px;padding:11px 18px;background:#0e2948;color:#e9f5ff;font:600 14px/1.2 system-ui;cursor:pointer;box-shadow:0 6px 24px #0005}
    .terminal-demo-launch:hover{background:#173b61}
    .slide[data-evaluation="EVQ-001"] .body,.slide[data-evaluation="EVQ-002"] .body,.slide[data-evaluation="EVQ-003"] .body,.slide[data-evaluation="EVQ-004"] .body,.slide[data-evaluation="EVQ-005"] .body,.slide[data-evaluation="EVQ-006"] .body,.slide[data-evaluation="EVQ-007"] .body{display:flex;flex-direction:column;align-items:stretch;justify-content:flex-start;gap:0;padding:0;min-height:0;overflow:hidden;overscroll-behavior:contain}
    .slide[data-evaluation="EVQ-001"] .points,.slide[data-evaluation="EVQ-002"] .points,.slide[data-evaluation="EVQ-003"] .points,.slide[data-evaluation="EVQ-004"] .points,.slide[data-evaluation="EVQ-005"] .points,.slide[data-evaluation="EVQ-006"] .points,.slide[data-evaluation="EVQ-007"] .points{width:min(100%,1060px);flex:none}
    .terminal-inline-commands{width:100%;max-width:none;min-height:0;flex:1;margin:0;padding:14px 18px;border:1px solid #416386;border-radius:12px;background:#0b1d37;box-sizing:border-box;overflow-y:auto;overscroll-behavior:contain}
    .terminal-inline-commands>h3{margin:0 0 10px;color:#cce8ff;font:700 17px/1.4 system-ui}
    .terminal-inline-commands .terminal-demo-item{margin:8px 0;padding:10px 12px;border-radius:8px}
    .terminal-inline-commands .terminal-demo-item h3{margin-bottom:6px;font-size:14px}
    .terminal-inline-commands .terminal-demo-item pre{padding:9px 11px;font-size:12px;line-height:1.45;white-space:pre-wrap;overflow-wrap:anywhere}
    .terminal-inline-commands .terminal-demo-actions{margin-top:6px}
    .terminal-inline-commands .terminal-demo-status{font-size:12px}
    .terminal-demo-launch-primary{position:static;left:auto;bottom:auto;z-index:auto;display:flex;align-items:center;justify-content:center;align-self:center;width:min(440px,90%);min-height:92px;margin:auto 0;padding:22px 36px;border:2px solid #9cddff;border-radius:18px;background:linear-gradient(135deg,#176d78,#176093);color:#fff;font:800 28px/1.2 system-ui;box-shadow:0 14px 38px #001a3d88;transform:translateY(0);transition:transform .16s ease,box-shadow .16s ease}
    .terminal-demo-launch-primary:hover{background:linear-gradient(135deg,#20848e,#2076b1);box-shadow:0 18px 44px #001a3daa;transform:translateY(-2px)}
    #terminal-demo-dialog{width:min(900px,calc(100vw - 32px));max-width:none;max-height:86vh;padding:0;border:1px solid #416386;border-radius:16px;background:#091a31;color:#e8f1fb;box-shadow:0 20px 80px #0009}
    #terminal-demo-dialog.terminal-log-mode{width:min(1320px,96vw);height:min(860px,92vh);max-height:none;border-radius:8px;background:#0a1c3e;color:var(--ink,#f7fbff)}
    #terminal-demo-dialog::backdrop{background:#020914c9;backdrop-filter:blur(3px)}
    .terminal-demo-head{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 22px;background:#0d2340;border-bottom:1px solid #35516e}
    .terminal-demo-head h2{margin:0;font:700 20px/1.3 system-ui}.terminal-demo-close{border:1px solid #526f8d;border-radius:8px;padding:8px 12px;background:#172f4d;color:inherit;font:600 14px system-ui;cursor:pointer}
    .terminal-demo-content{padding:18px 22px 24px;overflow:auto;max-height:calc(86vh - 68px)}
    .terminal-demo-item{margin:14px 0;padding:14px;border:1px solid #294665;border-radius:12px;background:#0c2039}
    .terminal-demo-item h3{margin:0 0 10px;font:600 15px/1.4 system-ui;color:#cce8ff}
    .terminal-demo-item pre{margin:0;overflow:auto;padding:13px;border-radius:8px;background:#050e1b;color:#e7f0fc;font:13px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre}
    .terminal-demo-actions{display:flex;align-items:center;gap:12px;margin-top:10px}
    .terminal-log-note{flex:none;margin:0 0 10px;color:#a9c5dd;font:13px/1.5 system-ui}
    #terminal-demo-dialog.terminal-log-mode .terminal-demo-head{padding:14px 22px;border-bottom:1px solid var(--rule,rgba(156,221,255,.38));background:#0a1c3e}
    #terminal-demo-dialog.terminal-log-mode .terminal-demo-head h2{font-size:18px}
    #terminal-demo-dialog.terminal-log-mode .terminal-demo-close{border-radius:5px;padding:4px 10px;background:#122c56}
    #terminal-demo-dialog.terminal-log-mode .terminal-demo-content{display:flex;flex:1;flex-direction:column;min-height:0;max-height:none;padding:14px 22px 22px;overflow:hidden}
    .terminal-log-tabs{display:flex;flex:none;gap:4px;overflow-x:auto;margin:0 0 12px;border-bottom:1px solid var(--rule,rgba(156,221,255,.38))}
    .terminal-log-tabs .tab{flex:none;max-width:260px;padding:10px 12px;border:0;border-bottom:3px solid transparent;background:transparent;color:var(--sub,#c7d9ed);font:600 14px/1.35 system-ui;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
    .terminal-log-tabs .tab[aria-selected="true"]{border-bottom-color:var(--accent,#9cddff);color:var(--accent,#9cddff)}
    .terminal-log-panel h3{margin:8px 0 6px;color:#cce8ff;font:600 14px/1.4 system-ui}
    .terminal-log-command-heading{display:flex;align-items:center;justify-content:space-between;gap:12px}
    .terminal-log-command-actions{display:flex;align-items:center;gap:10px}
    .terminal-log-panel pre{margin:0;flex:1;min-height:0;overflow:auto;max-height:none;padding:13px;border:1px solid #294665;border-radius:8px;background:#050e1b;color:#e7f0fc;font:13px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;overflow-wrap:anywhere}
    .terminal-log-line{display:grid;grid-template-columns:36px minmax(0,1fr);min-width:100%;white-space:pre-wrap}
    .terminal-log-line-number{padding-right:10px;color:#7890ad;text-align:right;user-select:none}
    .terminal-log-line-text{min-width:0;white-space:pre-wrap;overflow-wrap:anywhere}
    .terminal-log-line.is-log-highlight{background:rgba(83,163,255,.18);box-shadow:inset 3px 0 #9cddff}
    .terminal-log-line.is-log-highlight .terminal-log-line-number{color:#c5e8ff;font-weight:700}
    .terminal-log-explanation{margin:8px 0 0;padding-left:20px;color:#dce8f5;font:14px/1.6 system-ui}
    .terminal-log-explanation li{padding:8px 8px;cursor:pointer}
    .terminal-log-explanation li.is-explanation-selected{background:rgba(83,163,255,.16);box-shadow:inset 3px 0 #9cddff}
    .terminal-log-panel{display:grid;flex:1;min-height:0;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);grid-template-rows:auto auto minmax(0,1fr);gap:0 20px;align-items:start;overflow:hidden}
    .terminal-log-panel>[data-log-command]{grid-column:1/-1}
    .terminal-log-panel>[data-log-command].terminal-log-command-code{flex:none;margin:0 0 6px;padding:9px 12px;border:1px solid #294665;border-radius:6px;background:#07152e;color:#e7f0fc;font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;overflow-wrap:anywhere}
    .terminal-log-result,.terminal-log-explanation-pane{display:flex;flex-direction:column;min-width:0;min-height:0;overflow:auto}
    .terminal-log-result{grid-column:1;grid-row:3;align-self:start}
    .terminal-log-explanation-pane{grid-column:2;grid-row:3}
    .terminal-log-result pre{flex:none;max-height:min(58vh,560px);overflow:auto}
    .terminal-demo-copy{display:inline-grid;width:34px;height:34px;place-items:center;border:1px solid #3b817b;border-radius:7px;padding:0;background:#22776f;color:#fff;cursor:pointer}
    .terminal-demo-copy:hover{background:#2b9388}
    .terminal-demo-copy svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:1.8}
    .terminal-demo-status{color:#a9c5dd;font:13px system-ui}.terminal-demo-fallback{width:100%;min-height:68px;margin-top:10px;padding:10px;border:1px solid #7188a1;border-radius:6px;background:#071222;color:#fff;font:12px/1.5 ui-monospace,monospace}
    @media(max-width:700px){.slide[data-evaluation="EVQ-001"] .body,.slide[data-evaluation="EVQ-002"] .body,.slide[data-evaluation="EVQ-003"] .body,.slide[data-evaluation="EVQ-004"] .body,.slide[data-evaluation="EVQ-005"] .body,.slide[data-evaluation="EVQ-006"] .body,.slide[data-evaluation="EVQ-007"] .body{gap:14px}.terminal-inline-commands{padding:10px 12px}.terminal-inline-commands>h3{font-size:15px}.terminal-demo-head,.terminal-demo-content{padding-left:14px;padding-right:14px}.terminal-log-tabs .tab{max-width:180px;padding:9px 10px;font-size:12px}.terminal-log-panel{grid-template-columns:minmax(0,1fr);grid-template-rows:auto auto minmax(160px,auto) minmax(160px,auto);overflow:auto}.terminal-log-panel>[data-log-command],.terminal-log-result,.terminal-log-explanation-pane{grid-column:1}.terminal-log-result{grid-row:3}.terminal-log-explanation-pane{grid-row:4}.terminal-log-result pre{max-height:34vh}.terminal-log-panel pre{font-size:12px}.terminal-demo-item{padding:10px}.terminal-demo-item pre{font-size:12px}}
    @media(prefers-reduced-motion:reduce){#terminal-demo-dialog::backdrop{backdrop-filter:none}}
  `;
  document.head.append(styles);

  const dialog = document.createElement('dialog');
  dialog.id = 'terminal-demo-dialog';
  dialog.setAttribute('aria-labelledby', 'terminal-demo-title');
  dialog.innerHTML = '<div class="terminal-demo-head"><h2 id="terminal-demo-title"></h2><button class="terminal-demo-close" type="button">닫기</button></div><div class="terminal-demo-content"></div>';
  document.body.append(dialog);
  const content = dialog.querySelector('.terminal-demo-content');
  const title = dialog.querySelector('#terminal-demo-title');
  const close = dialog.querySelector('.terminal-demo-close');
  let launcher = null;
  let logLauncher = null;
  let dialogTrigger = null;

  function copyFallback(code, parent, status) {
    const field = document.createElement('textarea');
    field.className = 'terminal-demo-fallback';
    field.readOnly = true;
    field.setAttribute('aria-label', '직접 선택해 복사할 명령');
    field.value = code;
    parent.append(field);
    field.focus();
    field.select();
    status.textContent = '자동 복사에 실패했어요. 선택된 명령을 복사하세요.';
  }

  function createCopyButton(code, status, onFailure) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'terminal-demo-copy';
    button.setAttribute('aria-label', '명령 복사');
    button.title = '명령 복사';
    button.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="2"></rect><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"></path></svg>';
    button.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error('clipboard unavailable');
        await navigator.clipboard.writeText(code);
        status.textContent = '복사했어요. 터미널에 붙여 넣으세요.';
      } catch {
        onFailure();
      }
    });
    return button;
  }

  function addCommand(command) {
    const item = document.createElement('section');
    item.className = 'terminal-demo-item';
    const heading = document.createElement('h3');
    heading.textContent = command.title;
    const pre = document.createElement('pre');
    const code = document.createElement('code');
    code.textContent = command.code;
    pre.append(code);
    item.append(heading, pre);
    const actions = document.createElement('div');
    actions.className = 'terminal-demo-actions';
    const status = document.createElement('span');
    status.className = 'terminal-demo-status';
    status.setAttribute('role', 'status');
    const button = createCopyButton(command.code, status, () => {
      item.querySelector('.terminal-demo-fallback')?.remove();
      copyFallback(command.code, item, status);
    });
    actions.append(button, status);
    item.append(actions);
    content.append(item);
  }

  function renderInlineCommands(slide, config) {
    slide.querySelector('.terminal-inline-commands')?.remove();
    const panel = document.createElement('section');
    panel.className = 'terminal-inline-commands';
    panel.setAttribute('aria-label', '시연 명령어');
    const heading = document.createElement('h3');
    heading.textContent = '시연 명령어';
    panel.append(heading);
    config.commands.forEach(command => {
      const item = document.createElement('section');
      item.className = 'terminal-demo-item';
      const commandHeading = document.createElement('h3');
      commandHeading.textContent = command.title;
      const pre = document.createElement('pre');
      const code = document.createElement('code');
      code.textContent = command.code;
      pre.append(code);
      item.append(commandHeading, pre);
      const actions = document.createElement('div');
      actions.className = 'terminal-demo-actions';
      const status = document.createElement('span');
      status.className = 'terminal-demo-status';
      status.setAttribute('role', 'status');
      const button = createCopyButton(command.code, status, () => {
        item.querySelector('.terminal-demo-fallback')?.remove();
        copyFallback(command.code, item, status);
      });
      actions.append(button, status);
      item.append(actions);
      panel.append(item);
    });
    slide.querySelector('.body')?.append(panel);
  }

  function renderCommands(config) {
    title.textContent = `터미널 시연 · ${config.title}`;
    content.replaceChildren();
    config.commands.forEach(addCommand);
  }

  function selectLogExplanation(item) {
    const panel = item.closest('.terminal-log-panel');
    const selectedLines = new Set((item.dataset.outputLines || '').split(',').map(Number).filter(Number.isFinite));
    let firstLine;
    panel.querySelectorAll('.terminal-log-line').forEach(line => {
      const selected = selectedLines.has(Number(line.dataset.logLine));
      line.classList.toggle('is-log-highlight', selected);
      if (selected && !firstLine) firstLine = line;
    });
    panel.querySelectorAll('.terminal-log-explanation li').forEach(explanation => {
      const selected = explanation === item;
      explanation.classList.toggle('is-explanation-selected', selected);
      explanation.setAttribute('aria-pressed', String(selected));
    });
    if (firstLine) firstLine.scrollIntoView({block:'nearest', behavior:matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  }

  function renderLogOutput(output, text) {
    text.split('\n').forEach((lineText, index) => {
      const line = document.createElement('span');
      line.className = 'terminal-log-line';
      line.dataset.logLine = String(index + 1);
      const number = document.createElement('span');
      number.className = 'terminal-log-line-number';
      number.textContent = String(index + 1);
      const value = document.createElement('span');
      value.className = 'terminal-log-line-text';
      value.textContent = lineText;
      line.append(number, value);
      output.append(line);
    });
  }

  function showLogs(config) {
    dialogTrigger = logLauncher;
    dialog.classList.add('terminal-log-mode');
    title.textContent = `시연 로그 · ${config.title}`;
    content.replaceChildren();
    const tabs = document.createElement('div');
    tabs.className = 'terminal-log-tabs';
    tabs.setAttribute('role', 'tablist');
    const panels = [];
    config.logs.forEach((log, index) => {
      const tabId = `terminal-log-tab-${index}`;
      const panelId = `terminal-log-panel-${index}`;
      const tab = document.createElement('button');
      tab.type = 'button';
      tab.className = 'tab';
      tab.id = tabId;
      tab.dataset.tab = panelId;
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-selected', String(index === 0));
      tab.setAttribute('aria-controls', panelId);
      tab.textContent = `${String(index + 1).padStart(2, '0')} · ${log.title}`;
      tabs.append(tab);

      const panel = document.createElement('section');
      panel.className = 'tab-panel terminal-log-panel';
      panel.id = panelId;
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', tabId);
      panel.hidden = index !== 0;
      const command = config.commands[log.commandIndex ?? index];
      const commandHeading = document.createElement('h3');
      commandHeading.className = 'terminal-log-command-heading';
      commandHeading.textContent = '실행한 명령어';
      commandHeading.dataset.logCommand = 'true';
      const commandCode = document.createElement('pre');
      commandCode.className = 'terminal-log-command-code';
      commandCode.dataset.logCommand = 'true';
      commandCode.textContent = command?.code || '';
      commandCode.tabIndex = -1;
      const commandActions = document.createElement('span');
      commandActions.className = 'terminal-log-command-actions';
      const commandCopyStatus = document.createElement('span');
      commandCopyStatus.className = 'terminal-demo-status';
      commandCopyStatus.setAttribute('role', 'status');
      const commandCopyButton = createCopyButton(command?.code || '', commandCopyStatus, () => {
        const range = document.createRange();
        range.selectNodeContents(commandCode);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        commandCopyStatus.textContent = '자동 복사에 실패했어요. 선택된 명령을 복사하세요.';
        commandCode.focus({preventScroll:true});
      });
      commandActions.append(commandCopyButton, commandCopyStatus);
      commandHeading.append(commandActions);
      const outputHeading = document.createElement('h3');
      outputHeading.textContent = '터미널 출력';
      const output = document.createElement('pre');
      const outputLines = log.output.split('\n');
      renderLogOutput(output, log.output);
      const resultPane = document.createElement('div');
      resultPane.className = 'terminal-log-result';
      resultPane.append(outputHeading, output);
      const explanation = document.createElement('ul');
      explanation.className = 'terminal-log-explanation';
      log.explanation.forEach((text, explanationIndex) => {
        const item = document.createElement('li');
        item.textContent = text;
        item.tabIndex = 0;
        item.setAttribute('role', 'group');
        item.setAttribute('aria-pressed', 'false');
        item.dataset.outputLines = (log.explanationLines?.[explanationIndex] || outputLines.map((_, lineIndex) => lineIndex + 1)).join(',');
        item.addEventListener('click', () => selectLogExplanation(item));
        item.addEventListener('keydown', event => {
          if (event.key !== 'Enter' && event.key !== ' ') return;
          event.preventDefault();
          event.stopPropagation();
          selectLogExplanation(item);
        });
        explanation.append(item);
      });
      const explanationPane = document.createElement('div');
      explanationPane.className = 'terminal-log-explanation-pane';
      const explanationHeading = document.createElement('h3');
      explanationHeading.textContent = '로그 설명';
      explanationPane.append(explanationHeading, explanation);
      panel.append(commandHeading, commandCode, resultPane, explanationPane);
      panels.push(panel);
      tabs.addEventListener('click', () => {
        tabs.querySelectorAll('.tab').forEach(item => item.setAttribute('aria-selected', String(item === tab)));
        panels.forEach(item => { item.hidden = item !== panel; });
      });
    });
    content.append(tabs, ...panels);
    if (!dialog.open) dialog.showModal();
    tabs.querySelector('.tab')?.focus({preventScroll: true});
  }

  function showCommands(config) {
    dialogTrigger = launcher;
    dialog.classList.remove('terminal-log-mode');
    renderCommands(config);
    dialog.showModal();
    close.focus();
  }

  function updateLauncher() {
    const slide = document.querySelector('.slide.active');
    const config = commandMap[slide?.dataset.evaluation]
      || slide?.dataset.evaluation?.split(/\s+/).map(id => commandMap[id]).find(Boolean);
    if (!config) {
      launcher?.remove();
      launcher = null;
      logLauncher?.remove();
      logLauncher = null;
      return;
    }
    const isPrimaryDemoSlide = ['EVQ-001', 'EVQ-002', 'EVQ-003', 'EVQ-004', 'EVQ-005', 'EVQ-006', 'EVQ-007'].includes(slide?.dataset.evaluation);
    if (isPrimaryDemoSlide) {
      launcher?.remove();
      launcher = null;
      renderInlineCommands(slide, config);
    } else {
      launcher?.remove();
      launcher = null;
      slide.querySelector('.terminal-inline-commands')?.remove();
    }
    if (config.logs?.length) {
      if (!logLauncher) {
        logLauncher = document.createElement('button');
        logLauncher.type = 'button';
        logLauncher.className = 'code-btn terminal-log-launch';
      }
      logLauncher.textContent = `로그 보기 (${config.logs.length})`;
      logLauncher.setAttribute('aria-haspopup', 'dialog');
      logLauncher.onclick = () => showLogs(config);
      let actions = slide.querySelector('.slide-actions');
      if (!actions) {
        actions = document.createElement('div');
        actions.className = 'slide-actions';
        slide.querySelector('header')?.append(actions);
      }
      actions.append(logLauncher);
    } else {
      logLauncher?.remove();
      logLauncher = null;
    }
  }

  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    dialogTrigger?.focus();
    dialogTrigger = null;
  });
  window.addEventListener('keydown', event => {
    if (!dialog.open) return;
    if (event.key === 'Escape') {
      event.preventDefault();
      event.stopImmediatePropagation();
      dialog.close();
      return;
    }
    if (event.code === 'KeyW' || event.key.toLowerCase() === 'w' || event.key === 'ㅈ') {
      event.preventDefault();
      event.stopImmediatePropagation();
      dialog.close();
      return;
    }
    if (dialog.classList.contains('terminal-log-mode') && (event.key === 'ArrowUp' || event.key === 'ArrowDown')) {
      const panel = dialog.querySelector('.terminal-log-panel:not([hidden])');
      const items = [...(panel?.querySelectorAll('.terminal-log-explanation li') || [])];
      if (!items.length) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      const selectedIndex = items.findIndex(item => item.classList.contains('is-explanation-selected'));
      const nextIndex = selectedIndex < 0 ? (event.key === 'ArrowDown' ? 0 : items.length - 1)
        : Math.max(0, Math.min(items.length - 1, selectedIndex + (event.key === 'ArrowDown' ? 1 : -1)));
      const item = items[nextIndex];
      selectLogExplanation(item);
      item.focus({preventScroll:true});
      item.scrollIntoView({block:'nearest'});
      return;
    }
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      if (dialog.querySelector('.tab')) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      const slides = document.querySelectorAll('.slide');
      const current = Number(location.hash.slice(1)) || 1;
      const direction = event.key === 'ArrowRight' ? 1 : -1;
      const next = Math.max(1, Math.min(slides.length, current + direction));
      dialog.close();
      if (next !== current) location.hash = `#${next}`;
      return;
    }
    event.stopImmediatePropagation();
  }, true);

  let commandMap = {};
  fetch(new URL('terminal-demo.json', document.currentScript?.src || location.href))
    .then(response => {
      if (!response.ok) throw new Error('시연 명령을 불러오지 못했습니다.');
      return response.json();
    })
    .then(data => {
      commandMap = data;
      updateLauncher();
      new MutationObserver(mutations => {
        if (mutations.some(({ target }) => target.matches?.('.slide'))) updateLauncher();
      }).observe(document.querySelector('main'), {
        subtree: true,
        attributes: true,
        attributeFilter: ['class'],
      });
    })
    .catch(error => console.error(error));
})();
