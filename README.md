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
Lo que hago es fijarse mi hay valores faltantes y en caso de que haya, los remplazo por la palabra "Unknown". 

Podemos ver que en las columnas en las que falta más información es en aquellas relacionadas con el salario ofrecido.

También obtenemos los estadísticos principales del Data Set. Podemos obtener por ejemplo el valor que más se repite en cada una de las columnas, o el salario promedio ofrecido.

Otra información importante es que al ver la cantidad de valores únicos que tienen las columnas, la columna que se llama "job_id" tiene la misma cantidad de valores únicos que la cantidad de filas de la columna. Esto quiere decir que están bien numerados los "id" de los trabajos, porque no se deberían repetir estos códigos de referencia.

Una vez ordenado el Data Set base, le vamos a sumar información proveniente de otros Data Sets utilizando el "id" del trabajo ofrecido para linkear la información. Le sumamos información como los beneficios extra del puesto de trabajo, datos adicionales de la empresa que ofrece el trabajo y las habilidades necesarias para postularse al puesto.

Una vez agregada la información proveniente de los otros Data Sets, nos queda una tabla con 42 columnas, de las cuales muchas nos traen información poco útil. Por esto es que se eliminan varias de estas columnas, quedando finalmente tan solo 13 columnas.

-------------------------------------------------------------------

Información de interes:

1. Cual es el trabajo que mas se ofrecio?

Como podemos observar el la foto "Pregunta 1", el top de trabajos mas ofrecidos son:
 - Regisered Nurse.
 - Project Manager.
 - Director.
 - Lead.
 - Sales Associate.
 - Customer Service.

2. Que tipo de trabajo es mas comun encontrar publicado?

Como podemos observar en el grafico "Pregunta 2_a", el prabajo que mas se ofrece es en la modalidad de Full Time alcanzando un valor de casi 100.000 puestos ofrecidos.
Para que los valores sean un poco mas claros, se usa el grafico "Pregunta 2_b" donde se puede ver el porcentaje de participacion sobre el total de cada tipo de trabajo. Los resultados son:
 - Full-time     79.78%
 - Contract       9.78%
 - Part-time      7.82%
 - Temporary      0.96%
 - Internship     0.79%
 - Volunteer      0.45%
 - Other          0.39%

Podemos ver que la diferencia es bastante grande entre los puestos "Full Time" (79.78%) y el resto de peustos.

3. 
