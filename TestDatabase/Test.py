import sqlite3

# Create a connection to the database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with columns: Position (integer) and Direction (text)
cursor.execute('''CREATE TABLE IF NOT EXISTS positions
                  (Position INTEGER, Direction TEXT)''')

# Function to update the first two values in the database
def update_values(position, direction):
    # Update the first two rows with the provided values
    cursor.execute('''UPDATE positions SET Position = ?, Direction = ? WHERE rowid IN (1, 2)''', (position, direction))
    # Commit the changes to the database
    conn.commit()

# Function to insert new values into the database
def insert_values(position, direction):
    # Insert new values into the positions table
    cursor.execute('''INSERT INTO positions (Position, Direction) VALUES (?, ?)''', (position, direction))
    # Commit the changes to the database
    conn.commit()

# Example usage of the update_values and insert_values functions
update_values(10, 'North')
update_values(5, 'East')
insert_values(8, 'Southwest')

# Fetch and print values from the database
cursor.execute('''SELECT * FROM positions''')
rows = cursor.fetchall()
for row in rows:
    print('Position:', row[0], 'Direction:', row[1])

# Close the cursor and connection
cursor.close()
conn.close()
d