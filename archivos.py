import os

def gather_dart_files(directory, output_file):
    with open(output_file, 'w') as outfile:
        # Recorre el directorio y las subcarpetas
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Verifica que el archivo tenga extensión .dart
                if file.endswith('.dart'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        outfile.write(f"{file}\n")  # Escribe el nombre del archivo
                        outfile.write(infile.read())  # Escribe el contenido del archivo
                        outfile.write("\n\n")  # Salto de línea entre archivos

if __name__ == "__main__":
    # Cambia 'your_directory_path' por el directorio donde están los archivos .dart
    directory = r'C:\Users\dvere\Documents\Python Scripts\new project\flutter app\flutter_app\lib'
    output_file = 'dart_files_code.txt'
    
    gather_dart_files(directory, output_file)
    print(f"El contenido de los archivos .dart ha sido guardado en {output_file}")
