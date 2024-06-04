-- 코드를 작성해주세요
with RECURSIVE a as (
    select ID,PARENT_ID, 1 AS n
    from ECOLI_DATA
    where PARENT_ID IS NULL
    
    UNION ALL
    SELECT ECOLI_DATA.ID,ECOLI_DATA.PARENT_ID,a.n + 1
    FROM ECOLI_DATA 
    JOIN a ON a.ID = ECOLI_DATA.PARENT_ID
)

select ID from a
where n = 3