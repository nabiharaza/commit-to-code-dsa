-- Last updated: 8/5/2025, 2:54:12 PM
SELECT
    DISTINCT visited_on,
    SUM(amount) over W AS amount,
    ROUND(SUM(amount) over W / 7, 2) AS average_amount
FROM
    Customer
WINDOW W AS (
    ORDER BY visited_on
    RANGE BETWEEN INTERVAL 6 day PRECEDING and CURRENT ROW
)
LIMIT 6, 999