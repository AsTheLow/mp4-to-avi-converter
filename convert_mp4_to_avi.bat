@echo off
setlocal enabledelayedexpansion

:: Vérifiez si FFmpeg est présent dans le même répertoire que le script
if not exist "ffmpeg.exe" (
    echo FFmpeg n'a pas été trouvé dans le répertoire actuel.
    echo Placez ffmpeg.exe dans le même répertoire que ce script.
    pause
    exit /b
)

:: Créez un répertoire de sortie s'il n'existe pas
if not exist output (
    mkdir output
)

:: Parcours tous les fichiers MP4 dans le répertoire actuel
for %%f in (*.mp4) do (
    set "input=%%~nf.mp4"
    set "output=output\%%~nf.avi"
    
    :: Conversion de MP4 en AVI
    ffmpeg -i "!input!" "!output!"
    
    echo Conversion de !input! en !output! terminée.
)

echo Conversion de tous les fichiers MP4 en AVI terminée.
pause
