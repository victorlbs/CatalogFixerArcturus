import xml.etree.ElementTree as ET
import mysql.connector

# Caminho do arquivo XML
xml_file = 'furnidata.xml'


try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
except Exception as e:
    print(f"Erro ao carregar o arquivo XML: {e}")
    exit()


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'habbo'
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Erro de conexão: {err}")
    exit()

modified_items = []


for furni in root.find('roomitemtypes'):
    classname = furni.get('classname')
    name = furni.find('name').text

    sql = "UPDATE catalog_items SET catalog_name = %s WHERE catalog_name = %s"
    try:
        cursor.execute(sql, (name, classname))
        if cursor.rowcount > 0:
            modified_items.append({'catalog_name': classname, 'new_catalog_name': name})
            print(f"Atualizado com sucesso: {classname} -> {name}")
        else:
            print(f"Nenhum registro encontrado para: {classname}")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar: {err}")


print("\nRegistros modificados:")
print(modified_items)


conn.commit()
cursor.close()
conn.close()
