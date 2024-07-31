import sqlite3

# Function to create the database and table if they don't exist
def create_database():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS book (
                 id INTEGER PRIMARY KEY,
                 title TEXT,
                 author TEXT,
                 qty INTEGER)''')
    conn.commit()
    conn.close()

# Function to add a new book to the database
def add_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    qty = int(input("Enter quantity: "))
    c.execute("INSERT INTO book (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    conn.commit()
    conn.close()

# Function to update book information
def update_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    book_id = int(input("Enter book ID to update: "))
    title = input("Enter new book title: ")
    author = input("Enter new author name: ")
    qty = int(input("Enter new quantity: "))
    c.execute("UPDATE book SET title=?, author=?, qty=? WHERE id=?", (title, author, qty, book_id))
    conn.commit()
    conn.close()

# Function to delete a book from the database
def delete_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    book_id = int(input("Enter book ID to delete: "))
    c.execute("DELETE FROM book WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

# Function to search for a specific book
def search_books():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    keyword = input("Enter book title or author: ")
    c.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
    books = c.fetchall()
    if books:
        print("Books found:")
        for book in books:
            print(book)
    else:
        print("No books found.")
    conn.close()

# Main function to display menu and handle user input
def main():
    create_database()
    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

# Prompt user for choice      
        choice = input("Enter your choice: ")

# Based on choice, call corresponding function or exit program
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
