-- 코드를 입력하세요
SELECT
    AI.ANIMAL_ID,
    AI.ANIMAL_TYPE,
    AI.NAME
FROM
    ANIMAL_INS AS AI
JOIN
    ANIMAL_OUTS AS AO
ON 
    AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE 
-- 보호소에 들어올 당시에는 중성화1되지 않았지만,
--  보호소를 나갈 당시에는 중성화된 동물
    AI.SEX_UPON_INTAKE LIKE "Intact%"
    AND (AO.SEX_UPON_OUTCOME LIKE "Spayed%" 
         OR AO.SEX_UPON_OUTCOME LIKE "Neutered%")
ORDER BY
    ANIMAL_ID