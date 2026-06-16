import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS faculty(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    faculty TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS rooms(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS timetable_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT,
    generated_at TEXT,
    timetable_data TEXT
)
''')


conn.commit()
conn.close()

print("Database Created Successfully")