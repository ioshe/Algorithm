-- 코드를 입력하세요
SELECT
    ANIMAL_ID
    , NAME
    , SEX_UPON_INTAKE
from
    ANIMAL_INS
WHERE
    NAME = "Lucy"
    OR NAME = "Ella"
    OR NAME = "Pickle"
    OR NAME = "Rogan"
    OR NAME = "Sabrina"
    OR NAME = "Mitty"
ORDER BY 
    ANIMAL_ID