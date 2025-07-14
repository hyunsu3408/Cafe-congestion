# PostgreSQL 연결 설정
import os
import requests
from dotenv import load_dotenv
import psycopg2
import re
import time

load_dotenv()

def db_connect():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()
        print("DB connect 성공")
        return cur,conn
    except Exception as e:
        print("실패",e)
        return None,None