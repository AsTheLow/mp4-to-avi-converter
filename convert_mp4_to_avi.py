import os
import subprocess

# Vérifiez si FFmpeg est présent dans le même répertoire que le script
if not os.path.exists("ffmpeg.exe"):
    print("FFmpeg n'a pas été trouvé dans le répertoire actuel.")
    print("Placez ffmpeg.exe dans le même répertoire que ce script.")
    exit(1)

# Créez un répertoire de sortie s'il n'existe pas
if not os.path.exists("output"):
    os.mkdir("output")

# Parcours tous les fichiers MP4 dans le répertoire actuel
for filename in os.listdir("."):
    if filename.endswith(".mp4"):
        input_file = filename
        output_file = os.path.join("output", os.path.splitext(filename)[0] + ".avi")

        # Conversion de MP4 en AVI en utilisant FFmpeg
        command = ["ffmpeg", "-i", input_file, output_file]
        subprocess.run(command)

        print(f"Conversion de {input_file} en {output_file} terminée.")

print("Conversion de tous les fichiers MP4 en AVI terminée.")
