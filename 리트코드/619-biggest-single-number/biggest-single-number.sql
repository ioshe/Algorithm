select case when count(*) = 1 then max(num) else null end as num
from MyNumbers
group by num
order by num desc 
LIMIT 1