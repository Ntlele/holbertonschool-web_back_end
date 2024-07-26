export default function cleanSet(set, startString) {
  const result = [];

  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  }

  return result.join('-');
}
