from db import connect, close, create_table, insert, select

connect()
create_table('test', 'id INTEGER PRIMARY KEY, value TEXT, date DATE DEFAULT CURRENT_DATE')
insert("test", "value, date", "Item 1, 100.0")
rows = select("test", "id, value, date")
print(rows)
close()
