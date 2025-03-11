import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

def delete_duplicate_employees():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Employees 
        WHERE id NOT IN (
            SELECT MIN(id) FROM Employees GROUP BY name
        )
    """)

    conn.commit()
    conn.close()
