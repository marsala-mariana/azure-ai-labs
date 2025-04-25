import os
import time
import requests
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
api_key = os.getenv("AZURE_KEY")

# Leer archivo PDF local
file_path = "dummy.pdf"

# Endpoint para archivos binarios
analyze_url = f"{endpoint}/vision/v3.2/read/analyze"

headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/octet-stream"
}

# Enviar archivo a Azure OCR
with open(file_path, "rb") as f:
    data = f.read()

print("📤 Enviando archivo local a Azure OCR...")
response = requests.post(analyze_url, headers=headers, data=data)
if response.status_code != 202:
    print("⚠️ Error en la solicitud:")
    print(response.status_code)
    print(response.text)  # Esto nos dirá qué espera Azure
    response.raise_for_status()

# Obtener la URL para la operación
operation_url = response.headers["Operation-Location"]
print(f"⏳ Esperando resultados desde: {operation_url}")

# Función para consultar los resultados
def get_analysis_result():
    response = requests.get(operation_url, headers=headers)
    result = response.json()

    if "analyzeResult" in result:
        return result  # Si ya está listo, devolvemos el resultado
    return None  # Si no está listo aún

# Esperar y consultar resultados cada 5 segundos hasta que esté listo
max_retries = 10  # Intentar 10 veces, por ejemplo
for _ in range(max_retries):
    result = get_analysis_result()
    if result:
        # Mostrar resultado
        print("\n📄 Texto detectado:")
        for line in result["analyzeResult"]["readResults"][0]["lines"]:
            print(line["text"])
        break
    else:
        print("⏳ Esperando por resultados...")
        time.sleep(5)
else:
    print("⚠️ No se pudo obtener el resultado después de varios intentos.")
