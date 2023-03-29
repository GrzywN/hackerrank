SELECT
  N,
  IF(
    P IS NULL,
    'Root',
    IF(
      (N, 2) IN (
        SELECT
          P AS N,
          COUNT(P)
        FROM
          BST
        GROUP BY
          P
        HAVING
          COUNT(P) = 2
      ),
      'Inner',
      'Leaf'
    )
  ) AS TypeOfNode
FROM
  BST
ORDER BY
  N ASC;
