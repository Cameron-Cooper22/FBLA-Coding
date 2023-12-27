import sqlite3
from Functions_AND_Tools.sql_functions import SQL
from pdf_functions import PDF

# database format is name TEXT, phone_number TEXT, address TEXT

# address format is Street Address, City, State Postal Code i.e.
# 2800 NE Shoal Creek Pkwy, Kansas City, MO 64156

sql = SQL("fbla.db", "organizations")
with open('thing.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

# cursor.executescript(sql_script)

# rows = cursor.execute("SELECT name, phone_number, address FROM organizations").fetchall()

if __name__ == "__main__":
        # print(rows)
        out_document = PDF("test.pdf", "doc test title", "test title", "test subtitle", ["test line 1", "test line 2", "test line 3", "test line 4"])
        out_document.create_pdf()