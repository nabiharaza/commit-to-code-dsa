-- Last updated: 8/5/2025, 2:52:53 PM
# Write your MySQL query statement below
SELECT
    DISTINCT l1.account_id
FROM
    LogInfo l1
JOIN
    LogInfo l2
WHERE
    l1.account_id = l2.account_id
    AND l1.ip_address != l2.ip_address
    AND l1.login BETWEEN l2.login AND l2.logout;
