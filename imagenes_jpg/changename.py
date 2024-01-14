import os

def cambiar_nombres_en_carpeta(directorio):
    # Obtén la lista de archivos en el directorio
    archivos_jpg = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.jpg')]

    # Ordena la lista de archivos alfabéticamente
    archivos_jpg.sort()

    # Cambia el nombre de los archivos a números ascendentes
    for i, archivo in enumerate(archivos_jpg, start=1):
        nuevo_nombre = f"{i}.jpg"
        ruta_actual = os.path.join(directorio, archivo)
        nueva_ruta = os.path.join(directorio, nuevo_nombre)

        # Renombrar temporalmente el archivo
        temp_nombre = f"_{archivo}"
        temp_ruta = os.path.join(directorio, temp_nombre)

        os.rename(ruta_actual, temp_ruta)

        # Cambiar el nombre del archivo a la secuencia numérica
        while True:
            try:
                os.rename(temp_ruta, nueva_ruta)
                print(f"Renombrado: {archivo} -> {nuevo_nombre}")
                break
            except FileExistsError:
                # Si el archivo ya existe, agrega un sufijo al nuevo nombre
                i += 1
                nuevo_nombre = f"{i}.jpg"
                nueva_ruta = os.path.join(directorio, nuevo_nombre)

def cambiar_nombres_recursivamente(directorio_base):
    # Recorre todos los directorios y subdirectorios
    for directorio_actual, subdirectorios, archivos in os.walk(directorio_base):
        cambiar_nombres_en_carpeta(directorio_actual)

if __name__ == "__main__":
    # Obtén la ruta del directorio actual del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Aplica el cambio de nombres en todas las subcarpetas recursivamente
    cambiar_nombres_recursivamente(directorio_actual)
