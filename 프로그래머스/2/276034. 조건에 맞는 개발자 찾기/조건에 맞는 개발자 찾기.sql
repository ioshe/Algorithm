-- 코드를 작성해주세요
select 
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
from
    DEVELOPERS
where
    SKILL_CODE & (select CODE FROM SKILLCODES WHERE NAME="Python") or
    SKILL_CODE & (select CODE FROM SKILLCODES WHERE NAME="C#")
ORDER BY
    ID