SELECT
  DISTINCT City
FROM
  Station
WHERE
  (
    City NOT LIKE 'A%'
    AND City NOT LIKE 'E%'
    AND City NOT LIKE 'I%'
    AND City NOT LIKE 'O%'
    AND City NOT LIKE 'U%'
  )
  AND (
    City NOT LIKE '%a'
    AND City NOT LIKE '%e'
    AND City NOT LIKE '%i'
    AND City NOT LIKE '%o'
    AND City NOT LIKE '%u'
  );
