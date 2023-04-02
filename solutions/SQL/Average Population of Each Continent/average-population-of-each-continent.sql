SELECT
  Continent,
  FLOOR(
    AVG(City.Population)
  ) AS 'Average Population'
FROM
  City
  JOIN Country ON City.CountryCode = Country.Code
GROUP BY
  Continent;
