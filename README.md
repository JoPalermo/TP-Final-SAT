# TP-Final-SAT
Alumno --> Palermo Joaquin 60194

Para llevar a cabo el EDA se utiliza una base de datos con la información pertinente a los trabajos publicados en la plataforma LinkdIn. El objetivo es analizar la oferta de empleo en el último año y el tipo de trabajo y perfiles que demandas las empresas en el último año.

Para empezar a entender el Data Set, me fijo que información contiene. Para esto hago una preview de las primeras 5 filas del Data Set. Si bien no me aporta mucha información, ya me puedo empezar a dar una idea de lo que contiene.
Luego, busco la cantidad de filas y columnas para dimensionar el Data Set.
- Cantidad de Filas: 123849
- Cantidad de Columnas: 28

Una vez que sé la cantidad de columnas, quiero ver que contiene cada columna, por lo que extraigo el título de cada una de estas columnas.
- Nombres de las Columnas:
    1. job_id
    2. company_name
    3. title
    4. description
    5. max_salary
    6. pay_period
    7. location
    8. company_id
    9. views
    10. med_salary
    11. min_salary
    12. formatted_work_type
    13. applies
    14. original_listed_time
    15. remote_allowed
    16. job_posting_url
    17. application_url
    18. application_type
    19. expiry
    20. closed_time
    21. formatted_experience_level
    22. skills_desc
    23. listed_time
    24. posting_domain
    25. sponsored
    26. work_type
    27. currency
    28. compensation_type

El paso siguiente es ver si la información que contiene cada columna tiene errores o si faltan datos.
Lo que hago es fijarse mi hay valores faltantes y en caso de que haya, los remplazo por la palabra "Unknown". Podemos ver que en las columnas en las que falta más información es en aquellas relacionadas con el salario ofrecido.

Otra 



