WITH RepeatedTIVs AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(pid) > 1
),
UniqueLocations AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(pid) = 1
),
ValidPolicies AS (
    SELECT i.pid, i.tiv_2016
    FROM Insurance i
    JOIN RepeatedTIVs rt ON i.tiv_2015 = rt.tiv_2015
    JOIN UniqueLocations ul ON i.lat = ul.lat AND i.lon = ul.lon
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM ValidPolicies;