# Aplicación Web de Adopción de Mascotas  

Proyecto en el que se desarrolla una pagina web que realiza la gestion del proceso de adopcion, incluyendo la recepción de información de perros o gatos en adopción, ofrecer listados de todos los animales que están en adopción y ver la información detallada de una publicación de adopción. 

## Tecnologías utilizadas
- **Backend**: Python, Flask, MySQL con SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript

## Iniciar aplicacion

### Intalacion requerida 

Para ejecutar la aplicación se necesita tener instalado el framework Flask y las distintas bibliotecas utilizadas en este proyecto, para esto dentro del directorio flask_app ejecute lo
siguiente en una terminal, se aconseja primero crear un ambiente virtual.

```bash
pip install -r requirements.txt
```
### Ejecutar aplicacion

Si es la primera vez que inicia la aplicación debe correr la base de datos, para esto debe ejecutar los siguientes archivos:
```
flask_app
└── database
    ├── create-user.sql
    ├── region-comuna.sql
    └── tarea2.sql
```

Finalmente puede ejecutar la aplicacion con:

```bash
flask run
```
Esto iniciara la aplicación localmente y para ingresar diríjase a la dirección indicada en la terminal para ver la aplicación web en funcionamiento.

Para salir del servidor presione `CTRL + C` en la terminal.
