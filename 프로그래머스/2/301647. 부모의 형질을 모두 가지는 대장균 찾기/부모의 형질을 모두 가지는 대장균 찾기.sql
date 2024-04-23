-- 코드를 작성해주세요
select 
    child.ID
    , child.GENOTYPE
    , parent.GENOTYPE as PARENT_GENOTYPE
FROM
    ECOLI_DATA as child LEFT JOIN ECOLI_DATA as parent
ON
    child.PARENT_ID = parent.ID
WHERE
    child.GENOTYPE & parent.GENOTYPE = parent.GENOTYPE
ORDER BY
    ID