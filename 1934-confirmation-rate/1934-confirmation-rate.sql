# Write your MySQL query statement below
SELECT
  Signups.user_id,
  ROUND(COUNT(CASE WHEN Confirmations.action = "confirmed" THEN 1 END) / COUNT(*), 2) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
ON Signups.user_id = Confirmations.user_id
GROUP BY Signups.user_id;
