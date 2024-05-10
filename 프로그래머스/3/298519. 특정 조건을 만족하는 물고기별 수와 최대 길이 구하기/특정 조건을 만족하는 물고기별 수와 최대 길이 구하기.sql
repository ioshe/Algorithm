-- 코드를 작성해주세요
with avg_length_fish_info as (
    select 
        FISH_TYPE
        ,AVG(LENGTH) as AVG_LENGTH
        # , AVG(LENGTH) OVER (PARTITION BY FISH_TYPE) as AVG_LENGTH
    FROM
        FISH_INFO
    GROUP BY FISH_TYPE
    HAVING  AVG(LENGTH) >= 33
)

SELECT
    COUNT(*) as FISH_COUNT
    , MAX(LENGTH) as MAX_LENGTH
    , FISH_TYPE
from
    FISH_INFO
WHERE
    FISH_TYPE IN (
    select 
        FISH_TYPE
    FROM
        avg_length_fish_info
)
GROUP BY
    FISH_TYPE
ORDER BY
    FISH_TYPE

