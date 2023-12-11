import sqlite3
import os

class SQL:
    def __init__(self, database: str, main_table: str) -> None:
        self.database = database
        con         =   sqlite3.connect(database)
        self.cursor = con.cursor()
        self.main_table = main_table
        if not os.path.exists(database):
            self.cursor.execute(f"CREATE TABLE {self.main_table} (name TEXT, phone_number TEXT, address TEXT)")
        
    
    def select(self, statement: str) -> list:
        """
        params: statement refers to items selected from database. Format is similar to name, phone_number or just name
        returns: list with data retrieved from database
        """
        return self.cursor.execute(f"SELECT {statement} FROM {self.main_table}").fetchall()
    
    def insert_org(self, name: str, phone_number: str, address: str):
        """
        Parameters are self explanatory
        Function inserts a new organization to table_name, defaulting to organizations
        """
        self.cursor.execute(f"INSERT INTO {self.main_table} ({name}, {phone_number}, {address})")    
        
    def create_table(self, name: str, types: list, *params: str):
        """
        The list types must be same length as how many params there are
        Function creates a new table, throws exception if table already made
        """
        
        types = [i.upper() for i in types]
        try:
            table = f"CREATE TABLE {name} ("
            for i in params:
                table += f"{params[i]}, {types[i]}, "
            table += ")"
            self.cursor.execute(table)
        except:
            print("Table with that name already created or params is of different length than types list.")
        

        
        
            
sql = SQL("fbla.db", "organizations")
names = sql.select("name")

print(names)