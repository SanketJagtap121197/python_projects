import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Creating a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Inserting data
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")

# Fetching data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Closing connection
conn.commit()
conn.close()
