-- Last updated: 8/5/2025, 2:55:02 PM
SELECT
    A.player_id,
    A.device_id
FROM
    Activity A
WHERE
    (A.player_id, A.event_date) IN 
    (SELECT
        DISTINCT B.player_id,
        MIN(B.event_date) AS event_date
    FROM
        Activity B
    GROUP BY
        B.player_id);

