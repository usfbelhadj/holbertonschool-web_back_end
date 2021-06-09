export default function appendToEachArrayValue(array, appendString) {
  const tab = [];
  for (const string of array) {
    tab.push(appendString + string);
  }

  return tab;
}
