-- Last updated: 8/5/2025, 2:52:40 PM
# Write your MySQL query statement below
SELECT
    transaction_id
FROM    
    Transactions
WHERE
    (day,amount) IN
    (SELECT
        day,
        MAX(amount) 
    FROM
        Transactions
    GROUP BY
        day)
ORDER BY
    transaction_id;



