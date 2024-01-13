import os

def cambiar_nombres():
    # Obtén la ruta del directorio actual del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Obtén la lista de archivos en el directorio actual
    archivos_png = [archivo for archivo in os.listdir(directorio_actual) if archivo.lower().endswith('.png')]

    # Ordena la lista de archivos alfabéticamente
    archivos_png.sort()

    # Cambia el nombre de los archivos a números ascendentes
    for i, archivo in enumerate(archivos_png, start=1):
        nuevo_nombre = f"{i}.png"
        ruta_actual = os.path.join(directorio_actual, archivo)
        nueva_ruta = os.path.join(directorio_actual, nuevo_nombre)

        # Cambia el nombre del archivo
        os.rename(ruta_actual, nueva_ruta)
        print(f"Renombrado: {archivo} -> {nuevo_nombre}")

if __name__ == "__main__":
    cambiar_nombres()
