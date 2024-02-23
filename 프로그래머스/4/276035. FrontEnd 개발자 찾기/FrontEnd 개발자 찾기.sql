-- 코드를 작성해주세요

-- Front End 스킬을 가진 개발자의 정보를 조회
SELECT 
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS 
WHERE
    SKILL_CODE & ( SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = "Front End")
ORDER BY
    ID