SELECT 
    year, period, inscription_date,  count(*) as inscriptions
FROM 
    inscriptions
{% if from_year or to_date%}
    WHERE 
        {% if from_year %}
            year>={{from_year}} {% if to_date %} AND {% endif %}
        {% endif %}
        {% if to_date %}
            inscription_date<='{{to_date}}'
        {% endif %}
{% endif %}
GROUP BY 1,2,3 
ORDER BY 1,2,3 ASC
