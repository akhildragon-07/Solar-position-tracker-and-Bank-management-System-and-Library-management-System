import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="librarydb"
)
cursor = conn.cursor()

def add_book(title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (%s,%s,%s)", (title, author, year))
    conn.commit()
    print("Book added successfully!")

def display_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)

while True:
    print("\n1. Add Book\n2. Show Books\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        t = input("Title: ")
        a = input("Author: ")
        y = int(input("Year: "))
        add_book(t, a, y)
    elif choice == 2:
        display_books()
    else:
        break

conn.close()
