-- 코드를 작성해주세요
with avg_hr_grade as (
    select 
        EMP_NO
        , avg(SCORE) AVG_SCORE
    from
        HR_GRADE
    GROUP BY
        EMP_NO
), merge_avg_hr_grade as (
    select 
        ah.EMP_NO, EMP_NAME, SAL
    from
        HR_EMPLOYEES HR JOIN avg_hr_grade ah
    ON HR.EMP_NO = ah.EMP_NO
), grade_bonus as (
    select
        ma.EMP_NO
        , ma.EMP_NAME
        , 
        CASE 
            WHEN a.AVG_SCORE >= 96 THEN "S" 
            WHEN a.AVG_SCORE >= 90 THEN "A"
            WHEN a.AVG_SCORE >= 80 THEN "B"
            ELSE "C"
        END as GRADE
        , 
        CASE 
            WHEN a.AVG_SCORE >= 96 THEN ma.SAL * 0.2
            WHEN a.AVG_SCORE >= 90 THEN ma.SAL * 0.15
            WHEN a.AVG_SCORE >= 80 THEN ma.SAL * 0.1
            ELSE 0
        END as BONUS
    FROM
        avg_hr_grade as a JOIN merge_avg_hr_grade ma
    ON a.EMP_NO = ma.EMP_NO
    ORDER BY
        EMP_NO
)
select 
    *
from
    grade_bonus