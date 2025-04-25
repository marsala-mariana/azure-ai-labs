azure-ai-labs# Azure OCR Lab
Este repositorio está diseñado para ejecutar pruebas y laboratorios con el servicio OCR de Azure. El objetivo es enviar un archivo PDF local a la API de Azure y obtener el texto extraído del mismo.

Requisitos
Asegúrate de tener las siguientes herramientas y dependencias instaladas en tu entorno de desarrollo:

Python 3.x
Paquete requests (para realizar solicitudes HTTP)
Paquete python-dotenv (para cargar las variables de entorno desde el archivo .env)
Pasos para usar el repositorio
1. Clonar el repositorio
Clona el repositorio a tu máquina local:

git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_repositorio>

### 2. Instalar las dependencias

Instala las dependencias necesarias utilizando pip:
pip install -r requirements.txt

### 3. Crear el archivo .env
En la raíz del proyecto, crea un archivo .env y agrega las siguientes variables de entorno:
AZURE_ENDPOINT=tu_endpoint_de_azure
AZURE_KEY=tu_clave_de_azure

AZURE_ENDPOINT: El endpoint de la API de Azure OCR.
AZURE_KEY: La clave de suscripción de tu servicio de Azure OCR.

### 4. Crear el archivo .env
Ejecutar el script
Una vez que hayas configurado todo, ejecuta el script Python:
python ocr_script.py

### 5. Ver los resultados
El script enviará el archivo PDF a Azure OCR, procesará los resultados y mostrará el texto detectado en la consola.

### 6. ¿Qué hacer si algo no funciona?
Asegúrate de que las claves de Azure y el endpoint estén configurados correctamente en el archivo .env.
Verifica que el archivo PDF esté correctamente colocado y sea accesible por el script.
Si recibes un error, revisa el código de estado de la respuesta para obtener más detalles sobre lo que puede estar fallando.
