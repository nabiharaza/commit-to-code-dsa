-- Last updated: 8/5/2025, 2:54:17 PM
SELECT
    MIN(log_id) AS start_id, 
    MAX(log_id) AS end_id
FROM
    (SELECT
        log_id,
        ROW_NUMBER() OVER (ORDER BY log_id) AS num
    FROM
        Logs) AS temp 
GROUP BY
    log_id - num
ORDER BY
    start_id



