with recursive test as (
    select 0 as hour
    UNION ALL
    select hour+1 from test where test.hour < 23
)

SELECT 
    test.hour                    AS HOUR, 
    COUNT(ANIMAL_OUTS.ANIMAL_ID) AS COUNT 
FROM test
LEFT JOIN ANIMAL_OUTS
ON test.hour = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY test.hour
ORDER BY HOUR