-- 코드를 작성해주세요
with ECOLI_DATA_YEAR as (
    SELECT 
        ID, SIZE_OF_COLONY, YEAR(DIFFERENTIATION_DATE) as YEAR 
    FROM
        ECOLI_DATA 
),
max_size_of_colony as (
    SELECT 
        YEAR
        , MAX(SIZE_OF_COLONY) as max_size
    FROM
        ECOLI_DATA_YEAR
    GROUP BY
        YEAR
)

SELECT 
    M.YEAR
    , max_size-E.SIZE_OF_COLONY  as YEAR_DEV
    , ID
FROM 
    ECOLI_DATA_YEAR E JOIN max_size_of_colony M ON E.YEAR = M.YEAR
ORDER BY
    YEAR, YEAR_DEV
