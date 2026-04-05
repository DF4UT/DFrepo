from db import exe

exe("DELETE FROM test2 WHERE id > 6")
sl = exe("SELECT * FROM test2")
print(sl)
