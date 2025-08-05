-- Last updated: 8/5/2025, 2:53:01 PM
# Write your MySQL query statement below
select tweet_id from Tweets where char_length(content)>15;