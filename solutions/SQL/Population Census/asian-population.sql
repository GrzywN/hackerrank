SELECT
  SUM(City.Population) AS 'Sum of population of Asian cities.'
FROM
  City
  JOIN Country ON City.CountryCode = Country.Code
WHERE
  Continent LIKE 'Asia';
