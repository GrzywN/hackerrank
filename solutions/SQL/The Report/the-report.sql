WITH JoinedStudentsAndGrades AS (
  SELECT
    Name,
    Grade,
    Marks
  FROM
    Students
    JOIN Grades ON Students.Marks >= Grades.Min_mark
    AND Students.Marks <= Grades.Max_Mark
)

SELECT
  CASE WHEN Grade < 8 THEN NULL ELSE Name END,
  Grade,
  Marks
FROM
  JoinedStudentsAndGrades
ORDER BY
  Grade DESC,
  Name ASC,
  Marks ASC;
