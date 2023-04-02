SELECT
  ROUND(
    ABS(a - c) + ABS(b - d),
    4
  ) AS 'Manhattan Distance'
FROM
  (
    SELECT
      MIN(Lat_n) AS a
    FROM
      Station
  ) AS T1,
  (
    SELECT
      MIN(Long_w) AS b
    FROM
      Station
  ) AS T2,
  (
    SELECT
      MAX(Lat_n) AS c
    FROM
      Station
  ) AS T3,
  (
    SELECT
      MAX(Long_w) AS d
    FROM
      Station
  ) AS T4;

-- Shorter version
-- SELECT ROUND(ABS(MAX(Lat_n) - MIN(Lat_n)) + ABS(MAX(Long_w) - MIN(Long_w)), 4) AS 'Manhattan Distance' FROM Station;
