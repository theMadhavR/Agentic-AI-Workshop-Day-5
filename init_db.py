import sqlite3

def create_database():
    db_name = "students.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Drop table if exists to ensure clean initialization
    cursor.execute("DROP TABLE IF EXISTS students")

    # Create students table
    cursor.execute("""
    CREATE TABLE students (
        student_id TEXT PRIMARY KEY,
        name TEXT,
        department TEXT,
        python INTEGER,
        database INTEGER,
        ai INTEGER,
        web INTEGER
    )
    """)

    # Student data as specified in problem statement
    students_data = [
        ("22CS045", "Dhanushya", "Computer Science", 85, 72, 90, 78),
        ("22CS046", "Rahul", "Computer Science", 65, 70, 68, 72),
        ("22CS047", "Priya", "Information Technology", 92, 88, 95, 90),
        ("22CS048", "Arun", "Information Technology", 55, 60, 58, 62),
        ("22CS049", "Meena", "Computer Science", 78, 85, 80, 88)
    ]

    cursor.executemany("""
    INSERT INTO students (student_id, name, department, python, database, ai, web)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, students_data)

    conn.commit()

    # Verify insertion
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print(f"Successfully initialized '{db_name}' with {len(rows)} records:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    create_database()
