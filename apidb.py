import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="database1",
        port=3306
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student(
        student_id INT PRIMARY KEY,
        student_name VARCHAR(20),
        student_age INT,
        student_branch VARCHAR(5)
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_student(student_id, student_name, student_age, student_branch):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Student (student_id, student_name, student_age, student_branch)
    VALUES (%s, %s, %s, %s)
    """, (student_id, student_name, student_age, student_branch))
    conn.commit()
    cursor.close()
    conn.close()

def update_student_name(student_id, new_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Student SET student_name = %s WHERE student_id = %s
    """, (new_name, student_id))
    conn.commit()
    rowcount = cursor.rowcount
    cursor.close()
    conn.close()
    return rowcount


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM Student WHERE student_id = %s
    """, (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
