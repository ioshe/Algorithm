-- 코드를 작성해주세요

SELECT 
    count(*) as FISH_COUNT
FROM
    FISH_INFO
WHERE
    IFNULL(LENGTH,0) <= 10
    