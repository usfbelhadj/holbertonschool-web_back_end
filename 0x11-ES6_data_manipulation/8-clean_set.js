export default function cleanSet(set, startString) {
  const l = [];
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  for (const x of set) {
    if (typeof x === 'string' && x.startsWith(startString)) {
      l.push(x.slice(startString.length));
    }
  }
  return l.join('-');
}
