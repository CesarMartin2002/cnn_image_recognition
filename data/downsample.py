from PIL import Image
import os

def reduce_resolution(input_path, output_path, factor):
    image = Image.open(input_path)
    width, height = image.size
    new_width = width // factor
    new_height = height // factor
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    resized_image.save(output_path, quality=75)

def process_images(input_folder, output_folder, factor):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.png'):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_folder)
                print("-----")
                print(input_path)
                print("-----")
                output_path = os.path.join(output_folder, relative_path[:-4] + '.jpg')

                # Crear la carpeta de salida si no existe
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                reduce_resolution(input_path, output_path, factor)

if __name__ == "__main__":
    input_folder = ".\imagenes_convertidas"
    output_folder = ".\imagenes_jpg"
    reduction_factor = 4

    process_images(input_folder, output_folder, reduction_factor)

    print("Proceso completado.")
