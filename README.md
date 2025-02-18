# CatalogFixerArcturus (CFA)

CatalogFixerArcturus (CFA) is a set of four Python-based systems designed to manage and enhance the Arcturus catalog. It provides functionalities to:

- **Organize the store** – Automatically sort and structure the catalog.
- **Translate the catalog** – Apply translations to catalog items.
- **Download new furniture** – Retrieve and update new furniture items.
- **Download new visuals** – Fetch and update new visual assets.

- note: furnidata.xml and figuremap.xml are required for the code to work example: the translator translates the store through the furnidata you want.

## Requirements

To use CFA, ensure you have the following installed:

- **Python** (latest stable version recommended)
- **MySQL Connector for Python**

You can install the MySQL Connector with the following command:

```bash
pip install mysql-connector-python


Usage
Clone the repository:

git clone https://github.com/victorlbs/CatalogFixerArcturus.git


Navigate to the project directory:
cd CatalogFixerArcturus

python clothe.py
python furni.py
python organiza_loja.py
python traduz_loja.py

Contributing
Feel free to submit issues or pull requests to improve the system. Contributions are always welcome!

License
This project is licensed under the MIT License.

