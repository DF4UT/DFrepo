from db import exe

# exe("CREATE TABLE IF NOT EXISTS test2 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
st = exe("SELECT name FROM sqlite_master WHERE type='table';")
# ist = exe("INSERT INTO test2 (name) VALUES ('test')")
sl = exe("SELECT * FROM test2")
print(st)

print(sl)


def get_test2():
    return exe("SELECT * FROM test2")
