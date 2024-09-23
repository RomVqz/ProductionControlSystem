import configparser
import os

def config(filename='database.ini', section='postgresql'):
    # Crear el parser y leer el archivo de configuración
    parser = configparser.ConfigParser()
    parser.read(filename)

    # Obtener la sección de la base de datos
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db
