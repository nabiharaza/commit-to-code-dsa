-- Last updated: 8/5/2025, 2:54:22 PM
select
    distinct page_id as recommended_page
from
    (select
        case
            when user1_id=1 then user2_id
            when user2_id=1 then user1_id
        end as user_id
        from Friendship) f
join 
    Likes l
on 
    f.user_id = l.user_id
where 
    page_id not in 
    (select 
        page_id 
    from 
        Likes 
    where 
        user_id = 1)