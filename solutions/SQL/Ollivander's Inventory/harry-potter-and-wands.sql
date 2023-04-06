SELECT
  id,
  age,
  coins_needed,
  power
FROM
  Wands
  JOIN Wands_Property ON Wands.code = Wands_Property.code
WHERE
  is_evil = 0
  AND coins_needed = (
    SELECT
      MIN(coins_needed)
    FROM
      Wands AS W1
      JOIN Wands_Property AS P1 ON W1.code = P1.code
    WHERE
      W1.power = Wands.power
      AND P1.age = Wands_Property.age
  )
ORDER BY
  power DESC,
  age DESC;
