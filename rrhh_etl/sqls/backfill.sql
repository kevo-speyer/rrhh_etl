SELECT 
    year, period, inscription_date,  count(*) as inscriptions
FROM 
    inscriptions
WHERE 
    year>=2019 AND inscription_date<'2021-05-03'
GROUP BY 1,2,3 
ORDER BY 1,2,3 ASC
