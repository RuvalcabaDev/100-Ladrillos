# Backend project 100 Ladrillos
Propuesta de solución técnica al proyecto backend de 100 Ladrillos.

## _Información general_
Stack de tecnologías a implementar en esta solución.
- Lenguaje de programación python 3.8.10+ 
- Libreía pymysql para conexiones MySQL
- FastApi
- uvicorn
- Librería pydantic
- ORM pewee

## _Solución técnica_
Se realiza el desarrollo backend basado en historias técnicas.

Se hace un análisis de los requerimientos con los cuales, se crea un diagrama de entidad relación para la base de datos.

Se realizará el desarrollo implementando Test-Driven Development, por lo cual, se escriben los casos de prueba para validar los criterios de aceptación de todas las HU.

Se despliega la base de datos en un ambiente de desarrollo (servidor pequeño).
Esto, con el fin de facilitar el acceso a los datos.

## _Instalación del proyecto_
Pasos a seguir para poder correr el proyecto backend.
Se requiere tener instalado python3 +

En caso de usar sistemas basados en windows, se debe reemplazar "pip3" por "pip" de python. 

- Descargar el repositorio
- Configurar variables de entorno (conexión a base de datos).
- Instalar la librería FastApi
```sh
pip3 install fastapi
```
- Instalar el servidor uvicorn
```sh
pip3 install uvicorn
```
- Instalar la librería pymysql
```sh
pip3 install pymysql
```
- Instalar la librería pydantic
```sh
pip3 install pydantic
```
- Instalar el ORM pewee
```sh
pip3 install peewee
```

¡Listo! Todo debería funcionar.

También puede las dependencias con el archivo requirements.txt
```sh
pip3 install -r requirements.txt
```
