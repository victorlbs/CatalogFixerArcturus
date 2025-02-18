import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="habbo"
)
cursor = conn.cursor()


cursor.execute("SET @row := 0")


sql_update = """
    UPDATE catalog_pages AS cp
    JOIN (
        SELECT id, @row := @row + 1 AS row_number
        FROM catalog_pages, (SELECT @row := 0) r
        WHERE parent_id = %s
        ORDER BY caption
    ) AS subquery
    ON cp.id = subquery.id
    SET cp.order_num = subquery.row_number
"""

# Definir o valor do parent_id desejado
parent_id = 209

cursor.execute(sql_update, (parent_id,))

conn.commit()
cursor.close()
conn.close()

print("Atualização concluída com sucesso!")
