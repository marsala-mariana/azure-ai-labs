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

with open(file_path, "rb") as f:
    data = f.read()

print("📤 Enviando archivo local a Azure OCR...")
response = requests.post(analyze_url, headers=headers, data=data)
if response.status_code != 202:
    print("⚠️ Error en la solicitud:")
    print(response.status_code)
    print(response.text)  # Esto nos dirá qué espera Azure
    response.raise_for_status()
operation_url = response.headers["Operation-Location"]
print(f"⏳ Esperando resultados desde: {operation_url}")

# Esperar y consultar resultados
time.sleep(10)

result = requests.get(operation_url, headers=headers).json()

# Mostrar resultado
print("\n📄 Texto detectado:")
for line in result["analyzeResult"]["readResults"][0]["lines"]:
    print(line["text"])