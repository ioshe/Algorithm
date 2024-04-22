-- 코드를 작성해주세요
with percent_rank_size as(
    select 
        ID
        ,PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS COLONY_NAME
    FROM
        ECOLI_DATA
) 

select 
    ID,
    CASE 
        WHEN COLONY_NAME <= 0.25 THEN "CRITICAL"
        WHEN COLONY_NAME <= 0.50 THEN "HIGH"
        WHEN COLONY_NAME <= 0.75 THEN "MEDIUM"
        ELSE "LOW"
    END COLONY_NAME
FROM
    percent_rank_size
ORDER BY 
    ID