SELECT
  salary * months,
  COUNT(salary * months)
FROM
  Employee
WHERE
  salary * months IN (
    SELECT
      MAX(salary * months) AS max_salary
    FROM
      Employee
  )
GROUP BY
  salary * months;
