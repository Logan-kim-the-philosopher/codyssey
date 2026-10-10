'use strict';
const $ = id => document.getElementById(id);
const storageKey = 'b2-1-budget-demo-v1';
const money = value => `${Number(value || 0).toLocaleString('ko-KR')}원`;
const today = new Date();
const localDate = `${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,'0')}-${String(today.getDate()).padStart(2,'0')}`;
let state = { transactions: [], budgets: [] };
let response = null;
let busy = false;
let categories = [];
const categoryNames = {food:'식비',transport:'교통',rent:'주거',salary:'급여 · 용돈',shopping:'쇼핑',medical:'의료',education:'교육',other:'기타'};
const categoryLabel = name => categoryNames[name] || name;
try { const saved = JSON.parse(localStorage.getItem(storageKey)); if (saved && Array.isArray(saved.transactions) && Array.isArray(saved.budgets)) state = saved; } catch { $('status').textContent = '브라우저 저장 데이터를 읽지 못했습니다. 새 기록으로 시작합니다.'; }
$('date').value = localDate;
$('month').value = localDate.slice(0,7);
function message(text, error=false) { $('status').textContent=text; $('status').classList.toggle('error',error); }
function setBusy(value) { busy=value; document.querySelectorAll('button').forEach(button => button.disabled=value); $('month').disabled=value; }
async function request(action, fields={}) {
  if(busy) return false;
  setBusy(true); message('처리 중…');
  try {
    const result = await fetch('/api/budget', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action,state,month:$('month').value,...fields})});
    const data = await result.json();
    if(!result.ok) throw new Error(typeof data.error === 'string' ? data.error : data.error?.message || data.message || '요청을 처리하지 못했습니다.');
    if(!data.state || !Array.isArray(data.state.transactions)) throw new Error('서버 응답 형식이 올바르지 않습니다.');
    if(action !== 'view') {
      try { localStorage.setItem(storageKey, JSON.stringify(data.state)); } catch { throw new Error('브라우저에 저장할 공간이 부족하거나 저장이 차단돼 있습니다. 기록을 저장하지 않았습니다.'); }
    }
    state=data.state; response=data; categories=data.categories || categories;
    updateCategories(); render(); message(action==='view' ? '조회 완료' : '저장했습니다.');
    return true;
  } catch(error) { message(error instanceof TypeError ? '서버에 연결하지 못했습니다. 네트워크를 확인한 뒤 조회 월을 다시 선택해 주세요.' : error instanceof Error ? error.message : '연결에 실패했습니다. 잠시 후 다시 시도해 주세요.',true); return false; }
  finally { setBusy(false); }
}
function updateCategories() {
  const old=$('category').value;
  const kind=$('type').value;
  const values=Array.isArray(categories) ? categories : categories[kind] || [];
  $('category').replaceChildren();
  for(const item of values) {
    const name=typeof item==='string' ? item : item.name || item.category;
    if(!name) continue;
    const option=document.createElement('option'); option.value=name; option.textContent=categoryLabel(name); $('category').append(option);
  }
  if([...$('category').options].some(option=>option.value===old)) $('category').value=old;
}
function element(tag, text, className) { const node=document.createElement(tag); if(text!==undefined) node.textContent=text; if(className)node.className=className; return node; }
function render() {
  const summary=response?.summary || {};
  $('income').textContent=money(summary.income); $('expense').textContent=money(summary.expense); $('balance').textContent=money(summary.balance);
  const budget=summary.budget;
  $('budget-value').textContent=budget ? `${Math.round(Number(summary.expense || 0)/Number(budget.amount)*100)}%` : '미설정';
  $('budget-detail').textContent=budget ? `${money(budget.amount)} 중 ${money(summary.expense)} 사용` : '월 예산을 설정해 보세요';
  $('budget-month').textContent=$('month').value;
  $('budget-amount').value=budget?.amount || '';
  const totals=$('category-totals'); totals.replaceChildren();
  const categoryTotals=summary.category_totals || {};
  const entries=Array.isArray(categoryTotals) ? categoryTotals.map(item=>Array.isArray(item) ? item : [item.category,item.amount || item.total]) : Object.entries(categoryTotals);
  entries.forEach(([name,value])=>totals.append(element('span',`${categoryLabel(name)} ${money(value)}`,'total-chip')));
  if(!entries.length)totals.append(element('span','아직 지출 기록이 없습니다.','total-chip'));
  renderTransactions();
}
function renderTransactions() {
  const container=$('transactions'); container.replaceChildren();
  const term=$('search').value.trim().toLowerCase();
  const transactions=(response?.transactions || []).filter(item=>item.date?.startsWith($('month').value)).filter(item=>`${categoryLabel(item.category)} ${item.category} ${item.memo || ''} ${(item.tags || []).join(' ')}`.toLowerCase().includes(term));
  $('count').textContent=`${transactions.length}건`;
  if(!transactions.length) { container.append(element('p',term ? '검색 결과가 없습니다.' : '이번 달의 첫 거래를 기록해 보세요.','empty')); return; }
  transactions.forEach(item=>{
    const row=element('div',undefined,'transaction');
    const info=element('div',undefined,'transaction-info'); info.append(element('strong',categoryLabel(item.category)),element('p',item.memo || (item.type==='income' ? '수입 기록' : '지출 기록')),element('small',`${item.date} ${(item.tags || []).map(tag=>`#${tag}`).join(' ')}`));
    const amount=element('span',`${item.type==='income' ? '+' : '−'}${money(item.amount)}`,`transaction-amount ${item.type}`);
    const remove=element('button','삭제','delete'); remove.type='button'; remove.setAttribute('aria-label',`${item.date} ${item.category} ${money(item.amount)} 삭제`); remove.disabled=busy; remove.addEventListener('click',()=>request('delete',{transaction_id:item.id}));
    row.append(info,amount,remove); container.append(row);
  });
}
$('transaction-form').addEventListener('submit',async event=>{event.preventDefault(); if(await request('add',{transaction_type:$('type').value,transaction_date:$('date').value,category:$('category').value,amount:Number($('amount').value),memo:$('memo').value,tags:$('tags').value.split(',').map(value=>value.trim()).filter(Boolean)})){ $('amount').value=''; $('memo').value=''; $('tags').value=''; }});
$('budget-form').addEventListener('submit',event=>{event.preventDefault();request('budget',{amount:Number($('budget-amount').value)});});
$('month').addEventListener('change',()=>{if($('month').value)request('view');});
$('type').addEventListener('change',updateCategories);
$('search').addEventListener('input',renderTransactions);
$('sample').addEventListener('click',()=>{$('type').value='expense';updateCategories();$('date').value=localDate;$('amount').value='6500';$('memo').value='친구와 점심';$('tags').value='학교, 점심';$('amount').focus();message('예시를 채웠습니다. 기록 저장을 눌러 Python 검증을 체험하세요.');});
$('backup').addEventListener('click',()=>{const link=document.createElement('a');const url=URL.createObjectURL(new Blob([JSON.stringify(state,null,2)],{type:'application/json'}));link.href=url;link.download=`budget-backup-${localDate}.json`;link.click();URL.revokeObjectURL(url);});
request('view');
