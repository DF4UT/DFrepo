import sqlite3
import threading
import os

thread_local = threading.local()

def get_db_connection():
    if not hasattr(thread_local, 'connection'):
        # 使用绝对路径，确保从任何目录都能找到数据库文件
        db_path = os.path.join(os.path.dirname(__file__), 'knm.db')
        print(f"数据库文件路径: {db_path}")
        print(f"文件存在: {os.path.exists(db_path)}")
        thread_local.connection = sqlite3.connect(db_path)
        # 设置行工厂以获取更好的结果
        thread_local.connection.row_factory = sqlite3.Row
    return thread_local.connection

def get_db_cursor():
    connection = get_db_connection()
    if not hasattr(thread_local, 'cursor'):
        thread_local.cursor = connection.cursor()
    return thread_local.cursor

def exe(sql: str):
    try:
        cursor = get_db_cursor()
        print(f"执行SQL: {sql}")
        cursor.execute(sql)
        get_db_connection().commit()
        result = cursor.fetchall()
        print(f"查询结果: {result}")
        return result
    except Exception as e:
        print(f"数据库错误: {e}")
        return []