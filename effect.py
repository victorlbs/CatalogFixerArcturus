import json
import requests
import concurrent.futures


with open("effectmap.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def download_effect(effect):
    lib_name = effect["lib"]
    url = f"https://images.habblet.city/leet-asset-bundles/libraries/effect/{lib_name}.nitro"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(f"{lib_name}.nitro", "wb") as f:
                f.write(response.content)
            print(f"✔ Baixado: {lib_name}.nitro")
        else:
            print(f"❌ Erro ao baixar {lib_name}.nitro - Código {response.status_code}")
    except requests.RequestException as e:
        print(f"⚠ Erro de conexão para {lib_name}: {e}")


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(download_effect, data["effects"])
