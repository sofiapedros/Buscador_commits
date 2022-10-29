from git import Repo
import re 
import sys
import signal
import pprint

# Variables globales:
# Ruta del repositorio en el que se van a buscar commits
REPO_DIR = './skale-manager'

# Lista de palabras clave a buscar en los commits
KEY_WORDS = ['credentials', 'password', 'key', 'username', 'private']


def extract(repo_dir):
    '''
    Función que extrae todos los commits realizados en el repositorio
    '''
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def tranform(commits):
    '''
    Función que transforma los datos: busca los commits
    que contengan una palabra clave y los gurada en un diccionario
    '''
    # El diccionario empieza vacío
    diccionario = dict()
    
    # Por cada commit en el conjunto de commits
    for commit in commits:
        # Busca cada una de las palabras clave
        for word in KEY_WORDS:

            # Si la encuentra, añade al diccionario el "id"(versión en la que se hace) 
            # del commit y el mensaje que se hubiera introducido
            if re.search(word, commit.message, re.IGNORECASE):
                diccionario[commit.hexsha] =  commit.message
    return diccionario


def load(datos):
    '''
    Función para cargar los datos recopilados
    En este caso los resultados no se guardan
    y la solamente los imprime
    '''
    pprint.pprint(datos)
    pass



def handler_signal(signal, frame):
    '''
    Función que maneja la señal SIGINT (CTRL + C)
    '''
    # Imprime un mensaje y sale del programa
    print("\n\n[!] Out ............. \n")
    sys.exit(1)



if __name__ == '__main__':
    # Para que el main pueda registrar la señal SIGINT
    signal.signal(signal.SIGINT, handler_signal)

    # Extrae los commits
    commits = extract(REPO_DIR)

    # Los transforma para imprimirlos
    datos = tranform(commits)
    
    # Los imprime
    load(datos)
