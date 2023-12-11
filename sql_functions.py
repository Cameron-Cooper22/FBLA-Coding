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
        
    def create_table(self, name: str, types: list, *args: str):
        """
        Function creates a table or throws error if table with that name already exists
        
        params: name should be of new table, will print error message otherwise
                types is a list that must have the same length as the amount of arguments in args.
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
    
    def array_to_text(self, arr: list) -> str:
        """
        Creates stringified array that is able to be stores as type text.
        Format is python string, [element0, element1...]

        params: arr is list containing values of any type.
        """
        s = "["
        for i in range(0, len(arr)):
            s += f"{arr[i]}, "
        s += "]"
        return s
    
    def text_to_array(self, s: str) -> list:
        """
        Reformats string into array to read an array stored in database.
        String given must not contain '[' or ']' as an element name, only as the beginning or end.
        
        params: s: string to be read into an array.
        """
        return s.strip("[]").split(", ")
