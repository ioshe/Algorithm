-- 코드를 입력하세요
with recursive time as (
    select 0 as hour
    union all
    select hour+1 from time where hour<23
)

SELECT 
      time.hour  AS HOUR
    , COUNT(animal_id) AS COUNT
FROM time 
LEFT JOIN ANIMAL_OUTS 
ON time.hour = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR
ORDER BY HOUR