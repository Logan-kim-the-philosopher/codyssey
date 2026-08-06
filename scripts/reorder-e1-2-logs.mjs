#!/usr/bin/env node

import fs from 'fs';

const statePath = '/Users/hskim/Projects/codyssey/artifacts/e1-2/state.json';
const jsonlPath = '/Users/hskim/Projects/codyssey/artifacts/e1-2/logs/practice.jsonl';

const desiredOrder = [
  'log-1',
  'log-2',
  'log-24',
  'log-3',
  'log-4',
  'log-5',
  'log-6',
  'log-25',
  'log-7',
  'log-8',
  'log-9',
  'log-10',
  'log-11',
  'log-26',
  'log-12',
  'log-13',
  'log-27',
  'log-14',
  'log-15',
  'log-16',
  'log-28',
  'log-17',
  'log-18',
  'log-19',
  'log-20',
  'log-29',
  'log-21',
  'log-22',
  'log-30',
  'log-23',
  'log-31',
];

function reorder(items) {
  const byId = new Map(items.map((item) => [item.id, item]));
  const reordered = desiredOrder.map((id) => {
    const item = byId.get(id);
    if (!item) {
      throw new Error(`Missing log: ${id}`);
    }
    return item;
  });

  if (reordered.length !== items.length) {
    const extras = items
      .map((item) => item.id)
      .filter((id) => !desiredOrder.includes(id));
    throw new Error(`Unexpected extra logs: ${extras.join(', ')}`);
  }

  return reordered;
}

const state = JSON.parse(fs.readFileSync(statePath, 'utf8'));
state.logs = reorder(state.logs);
fs.writeFileSync(statePath, `${JSON.stringify(state, null, 2)}\n`, 'utf8');

fs.writeFileSync(
  jsonlPath,
  `${state.logs.map((log) => JSON.stringify(log)).join('\n')}\n`,
  'utf8',
);

console.log('Reordered E1-2 logs for natural practice-to-commit flow.');
