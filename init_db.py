import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('reviews.db')
cursor = conn.cursor()

# Drop the table if it exists
cursor.execute('DROP TABLE IF EXISTS reviews')

# Create a new table
cursor.execute('''
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    review TEXT NOT NULL,
    sentiment TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
