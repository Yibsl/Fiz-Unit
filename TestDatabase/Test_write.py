import sqlite3
import json



def create():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Data
                    (Pos TEXT, BatVoltage INTEGER, RecStatus INTEGER, Lidar INTEGER, Marks TEXT)''')

def delete():
    cursor.execute("DROP TABLE Data")

# Function to insert data into the table
def insert_data(data):
    data_to_insert = json.dumps(data)  # Convert the dictionary to a JSON string
    cursor.execute('''INSERT INTO Data (Pos, BatVoltage, RecStatus, Lidar, Marks) VALUES (?, ?, ?, ?, ?)''',
                   (json.dumps(data["Pos"]), data["BatVoltage"], int(data["RecStatus"]), data["Lidar"], json.dumps(data["Marks"])))
    conn.commit()

# Function to update all values in the table
def update_all_values(new_data):
    cursor.execute('''UPDATE Data SET 
                      Pos = ?,
                      BatVoltage = ?,
                      RecStatus = ?,
                      Lidar = ?,
                      Marks = ?''', (json.dumps(new_data["Pos"]), new_data["BatVoltage"],
                                    int(new_data["RecStatus"]), new_data["Lidar"], json.dumps(new_data["Marks"])))
    conn.commit()

# Function to print all values from the table
def print_all_values():
    cursor.execute('''SELECT * FROM Data''')
    rows = cursor.fetchall()
    prin1t(rows)
    for row in rows:
        print('Pos:', json.loads(row[0]))
        print('BatVoltage:', row[1])
        print('RecStatus:', row[2])
        print('Lidar:', row[3])
        print('Marks:', json.loads(row[4]))
        print('---')

delete()
create()
# Sample data
sample_data = {
    "Pos": {"X": 10, "Y": 20, "Z": 5},
    "BatVoltage": 12,
    "RecStatus": True,
    "Lidar": 150,
    "Marks": {"A": 1, "B": 2, "C": 3}
}

# Insert data into the table
insert_data(sample_data)

# Update all values and print them
updated_data = {
    "Pos": {"X": 15, "Y": 25, "Z": 10},
    "BatVoltage": 18,
    "RecStatus": False,
    "Lidar": 200,
    "Marks": {"A": 3, "B": 2, "C": 1,"D":3}
}

print("old")
print_all_values()
update_all_values(updated_data)
print('Updated Values:')
print_all_values()

# Close the cursor and connection
cursor.close()
conn.close()
