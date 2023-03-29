SET
  @row_index := -1;

SELECT
  ROUND(
    AVG(Lat_n),
    4
  ) AS Median
FROM
  (
    SELECT
      Lat_n,
      @row_index := @row_index + 1 AS RowIndex
    FROM
      Station
    ORDER BY
      Lat_n ASC
  ) AS Subquery
WHERE
  Subquery.RowIndex IN (
    FLOOR(@row_index / 2),
    CEIL(@row_index / 2)
  );
