# bentel-prueba
Bienvenidos a la Prueba Bentel. 

---------------------------------------------------------------------------------------------------------------------------------------------

Para optimizar el rendimiento de la aplicación, leí que existen las siguientes alternativas para DRF:

- Politicas de throttling: Se determina si la petición tiene autorización, lo cual aplica diferentes reglas para:
    - Limitar la cantidad de peticiones por día/hora/minuto.
    - Permitir el uso de la caché interna que provee Django según el tipo de usuario.

- Carga ansiosa(Eager Loading): Requerir toda la información que se requiere de la base de datos en una(o varias consultas) una sola vez y luego iterar, procesar, buscar, evitar hacer consultas dentro de ciclos. Esto se hace a través de consultas más astutas y el uso de prefetch.

- Limpieza de consultas: Retornar solo la información necesaria.

- Apagar la interfaz web para la API: al parecer luego de cierto tiempo de uso de la API esta puede generar un overhead innecesario.

Alternativas respecto a la bases de datos:

- Crear índices eficientes para la busqueda de registros.
- Crear vistas/particiones para acelerar ciertas consultas.

---------------------------------------------------------------------------------------------------------------------------------------------

¿Por qué se dice que las bases de datos relacionales escalan mal?

Existen varias razones, las principales y las que marcan la diferencia son las siguientes:

1) Escalabilidad HORIZONTAL. Bases de datos relacionales tienen una limitación importante que cuando las tablas/modelos crecen horizontalmente(al agregar campos) se reduce progresivamente las velocidades de lectura/escritura en las mismas, inclusive pueden ocurrir bloqueos durante la modificación de algún campo de la tabla, resultando en problemas de disponibilidad de la información, interbloqueos, tiempo de respuesta, entre otros.

2) Los grandes volúmenes de datos(Escalabilidad vertical). A pesar de que los promotores de BD relacionales aseguran que estas escalan verticalmente sin problemas, agrega cierta dificultad cuando implica implementar sharding(distribuir la información en varios servidores). Afecta de manera sustancial las consultas complejas que contienen joins o transacciones, una vez más afectando al rendimiento general de la base de datos.

Mi recomendación sería usar bases de datos relacionales cuando la aplicación requiera consultas complejas a través de varias tablas y que éstas no sobrepasen los 10M de registros. Lo ideal la mayoría de las veces es una combinación(un híbrido), una sinergia que beneficie el rendimiento de la aplicación aprovechando las bondades de cada uno de los paradigmas.

---------------------------------------------------------------------------------------------------------------------------------------------

Con respecto a qué métricas usar y qué servicios se pueden usar para ayudar a comprobar que la API y los servicios funcionan correctamente, la respuesta es compleja, porque lo que interpreto no es tan genérico como parece la pregunta:

- PRUEBAS UNITARIAS AUTOMATIZADAS. Si queremos comprobar que los endpoints retornan exactamente la información que se planificó. No sé que se usa para Python/Django, pero habría que buscar un framework para pruebas unitarias que permita hacer tantas pruebas necesarias e inclusive permita TDD(Test Driven Development) para algunos casos, en otras palabras que podamos diseñar funcionalidades precisas a partir de pruebas unitarias.

- DRF TRACKING. Si queremos registrar ciertos comportamientos(fallas, advertencias, delays) de la views de la API. Para no tener que revisar exhaustivamente los logs de apache/nginx/sys o tener que configurar un servicio aparte que permita recolectar los registros de los antes mencionados.

- DJANGO-ANALYTICAL. Permite una amplia gama de servicios de monitoreo en casi todos los aspectos que involucra una aplicación Web.

- HERRAMIENTAS DE PROFILING. Apache JMeter, SoapUI, ApacheBench, Vegeta.

- HERRAMIENTAS DESDE EL NAVEGADOR. Postman, REST Easy, REST Client. 

---------------------------------------------------------------------------------------------------------------------------------------------

Si te refieres a mi preferencia de IDE, he trabajado con varios. Actualmente uso mucho Atom(por los paquetes que son geniales) y VS Code(es molesto que no te permita abrir varios proyectos en la misma instancia) como principales, usé por mucho tiempo Sublime, pero me molestaba los problemas de inestabilidad que solía tener en aquel entonces. Con respecto a OS, me parece indistinto si uso Linux(prefiero distribuciones basadas en Debian) o Windows(actualmente estoy usando la versión 10 con todo lo que necesito para desarrollar).

