import sqlite3  # used to add sql queries and database connectivity

# Connect to SQLite database (or create if it doesn't exist)
connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

# Create a table for storing contacts just like on MYSQL
cursor.execute
("""
CREATE TABLE IF NOT EXISTS contacts 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
""")

connection.commit()  #used to save changes on databases

# Function to add a contact
def add_contact(name, phone, email):
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    connection.commit()
    print("Contact added successfully!")

# function to view all contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    
    if contacts:
        print("\nContacts List:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
    else:
        print("No contacts found.")

# main program loop python
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    
    elif choice == "2":
        view_contacts()
    
    elif choice == "3":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")

# Close database connection
connection.close()
