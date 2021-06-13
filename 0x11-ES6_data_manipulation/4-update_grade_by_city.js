export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Array.isArray(students) === false) {
    return [];
  }
  return students.filter((x) => x.location === city).map((x) => {
    const [newGrade] = newGrades.filter((item) => item.studentId === x.id);
    return { ...x, grade: newGrade ? newGrade.grade : 'N/A' };
  });
}
