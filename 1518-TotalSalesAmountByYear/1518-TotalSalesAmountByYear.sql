-- Last updated: 8/5/2025, 2:54:05 PM
# Write your MySQL query statement below
WITH RECURSIVE s1 AS ( -- 1. creating another table including all sales dates for each product
    SELECT
        product_id,
        period_start,
        period_end,
        average_daily_sales,
        period_start AS p_date -- 2. we call it `p_date`, and the counting starts from `period_start` date
    FROM
        Sales
    UNION ALL -- 3. constructing the recursive part
    SELECT
        product_id,
        period_start,
        period_end,
        average_daily_sales,
        DATE_ADD(p_date, INTERVAL 1 DAY) -- 4. one day at a time
    FROM
        s1
    WHERE -- 5. until the following condition is met (from period_start to period_end)
        DATE_ADD(p_date, INTERVAL 1 DAY) <= (SELECT period_end FROM Sales WHERE product_id = s1.product_id)
)

SELECT /*+ SET_VAR(cte_max_recursion_depth = 1M) */
-- adding this line to make the solution more scalable (not necessary for the provided testcases)
-- i.e. when we have a lot more products or the timespan is larger
    product_id,
    product_name,
    LEFT(p_date, 4) AS report_year, -- 6. creating the report_year column and group results by it later
    SUM(average_daily_sales) AS total_amount
FROM s1
    JOIN Product USING (product_id)
GROUP BY product_id, LEFT(p_date, 4) -- 7. calculating for each product and year, the sum of daily_sales
ORDER BY product_id, report_year