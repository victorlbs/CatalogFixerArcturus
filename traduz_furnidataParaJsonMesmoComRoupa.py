import json
import xml.etree.ElementTree as ET


json_file = "FurnitureDataAtualizado.json"
xml_file = "furnidata.xml"
output_file = "furni_atualizado.json"


with open(json_file, "r", encoding="utf-8") as f:
    furni_data = json.load(f)


furni_json = furni_data.get("roomitemtypes", {}).get("furnitype", [])


tree = ET.parse(xml_file)
root = tree.getroot()


furni_data_map = {}


for furni in root.findall(".//furnitype"):
    classname = furni.get("classname", "").strip().lower()  # Convertendo para minúsculas e removendo espaços extras


    customparams_elem = furni.find("customparams")
    customparams_value = customparams_elem.text.strip() if customparams_elem is not None and customparams_elem.text else "0"

    specialtype_elem = furni.find("specialtype")
    specialtype_value = int(specialtype_elem.text.strip()) if specialtype_elem is not None and specialtype_elem.text and specialtype_elem.text.strip().isdigit() else 0


    name_elem = furni.find("name")
    name_value = name_elem.text.strip() if name_elem is not None and name_elem.text else classname  # Usa classname se name for None

    description_elem = furni.find("description")
    description_value = description_elem.text.strip() if description_elem is not None and description_elem.text else classname  # Usa classname se description for None

   
    print(f"🔍 Extraído do XML - {classname}: customparams={customparams_value}, specialtype={specialtype_value}")

    if classname:
        furni_data_map[classname] = {
            "customparams": customparams_value,
            "specialtype": specialtype_value,
            "name": name_value,
            "description": description_value
        }


for item in furni_json:
    classname = item.get("classname", "").strip().lower()  # Normaliza o classname

    if classname.startswith("clothing_"):
        print(f"🔎 Verificando {classname} no XML...")

        if classname in furni_data_map:
            print(f"✔ Atualizando {classname}")
            item["customparams"] = furni_data_map[classname].get("customparams", "0")
            item["specialtype"] = furni_data_map[classname].get("specialtype", 0)
            item["name"] = furni_data_map[classname].get("name", classname)
            item["description"] = furni_data_map[classname].get("description", classname)
        else:
            print(f"⚠ Não encontrado no XML: {classname}")

furni_data["roomitemtypes"]["furnitype"] = furni_json

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(furni_data, f, indent=4, ensure_ascii=False)

print(f"✅ Arquivo '{output_file}' atualizado com sucesso!")
