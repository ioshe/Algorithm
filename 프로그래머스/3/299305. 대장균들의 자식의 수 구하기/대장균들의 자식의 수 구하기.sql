-- 코드를 작성해주세요
select 
    E1.ID
    , count(E2.PARENT_ID) as CHILD_COUNT
from
    ECOLI_DATA E1 LEFT JOIN ECOLI_DATA E2 ON E1.ID = E2.PARENT_ID
GROUP BY 
    E1.ID
ORDER BY 
    E1.ID