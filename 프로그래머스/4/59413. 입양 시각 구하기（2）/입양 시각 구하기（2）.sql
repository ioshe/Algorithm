with recursive test as (
    select 0 as hour
    Union all
    select hour+1 from test where test.hour < 23)

SELECT 
    TEST.HOUR,
    COUNT(ANIMAL_ID) AS COUNT
FROM TEST
LEFT JOIN ANIMAL_OUTS 
ON TEST.HOUR = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR
ORDER BY HOUR