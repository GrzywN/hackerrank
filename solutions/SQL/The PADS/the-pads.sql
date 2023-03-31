SELECT
  CONCAT(
    Name,
    '(',
    LEFT(Occupation, 1),
    ')'
  ) AS FormattedString
FROM
  Occupations
UNION
SELECT
  CONCAT(
    'There are a total of ',
    COUNT(Occupation),
    ' ',
    LOWER(Occupation),
    's.'
  ) AS FormattedString
FROM
  Occupations
GROUP BY
  Occupation
ORDER BY
  FormattedString ASC;
