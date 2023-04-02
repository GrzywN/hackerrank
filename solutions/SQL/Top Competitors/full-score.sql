SELECT
  Hackers.hacker_id AS hacker_id,
  Hackers.name AS name
FROM
  Submissions
  JOIN Hackers ON Submissions.hacker_id = Hackers.hacker_id
  JOIN Challenges ON Submissions.challenge_id = Challenges.challenge_id
  JOIN Difficulty ON Challenges.difficulty_level = Difficulty.difficulty_level
WHERE
  Submissions.score = Difficulty.score
GROUP BY
  Hackers.hacker_id,
  Hackers.name
HAVING
  COUNT(Hackers.hacker_id) >= 2
ORDER BY
  COUNT(Hackers.hacker_id) DESC,
  Hackers.hacker_id ASC;
