# Write your MySQL query statement below
select 
    actor_id,
    director_id
from
    ActorDirector 
group by 
    actor_id,director_id
HAVING
    count(director_id) >= 3