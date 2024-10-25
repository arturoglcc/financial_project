# Proyecto Web con Vue.js, Django y MySQL usando Docker

Este proyecto combina un frontend en Vue.js, un backend en Django y una base de datos MySQL, todos ejecutados y administrados mediante Docker.

## Requisitos Previos

    Docker: Asegúrate de tener Docker instalado. Puedes descargarlo desde Docker's download page.
    Docker Compose: Viene incluido con Docker Desktop.

## Estructura del Proyecto

    /docker: Contiene los archivos Dockerfile para construir las imágenes de la base de datos y el servidor HTTP.
    /script: Contiene un script para ejecutar y probar la aplicación.
    docker-compose.yml: Orquesta los servicios (base de datos, backend y frontend).
    /frontend y /backend: Directorios con el código fuente de Vue.js y Django, respectivamente.

## Guía de Uso

Este proyecto está diseñado para ejecutarse en un entorno local. Sigue estos pasos para configurarlo y probarlo:
### 1. Clona el Repositorio

``` bash

git clone https://github.com/arturoglcc/financial_project.git
cd financial_project
```
 
### 2. Usa el Script para Ejecutar la Aplicación

Para simplificar el proceso, puedes usar el script ubicado en el directorio /script. Este script construirá las imágenes de Docker y ejecutará los servicios necesarios.

``` bash

bash script/run.sh
```

### Este comando:

    Construye las imágenes de Docker necesarias para el frontend, backend y base de datos.
    Ejecuta los servicios de Docker Compose, levantando cada componente de la aplicación.

    Nota: El script run.sh asume que Docker y Docker Compose están instalados correctamente. Puedes verificar esto ejecutando docker --version y docker-compose --version.

### 3. Probar la Aplicación Localmente

## Una vez que la aplicación esté en funcionamiento, podrás acceder a los diferentes componentes de la siguiente manera:

    Frontend (Vue.js): Accede a http://localhost:8080 en tu navegador para ver la interfaz de usuario.
    Backend (Django): La API de Django estará disponible en http://localhost:8000.
    Base de Datos (MySQL): La base de datos estará disponible en el puerto 3306. Puedes conectarte a ella con herramientas de administración como MySQL Workbench usando las credenciales definidas en docker-compose.yml.

### 4. Apagar la Aplicación

Para detener todos los servicios y liberar los recursos, puedes ejecutar el siguiente comando:

```bash
docker-compose down
```

    Nota: Esto detendrá todos los contenedores, pero mantendrá los datos de la base de datos si usaste volúmenes persistentes.

Personalización del Script

Si necesitas ajustar el script para adaptarse a un entorno específico, abre el archivo run.sh en /script y revisa las siguientes secciones:

    Variables de entorno: Asegúrate de que las credenciales de MySQL y las configuraciones de red coincidan con las especificadas en docker-compose.yml.
    Comandos de Docker Compose: Si necesitas cambiar los puertos o configuraciones, puedes hacerlo en el archivo docker-compose.yml.

## Detalles Técnicos

    Persistencia de la Base de Datos: Los datos de MySQL se guardan en ./dbdata en tu máquina local para asegurar que la base de datos no se pierda entre reinicios.
    Archivos Estáticos de Vue.js: Los archivos del frontend se generan y sirven desde el backend (Django) para simplificar el despliegue.
    Orquestación de Servicios: Docker Compose maneja la comunicación y dependencias entre los contenedores de base de datos, backend y frontend.

## Solución de Problemas Comunes

    Error de Puertos en Uso: Si los puertos 8000, 8080 o 3306 están ocupados, cambia los puertos en docker-compose.yml y en el script run.sh.
    Problema de Conexión con MySQL: Verifica que las credenciales en docker-compose.yml y en run.sh sean correctas y que el contenedor db esté activo.
