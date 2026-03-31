from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db.db import exe

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def test():
    """查询test2表数据"""
    tbs = exe("SELECT * FROM test2")
    return tbs

# 调试接口：检查数据库状态
@app.get("/debug")
def debug():
    """调试接口：检查数据库状态"""
    # 检查所有表
    tables = exe("SELECT name FROM sqlite_master WHERE type='table';")
    
    # 检查test2表结构
    test2_structure = exe("PRAGMA table_info(test2);")
    
    # 检查test2表数据
    test2_data = exe("SELECT * FROM test2;")
    
    return {
        "所有表": tables,
        "test2表结构": test2_structure,
        "test2表数据": test2_data
    }