import os

def cambiar_nombres_en_carpeta(directorio):
    # Obtén la lista de archivos en el directorio
    archivos_png = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.png')]

    # Ordena la lista de archivos alfabéticamente
    archivos_png.sort()

    # Cambia el nombre de los archivos a números ascendentes
    for i, archivo in enumerate(archivos_png, start=1):
        nuevo_nombre = f"{i}.png"
        ruta_actual = os.path.join(directorio, archivo)
        nueva_ruta = os.path.join(directorio, nuevo_nombre)

        # Maneja la excepción si ya existe un archivo con el nuevo nombre
        while True:
            try:
                os.rename(ruta_actual, nueva_ruta)
                print(f"Renombrado: {archivo} -> {nuevo_nombre}")
                break
            except FileExistsError:
                # Si el archivo ya existe, agrega un sufijo al nuevo nombre
                i += 1
                nuevo_nombre = f"{i}.png"
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
