# RECONOCIMIENTO DE PLACAS VEHICULARES CON IA

Proyecto de clasificación que detecta y lee placas vehiculares en tiempo real

## Requisitos previos
* **Python 3.12 o superior**
* **Extensiones recomendadas para VS Code:
   * `Python`
   * `Pylance`
* Camara Web o un video mp4

## Instalacion y ejecucion 
1. **Clonar o descargar el repositorio** y abrir en VSC
2. **Crear y activar el entorno** desde la terminal:
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
````
**NOTITA:** Si se bloque al ejecutar prueba:
* `Set_ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Procees`

## PROFUNDIZANDO PROCESO
* **1.Instalar las dependencias**
  * `python -m pip install "setuptools<70.0.0" wheel`
  * `python -m pip install -r requerimientos.txt`
* **2.Ejecutar programa**
  * `python main.py`
Presiona la tecla Q para detener la ejecucion :D y guardar resultados en text.csv
Antees de ejecutar el git push:
* **Crea un archivo `.gitignore`:** Si subes la carpeta `venv` a GitHub, la subida tardará mucho o fallará por el tamaño de PyTorch y OpenCV.
* **Crea un archivo llamado `.gitignore` en la raíz de tu proyecto y escribe dentro simplemente:**
  ```text
  venv/
  __pycache__/
  *.csv
  ```
# Creditos y derechos de autor:
Este proyecto esta basado en el repositorio original de **Bryan de Jesús (`bryandejesusrt`), adaptado para la deteccion y reconocimiento en tiempo real de placas
vehiculares:
* Repositorio base: [Reconocimiento-de-placas-con-IA-Bytecoders](https://github.com/bryandejesusrt/Reconocimiento-de-placas-con-IA-Bytecoders)
