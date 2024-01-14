import os
from PIL import Image
from pillow_heif import register_heif_opener

class HeicToPngConverter:
    def __init__(self) -> None:
        register_heif_opener()
        
        self.input_folder = os.path.dirname(os.path.abspath(__file__))
        self.output_folder = os.path.join(self.input_folder, 'imagenes_convertidas')

        self.convert_files()

    def convert_files(self):
        # Crear la carpeta de salida si no existe
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        heic_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.heic')]

        for heic_file in heic_files:
            heic_path = os.path.join(self.input_folder, heic_file)

            with Image.open(heic_path) as heic_image:
                # Cambiar la extensión del archivo de .heic a .png
                png_file = os.path.splitext(heic_file)[0] + '.png'
                png_path = os.path.join(self.output_folder, png_file)

                # Guardar la imagen como .png
                heic_image.save(png_path, format='PNG')
                print(f"Convertido {heic_file} a {png_file}")

        print("Todas las imágenes .HEIC han sido convertidas a .png en ./imagenes_convertidas")


if __name__ == "__main__":
    heic_to_png_converter = HeicToPngConverter()
