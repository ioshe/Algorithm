# Write your MySQL query statement below
select 
    id,
    CASE 
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN t.id IN (select DISTINCT p_id from Tree WHERE p_id IS NOT NULL )  THEN 'Inner'
        ELSE 'Leaf'
    END as type
from
    Tree t
