import json
import requests
import os
from concurrent.futures import ThreadPoolExecutor


json_file = "figuremap.json"

output_folder = "visuais"

os.makedirs(output_folder, exist_ok=True)


with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)


ids = [library["id"] for library in data.get("libraries", [])]


def download_file(item_id):
    file_url = f"https://images.habblet.city/leet-asset-bundles/libraries/figure/{item_id}.nitro"
    file_path = os.path.join(output_folder, f"{item_id}.nitro")

    try:
        response = requests.get(file_url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✔ Download concluído: {item_id}.nitro")
        else:
            print(f"❌ Erro ao baixar: {item_id}.nitro (Status {response.status_code})")
    except Exception as e:
        print(f"❌ Erro ao processar {item_id}: {e}")


max_threads = 10  # Ajuste conforme necessário
with ThreadPoolExecutor(max_threads) as executor:
    executor.map(download_file, ids)

print("✅ Processo finalizado!")