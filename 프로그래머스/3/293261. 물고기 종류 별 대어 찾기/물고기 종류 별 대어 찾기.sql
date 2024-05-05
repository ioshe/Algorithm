SELECT 
    ID
    , FN.FISH_NAME
    , LENGTH
FROM
    FISH_INFO FI JOIN FISH_NAME_INFO FN ON FI.FISH_TYPE = FN.FISH_TYPE
WHERE 
    (FI.FISH_TYPE, FI.LENGTH) IN (
           select fish_type, max(length) 
           from fish_info
           group by fish_type
)
ORDER BY
    ID