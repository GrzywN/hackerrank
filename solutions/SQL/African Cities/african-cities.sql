SELECT
  CITY.name AS 'African city'
FROM
  CITY
  JOIN Country ON CITY.CountryCode = COUNTRY.Code
WHERE
  Continent LIKE 'Africa';
