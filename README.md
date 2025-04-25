Azure OCR Lab

Este repositorio contiene diferentes componentes de pruebas que implementan diversos servicios de Azure AI. Cada componente está orientado a un laboratorio diferente que utiliza distintas tecnologías de Azure AI.
Requisitos

Asegúrate de tener las siguientes herramientas instaladas en tu entorno:

    Python 3.x

    Paquete requests: Para realizar solicitudes HTTP.

    Paquete python-dotenv: Para cargar las variables de entorno desde el archivo .env.

Instalación de dependencias
Clonar el repositorio:

    git clone <URL_DEL_REPOSITORIO>
    cd <nombre_del_repositorio>



Instalar las dependencias:

    pip install -r requirements.txt

Configuración de variables de entorno

Antes de ejecutar cualquier componente, debes configurar las variables de entorno. 
Crea un archivo .env en la raíz del proyecto con las siguientes variables:

    AZURE_ENDPOINT=tu_endpoint_de_azure
    AZURE_KEY=tu_clave_de_azure

AZURE_ENDPOINT: El endpoint de la API de Azure correspondiente al servicio que estás utilizando.

AZURE_KEY: La clave de suscripción de tu servicio de Azure correspondiente.


Ejecución de los Laboratorios

Para ejecutar cualquier componente, simplemente usa el siguiente formato en la terminal:

    python <nombre_del_componente>.py
