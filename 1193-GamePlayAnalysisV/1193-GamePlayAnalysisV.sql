-- Last updated: 8/5/2025, 2:54:59 PM
# Write your MySQL query statement below
SELECT install_dt, COUNT(DISTINCT player_id) installs,
ROUND(SUM(event_date = install_dt + INTERVAL 1 DAY) / COUNT(DISTINCT player_id),2) Day1_retention
FROM
(SELECT *, MIN(event_date) OVER(PARTITION BY player_id ORDER BY event_date) install_dt FROM activity) temp
GROUP BY 1