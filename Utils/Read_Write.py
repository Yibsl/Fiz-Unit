import sqlite3 as sq
import json
import random
import time
from Debug import *


class Focus:
    def __init__(self):
        self.con = sq.connect(r"/home/kali/Desktop/Struktur/Databases/Focus_Database.db")
        self.cur = self.con.cursor()
        
    def create(self):
        self.cur.execute("CREATE TABLE Focus(Pos INTEGER ,Direction VARCHAR(255))")
        
    def delete(self):
        self.cur.execute("DROP TABLE Focus")

    def insert_values(self,position, direction):
        # Insert new values into the Focus table
        self.cur.execute('''INSERT INTO Focus (Pos, Direction) VALUES (?, ?)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def update_values(self,position, direction):
        # Update the first two rows with the provided values
        self.cur.execute('''UPDATE Focus SET Pos = ?, Direction = ? WHERE rowid IN (1, 2)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def get(self,key):
        res = self.cur.execute(f"SELECT {key} FROM Focus")
        res = res.fetchall()
        positions = [item for sublist in res for item in sublist]
        return positions[0]


    def close(self):
        self.cur.close()
        self.con.close()
        
class Zoom:
    def __init__(self):
        self.con = sq.connect(r"/home/kali/Desktop/Struktur/Databases/Zoom_Database.db")
        self.cur = self.con.cursor()

    def create(self):
        self.cur.execute("CREATE TABLE Zoom(Pos INTEGER ,Direction VARCHAR(255))")
        
    def delete(self):
        self.cur.execute("DROP TABLE Zoom")

    def insert_values(self,position, direction):
        # Insert new values into the Iris table
        self.cur.execute('''INSERT INTO Zoom (Pos, Direction) VALUES (?, ?)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def update_values(self,position, direction):
        # Update the first two rows with the provided values
        self.cur.execute('''UPDATE Zoom SET Pos = ?, Direction = ? WHERE rowid IN (1, 2)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def get(self,key):
        res = self.cur.execute(f"SELECT {key} FROM Zoom")
        res = res.fetchall()
        positions = [item for sublist in res for item in sublist]
        return positions[0]

    def close(self):
        self.cur.close()
        self.con.close()

class Iris:
    def __init__(self):
        self.con = sq.connect(r"/home/kali/Desktop/Struktur/Databases/Iris_Database.db")
        self.cur = self.con.cursor()

    def create(self):
        self.cur.execute("CREATE TABLE Iris(Pos INTEGER ,Direction VARCHAR(255))")
        
    def delete(self):
        self.cur.execute("DROP TABLE Iris")

    def insert_values(self,position, direction):
        # Insert new values into the Iris table
        self.cur.execute('''INSERT INTO Iris (Pos, Direction) VALUES (?, ?)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def update_values(self,position, direction):
        # Update the first two rows with the provided values
        self.cur.execute('''UPDATE Iris SET Pos = ?, Direction = ? WHERE rowid IN (1, 2)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def get(self,key):
        res = self.cur.execute(f"SELECT {key} FROM Iris")
        res = res.fetchall()
        positions = [item for sublist in res for item in sublist]
        return positions[0]

    def close(self):
        self.cur.close()
        self.con.close()

class Button:
    def __init__(self):
        # Create a connection to the database (or create it if it doesn't exist)
        self.con = sq.connect(r"/home/kali/Desktop/Struktur/Databases/Buttons_Database.db")
        # Create a cursor object to execute SQL commands
        self.cursor = self.con.cursor()

    def create(self):
        # Create a table with columns: ButtonID (integer) and ButtonState (integer)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS button_states
                        (ButtonID INTEGER, ButtonState INTEGER)''')

    def delete(self):
        self.cursor.execute("DROP TABLE button_states")


    # Function to store button states in the database
    def store_button_state(self, button_id, button_state):
        # Check if the button ID already exists in the database
        self.cursor.execute('''SELECT * FROM button_states WHERE ButtonID = ?''', (button_id,))
        existing_entry = self.cursor.fetchone()
        
        # If the button ID exists, update the button state; otherwise, insert a new entry
        if existing_entry:
            self.cursor.execute('''UPDATE button_states SET ButtonState = ? WHERE ButtonID = ?''', (button_state, button_id))
        else:
            self.cursor.execute('''INSERT INTO button_states (ButtonID, ButtonState) VALUES (?, ?)''', (button_id, button_state))
        
        # Commit the changes to the database
        self.con.commit()

    def read_single_button_state(self, button_id):
        self.cursor.execute('''SELECT ButtonState FROM button_states WHERE ButtonID = ?''', (button_id,))
        print("read")
        state = self.cursor.fetchone()
        if state:
            return state[0]
        else:
            return None  # Return None if the button ID is not found

    # Function to read the states of all buttons from the database
    def read_all_button_states(self):
        self.cursor.execute('''SELECT * FROM button_states''')
        rows = self.cursor.fetchall()
        return rows


    def close(self):
        # Close the cursor and connection
        self.cursor.close()
        self.con.close()

class Screen:
    def __init__(self):
        # Create a connection to the database (or create it if it doesn't exist)
        self.Screen_Database = sq.connect(r"/home/kali/Desktop/Struktur/Databases/Screen_Database.db")
        # Create a cursor object to execute SQL commands
        self.cursor = self.Screen_Database.cursor()
        self.F=Focus()
        self.I=Iris()
        self.Z=Zoom()
    
    def create(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Data
                        (Pos TEXT, BatVoltage INTEGER, RecStatus INTEGER, Lidar INTEGER, Marks TEXT)''')

    def delete(self):
        self.cursor.execute("DROP TABLE Data")

    # Function to insert data into the table
    def insert_data(self,data):
        data_to_insert = json.dumps(data)  # Convert the dictionary to a JSON string
        self.cursor.execute('''INSERT INTO Data (Pos, BatVoltage, RecStatus, Lidar, Marks) VALUES (?, ?, ?, ?, ?)''',
                    (json.dumps(data["Pos"]), data["BatVoltage"], int(data["RecStatus"]), data["Lidar"], json.dumps(data["Marks"])))
        self.Screen_Database.commit()

    # Function to update all values in the table
    def update(self,new_data):
        self.cursor.execute('''UPDATE Data SET 
                        Pos = ?,
                        BatVoltage = ?,
                        RecStatus = ?,
                        Lidar = ?,
                        Marks = ?''', (json.dumps(new_data["Pos"]), new_data["BatVoltage"],
                                        int(new_data["RecStatus"]), new_data["Lidar"], json.dumps(new_data["Marks"])))
        self.Screen_Database.commit()
        
    def get_all_values(self):
        self.cursor.execute('''SELECT * FROM Data''')
        rows = self.cursor.fetchall()
        for row in rows:
            pass
            data={
                'Pos': json.loads(row[0]),
                'BatVoltage': row[1],
                'RecStatus': row[2],
                'Lidar': row[3],
                'Marks': json.loads(row[4]),
            }
        return data
        
    # Function to print all values from the table
    def print_all_values(self):
        self.cursor.execute('''SELECT * FROM Data''')
        rows = self.cursor.fetchall()
        for row in rows:
            pass
            print('Pos:', json.loads(row[0]))
            print('BatVoltage:', row[1])
            print('RecStatus:', row[2])
            print('Lidar:', row[3])
            print('Marks:', json.loads(row[4]))
            print('---')

    def collect_data(self):
        F=self.F.get("Pos")
        I=self.I.get("Pos")
        Z=self.Z.get("Pos")
        BatVol=3.4
        RecStat=0
        Lidar=0
        Marks={}

        data = {
            "Pos": {"Fpos": F, "Ipos": I, "Zpos": Z},
            "BatVoltage": BatVol,
            "RecStatus": RecStat,
            "Lidar": Lidar,
            "Marks": Marks
            }

        return data
    
class Settings:
    def __init__(self):
        debug(1,"innit Settings")
        self.con = sq.connect(r"/home/kali/Desktop/Struktur/Databases/Settings_Database.db")
        self.cur = self.con.cursor()

    def create(self):
        self.cur.execute("CREATE TABLE Screen (Brightness INTEGER, ColorF TEXT, ColorI TEXT, ColorZ TEXT, ColorBG TEXT,Font TEXT)")
        F="{255,0,0}"
        I="{0,255,0}"
        Z="{0,0,255}"
        BG="{0,0,0}"
        self.cur.execute('''INSERT INTO Screen (Brightness, ColorF, ColorI, ColorZ, ColorBG, Font) VALUES (?, ?, ?, ?, ?, ?)''', (100, F, I, Z, BG,'freesansbold.ttf'))

        self.con.commit()
        self.cur.execute("CREATE TABLE Focus (Direction INTEGER, Resistance INTEGER, Vibration INTEGER, Sensebility INTEGER)")
        self.cur.execute('''INSERT INTO Focus (Direction, Resistance, Vibration, Sensebility) VALUES (?, ?, ?, ?)''', (0, 5, 5, 1))

        self.cur.execute("CREATE TABLE Iris (Direction INTEGER, Resistance INTEGER, Vibration INTEGER)")
        self.cur.execute('''INSERT INTO Iris (Direction, Resistance, Vibration) VALUES (?, ?, ? )''', (0,5,5))
  

        self.cur.execute("CREATE TABLE Zoom (Direction INTEGER, Resistace INTEGER, Sensebility INTEGER)")
        self.cur.execute('''INSERT INTO Zoom (Direction, Resistace, Sensebility) VALUES (?, ?, ?)''', (0, 5, 1))

        self.cur.execute("CREATE TABLE Misc (Autofocus INTEGER, PowerState FLOAT, CurrentLense)")
        self.cur.execute('''INSERT INTO Misc (Autofocus, PowerState, CurrentLense) VALUES (?, ?, ?)''', (0, 3.9, 1))

        self.cur.execute("CREATE TABLE Lenses (Id INTEGER, Name TEXT, VariableZoom INTEGER, mmMin INTEGER, mmMax INTEGER, ApatureMin FLOAT, ApatureMax FLOAT, FocusMin INTEGER, FocusMax INTEGER, Focus TEXT, Iris TEXT, Zoom Text)")
        Focus={}
        Iris={            
            "0":1.5,
            "1":2,
            "2":2.8,
            "3":4,
            "4":5.6,
            "5":8,
            "6":11,
            "7":16,
            "8":22}
        Zoom={}
        self.cur.execute('''INSERT INTO Lenses (Id, Name, VariableZoom, mmMin, mmMax, ApatureMin, ApatureMax, FocusMin, FocusMax, Focus, Iris, Zoom) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (1, "Sigma 18_35 1.8", 1, 18, 35, 1.8, 22, 20, 50, str(Focus), str(Iris), str(Zoom)))

        self.con.commit()
             
    def delete(self,table):
        if table=="all":
            self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = self.cur.fetchall()
            # Drop each table
            for table in tables:
                table_name = table[0]
                self.cur.execute(f"DROP TABLE IF EXISTS {table_name};")
                print(f"Dropped table: {table_name}")
        else:
            try:
                self.cur.execute(f"DROP TABLE {table};")
            except:
                print("failed delete")

    def update_values(self,key, value):
        # Update the first two rows with the provided values
        self.cur.execute('''UPDATE Iris SET Pos = ?, Direction = ? WHERE rowid IN (1, 2)''', (position, direction))
        # Commit the changes to the database
        self.con.commit()

    def get_by_key(self, key, table):
        try:
            query = f"SELECT {key} FROM {table}"
            self.cur.execute(query)
            result = self.cur.fetchall()
            result = [item for sublist in result for item in sublist]

            if result is not None:
                return result[0]
            else:
                print(f"No result found for key '{key}' in table '{table}'.")
                return None

        except Exception as e:
            print(f"Error in get method: {e}")
            return None

    def get_by_id(self, key, table, id):
        try:
            query = f"SELECT {key} FROM {table} WHERE id = ?"
            self.cur.execute(query, (id,))
            result = self.cur.fetchall()

            if result is not None:
                return result[0]
            else:
                print(f"No result found for ID '{id}' in table '{table}'.")
                return None

        except Exception as e:
            print(f"Error in get_by_id method: {e}")
            return None


    def close(self):
        self.cur.close()
        self.con.close()

