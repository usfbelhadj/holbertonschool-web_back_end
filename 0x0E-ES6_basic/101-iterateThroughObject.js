export default function iterateThroughObject(reportWithIterator) {
    const employees = [];
    for ( const i in reportWithIterator) {
      employees.push(i);
    }
  
    return employees.join(' | ');
  }