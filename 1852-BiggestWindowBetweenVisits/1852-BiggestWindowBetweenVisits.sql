-- Last updated: 8/5/2025, 2:52:57 PM
SELECT
    user_id,
    MAX(w) AS biggest_window 
FROM
    (SELECT
        *,
        DATEDIFF(IFNULL(LEAD(visit_date, 1) OVER (PARTITION BY user_id ORDER BY visit_date), '2021-01-01'), visit_date) AS w
    FROM
        UserVisits) AS temp
GROUP BY
    user_id
ORDER BY
    user_id


