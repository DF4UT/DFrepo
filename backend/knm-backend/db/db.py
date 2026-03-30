import sqlite3

def connect():
    global db, cursor
    db = sqlite3.connect('knm.db')
    cursor = db.cursor()
    return True

def close():
    db.close()
    cursor.close()
    return True

def create_table(table_name: str, columns: str):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
    db.commit()
    return True

def insert(table_name: str, columns: str, values: str):
    cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
    db.commit()
    return True

def select(table_name: str, columns: str):
    cursor.execute(f"SELECT {columns} FROM {table_name}")
    return cursor.fetchall()

def update(table_name: str, columns: str, where: str):
    cursor.execute(f"UPDATE {table_name} SET {columns} WHERE {where}")
    db.commit()
    return True

def delete(table_name: str, where: str):
    cursor.execute(f"DELETE FROM {table_name} WHERE {where}")
    db.commit()
    return True