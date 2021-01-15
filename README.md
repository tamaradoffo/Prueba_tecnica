# Prueba_tecnica_Nro 2
Esquema de configuración
Contenedores:
nginx: proporcionará el servicio web.
postgres: proporcionará el servicio de base de datos.
data: proporcionará servicios de respaldo.
django: proporcionara los servicios de la aplicación django.
Volúmenes:
django_static: contiene los archivos estáticos de nuestra aplicación django.
django_media: contiene los archivos subidos por los usuarios de nuestra aplicación django.
postgres: contiene la información de la base de datos.
Directorios compartidos en contenedores:
./nginx/conf: contiene las configuraciones del servidor web.
./postgres/initdb: contiene los archivos de inicialización de la base de datos
Directorios del Proyecto:
Project:
   -> app
        ->src
   -> ngnix
        ->conf
   -> postgres
        ->initbd
        
Comentarios:
version de sop: alpine 3.8
