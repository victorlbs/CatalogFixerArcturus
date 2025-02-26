import json
import xml.etree.ElementTree as ET


with open("FurnitureDataNova25.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)


tree = ET.parse("furnidata.xml")
root = tree.getroot()


xml_data = {}
for item in root.findall(".//furnitype"):
    classname = item.get("classname")
    name = item.find("name").text if item.find("name") is not None else ""
    description = item.find("description").text if item.find("description") is not None else ""
    xml_data[classname] = {"name": name, "description": description}


for furniture in json_data["roomitemtypes"]["furnitype"]:
    classname = furniture.get("classname")
    if classname in xml_data:
        furniture["name"] = xml_data[classname]["name"]
        furniture["description"] = xml_data[classname]["description"]


with open("FurnitureDataAtualizado.json", "w", encoding="utf-8") as json_out:
    json.dump(json_data, json_out, indent=4, ensure_ascii=False)

print("✅ Arquivo atualizado e salvo como 'FurnitureDataAtualizado.json'")
