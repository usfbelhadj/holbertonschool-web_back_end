export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw Error('Cannot process');
  }
  groceries.forEach((k, v) => {
    if (k === 1) {
      groceries.set(v, 100);
    }
  });
  return groceries;
}
