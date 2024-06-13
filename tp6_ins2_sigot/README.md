Extractor de token para acceso API Servicios Banco XXX (versión 1.0)

Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operará como un microservicio invocado mediante:

        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

ej.
        ./getJason.pyc ./sitedata.json

El token podrá recuperarse mediante el standard output de ejecución en el formato

       {1.0}XXXX-XXXX-XXXX-XXXX

Para obtener un mensaje de ayuda detallado ejecutar

       ./getJason.pyc -h

Excepciones

Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
terminar.
<!-- --------------------------------------------------------------- -->

Documentacion Recuperada


Paso 1 Colección de datos

Código fuente y librerías (nivel de dependencia)

Código Fuente:
Python: getJason.pyc, getJason-3.7.pyc, getJason-3.6.pyc y getJason-2.7.pyc tienen lógica de negocio para extraer la clave de acceso API para utilizar los servicios del Banco XXX en distintas versiones de Python.

Scripts y otro material relevante para la ejecución.

Scripts:
Shell Scripts: compile.sh se usa para automatizar tareas repetitivas, en este caso, la compilación del código fuente.
Material relevante para la ejecución:
Datos de prueba: sitedata.json contiene datos necesarios para recuperar los tokens.

Documentación de uso, frecuencia transaccional.

Documentación Técnica:
README.md tiene detalles de como operar con el programa.

Valor relativo para el negocio de cada componente (cantidad de ejecuciones).

Componentes Críticos:
getJason-3.7.pyc y getJason-3.6.pyc se asegura de la compatibilidad del código con versiones 3.7 y 3.6 del intérprete de Python, permite extraer  la clave de acceso API por lo cual es crucial para el negocio. 
compile.sh es crucial durante el proceso de desarrollo, especialmente en equipos donde se requiere la compilación frecuente del código. Automatiza y estandariza la compilación, reduciendo errores y ahorrando tiempo.
sitedata.json contiene datos necesarios para recuperar los tokens.

Componentes de Bajo Uso:
getJason-2.7.pyc Python 2.7 está obsoleto y la clase no tiene conexión con otras clases. 


Paso 2 Extraer información 

Inventario de objetos disponibles:
Ejecutables/Binarios:
compile.sh
Configuraciones:
sitedata.json
Código fuente:
getJason-3.7.pyc  
getJason-3.6.pyc
getJason-2.7.pyc 
getJason.pyc

Métricas (ej. multimetric).
La proporción de comentarios es 0.0 ya que no existen código en el programa.

Algo parecido pasa con la complejidad del código ya que no contamos con el código y nos da un porcentaje bajo.

Faltantes o excedentes.
Faltantes: 
Falta el código fuente de cada clase.

Documentación disponible.
El archivo README.md tiene contenido de los comandos a ejecutar para que funcione el programa:
{path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json
./getJason.pyc ./sitedata.json token1
./getJason.pyc -h

Discrepancias identificadas.
El comando ./getJason.pyc -h usado para obtener un mensaje de ayuda no funciona.
No conocemos el código fuente de los archivos getJason.pyc, getJason-2.7.pyc, getJason-3.7.pyc y getJason-3.6.pyc.

Resultados de ejecución.
Al ejecutar una versión del código compatible obtenemos el siguiente resultado:
(devuelve la clave API)
Pero cuando se ejecuta una versión la cual no es compatible nos da este resultado:
(mensaje de error)

Paso 3 Extraer estructura
compile.sh
Principales “nodos” de procesamiento y fuentes de complejidad:
La única operación significativa en el script es la ejecución del comando python -m compileall $1, que compila todos los archivos Python en el directorio especificado.

sitedata.json
Variables: 
token1  
token2.
Estructuras de datos clave-valor: 
"token1": "C598-ECF9-F0F7-881A"
"token2": "C598-ECF9-F0F7-881B"
Principales “nodos” de procesamiento y fuentes de complejidad:
El uso de estos tokens en la aplicación puede ser una fuente de complejidad.

El resto de clases no presentan código para realizar el paso 3.

Paso 4 Registra funcionalidad 
La imagen del Diagrama de flujo se encuentra en el pdf adjuntado

Paso 5 Registra flujo de datos
La imagen del Diagrama de secuencia se encuentra en el pdf adjuntado




