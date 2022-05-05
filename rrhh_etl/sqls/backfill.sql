SELECT 
    year, period, inscription_date,  count(*) as inscriptions
FROM 
    inscriptions
{% if from_date or to_date%}
    WHERE 
        {% if from_date %}
            inscription_date>='{{from_date}}' {% if to_date %} AND {% endif %}
        {% endif %}
        {% if to_date %}
            inscription_date<='{{to_date}}'
        {% endif %}
{% endif %}
GROUP BY 1,2,3 
ORDER BY 1,2,3 ASC
