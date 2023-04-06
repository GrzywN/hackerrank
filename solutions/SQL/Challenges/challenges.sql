-- Oracle

SELECT
  Hackers.hacker_id,
  Hackers.name,
  COUNT(challenge_id)
FROM
  Challenges
  JOIN Hackers ON Challenges.hacker_id = Hackers.hacker_id
GROUP BY
  Hackers.hacker_id,
  Hackers.name
HAVING
  COUNT(challenge_id) = (
    SELECT
      MAX(challenges_created)
    FROM
      (
        SELECT
          COUNT(challenge_id) AS challenges_created
        FROM
          Challenges
        GROUP BY
          hacker_id
      ) Subquery
  )
  OR COUNT(challenge_id) IN (
    SELECT
      cnt
    FROM
      (
        SELECT
          COUNT(*) AS cnt
        FROM
          Challenges
        GROUP BY
          hacker_id
      ) Subquery
    GROUP BY
      cnt
    HAVING
      COUNT(cnt) = 1
  )
ORDER BY
  COUNT(challenge_id) DESC,
  Hackers.hacker_id;
