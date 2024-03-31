# Write your MySQL query statement below
with a as (
    select 
        student_id
        , subject_name
        , count(*) as attended_exams
    from
        Examinations
    group by
        student_id,subject_name
)

select 
    st.student_id
    , st.student_name
    , su.subject_name
    , IFNULL(attended_exams,0) as attended_exams 
from Students as st JOIN Subjects as su
left JOIN a
ON
    st.student_id = a.student_id 
    and su.subject_name = a.subject_name
order by
    st.student_id, su.subject_name