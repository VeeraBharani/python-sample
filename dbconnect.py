import pymysql
from pymysql import Error

def connection():
    conn = pymysql.connect(host="localhost",
                           user = "root",
                           passwd = "123",
                           db = "pythonprogramming")
    c = conn.cursor()

    return c, conn
