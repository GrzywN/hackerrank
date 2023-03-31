SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', ''))) AS Error FROM Employees;
