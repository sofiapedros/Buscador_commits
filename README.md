# Buscador_commits
En la carpeta 'buscador commits' se encuentran tres documentos: 
- git_leaks.py
- requirements.txt
- skale-manager

El último documento es un directorio que continen el repositorio de skale sobre el que se van a buscar los commits.

- git_leaks.py: al ejecutarse, imprime por pantalla una lista con los commits que contengan alguna de las palabras consideradas como 'sensibles' para buscar leaks ('private', 'key'...). Para ello, guarda todos los commits con alguna palabra clave en un diccionario cuya clave es el id del commit y cuyo valor es el mensaje correspondiente. Al final del programa, se imprimen los valores del diccionario con sus claves correspondientes

- requirements.txt: contiene todas las librerías usadas en el desarrollo del programa para que se puedan descargar con pip install -r requirements.txt
