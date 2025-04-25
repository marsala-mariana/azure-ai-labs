import os
import requests
from dotenv import load_dotenv
import base64


load_dotenv()
endpoint = os.getenv("AZURE_ENDPOINT")  
api_key = os.getenv("AZURE_KEY")  



# Función para analizar texto con la API de Azure Content Safety
def analyze_text(text):
    # URL del endpoint para el análisis de texto
    url = f"{endpoint}/contentsafety/text:analyze?api-version=2023-10-01"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,  # Autenticación mediante la clave API
        "Content-Type": "application/json"  # Especificar que el contenido es JSON
    }
    # El texto que queremos analizar
    payload = { "text": text }

    # Realizar la solicitud POST a la API de Azure
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        # Si la respuesta no es 200 (OK), mostramos un mensaje de error
        print(f"⚠️ Error en la solicitud de texto: {response.status_code}")
        print(response.text)  # Mostrar detalles del error
        return None
    # Retornar el resultado en formato JSON
    return response.json()

# Función para procesar el resultado del análisis de texto
def process_text_result(result):
    if not result:
        print("❌ No se recibió resultado del análisis de texto.")  # Si no hubo resultado, mostrar un mensaje
        return

    print("🔍 Resultado del análisis de texto:")
    # Iterar sobre las categorías de análisis recibidas
    for item in result.get("categoriesAnalysis", []):
        category = item.get("category")  # Obtener la categoría del análisis
        severity = item.get("severity")  # Obtener la severidad del contenido encontrado
        if severity > 0:  # Solo mostrar si la severidad es mayor que 0 (contenido inapropiado)
            print(f" - ⚠️ Categoría: {category}, Severidad: {severity}")
    print("✅ Análisis de texto completado.")

# Función para analizar una imagen, que la convierte a base64 y la envía a la API
def analyze_image(image_path):
    # URL del endpoint para el análisis de imagen
    url = f"{endpoint}/contentsafety/image:analyze?api-version=2023-10-01"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,  # Autenticación mediante la clave API
        "Content-Type": "application/json"  # Especificar que el contenido es JSON
    }

    try:
        # Intentar abrir la imagen en modo binario ('rb') y leer su contenido
        with open(image_path, "rb") as f:
            image_data = f.read()
            # Convertir la imagen leída a base64
            image_base64 = base64.b64encode(image_data).decode("utf-8")
    except FileNotFoundError:
        # Si no se encuentra la imagen, mostrar un mensaje de error
        print(f"❌ Imagen no encontrada: {image_path}")
        return None

    # Preparar el cuerpo de la solicitud con la imagen en base64
    payload = {
        "image": {
            "content": image_base64
        }
    }

    # Realizar la solicitud POST a la API de Azure
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        # Si la respuesta no es 200 (OK), mostramos un mensaje de error
        print(f"⚠️ Error en la solicitud de imagen: {response.status_code}")
        print(response.text)  # Mostrar detalles del error
        return None
    # Retornar el resultado del análisis en formato JSON
    return response.json()

# Función para procesar el resultado del análisis de la imagen
def process_image_result(result, image_path):
    if not result:
        print(f"❌ No se recibió resultado para la imagen {image_path}.")  # Si no hay resultado, mostrar error
        return

    print(f"🔍 Resultado del análisis de imagen: {image_path}")
    # Iterar sobre las categorías de análisis recibidas para la imagen
    for item in result.get("categoriesAnalysis", []):
        category = item.get("category")  # Obtener la categoría del análisis
        severity = item.get("severity")  # Obtener la severidad del contenido encontrado
        if severity > 0:  # Solo mostrar si la severidad es mayor que 0 (contenido inapropiado)
            print(f" - ⚠️ Categoría: {category}, Severidad: {severity}")
    print(f"✅ Imagen '{image_path}' analizada.")

# ------------------------- Ejecución -------------------------

# Ejemplo de análisis de texto
texto = "Este es un texto de prueba con referencias a drogas o violencia."
print("🔍 Analizando texto...")
# Llamar a la función para analizar el texto
text_result = analyze_text(texto)
# Procesar el resultado del análisis de texto
process_text_result(text_result)

# Ejemplo de análisis de imágenes desde la carpeta 'visual'
image_files = ["img1.jpg", "img2.jpeg", "img3.jpg", "img4.jpeg"]
for img in image_files:
    # Para cada imagen, obtener la ruta completa en el directorio 'visual'
    path = os.path.join("visual", img)
    print(f"\n🔍 Analizando imagen: {img}")
    # Llamar a la función para analizar la imagen
    image_result = analyze_image(path)
    # Procesar el resultado del análisis de imagen
    process_image_result(image_result, img)
