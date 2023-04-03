SELECT
  hacker_id,
  name,
  SUM(MaxChallengeScore) AS total_score
FROM
  (
    SELECT
      Submissions.hacker_id AS hacker_id,
      name,
      MAX(Submissions.score) AS MaxChallengeScore
    FROM
      Submissions
      JOIN Hackers ON Submissions.hacker_id = Hackers.hacker_id
    WHERE
      Submissions.score != 0
    GROUP BY
      Submissions.challenge_id,
      Submissions.hacker_id,
      name
  ) AS T1
GROUP BY
  hacker_id,
  name
ORDER BY
  total_score DESC,
  hacker_id ASC;
