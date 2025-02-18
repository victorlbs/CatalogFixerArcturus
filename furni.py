import os
import requests
import json
import configparser
from pathlib import Path

def main():
    print("Produzido por Victor - Versão 2025")


    config = configparser.ConfigParser()
    try:
        config.read("config.ini")
        settings = config["Settings"]
        url = settings["JsonUrl"]
        folder_path = settings["FolderPath"]
        base_url = settings["BaseUrl"]
    except Exception as e:
        print(f"Erro ao ler o arquivo de configuração: {e}")
        return

  
    Path(folder_path).mkdir(parents=True, exist_ok=True)

   
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Arquivo JSON baixado com sucesso.")

       
        json_data = response.json()
        furnitype_array = json_data.get("roomitemtypes", {}).get("furnitype", [])

 
        for item in furnitype_array:
            classname = item.get("classname")
            if classname:
                # URL do arquivo .nitro
                nitro_url = f"{base_url}{classname}.nitro"

            
                file_path = os.path.join(folder_path, f"{classname}.nitro")

             
                try:
                    nitro_response = requests.get(nitro_url)
                    if nitro_response.status_code == 404:
                        print(f"Arquivo não encontrado: {nitro_url} (Erro 404)")
                        continue
                    
                    nitro_response.raise_for_status()
                    with open(file_path, "wb") as f:
                        f.write(nitro_response.content)
                    print(f"Arquivo '{file_path}' baixado com sucesso.")
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao baixar o arquivo '{nitro_url}': {e}")
    except Exception as e:
        print(f"Erro ao baixar ou processar o arquivo JSON: {e}")


if __name__ == "__main__":
    main()