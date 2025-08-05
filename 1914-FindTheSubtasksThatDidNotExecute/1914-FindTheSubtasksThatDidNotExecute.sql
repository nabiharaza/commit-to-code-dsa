-- Last updated: 8/5/2025, 2:52:47 PM
# Write your MySQL query statement below
with recursive cte as (
    select task_id, subtasks_count
    from tasks
    union
    select task_id, subtasks_count - 1 from cte
    where subtasks_count > 1)

select
    task_id,
    subtasks_count AS subtask_id 
from 
    cte
where
    (task_id, subtasks_count) not in
    (select
        *
    from
        executed)
order by 
    task_id, subtasks_count