# Write your MySQL query statement below
select w1.Id
from Weather as w1
join Weather as w2
on w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature