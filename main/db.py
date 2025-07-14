import os
import requests
from dotenv import load_dotenv
import psycopg2
import re
import time
from db_connect import db_connect

#env 파일 환경변수 로드
load_dotenv()

# KaKao API 설정
KAKAO_API_KEY = os.getenv("KAKAO_REST_API_KEY")
headers = { "Authorization": f"KakaoAK {KAKAO_API_KEY}" }
url = "https://dapi.kakao.com/v2/local/search/keyword.json"


def save_cafe_db(cafe):
    
    cur,conn = db_connect()

    if conn is None or cur is None:
        print("DB 연결 실패")
        return
    
    cur.execute("""
        INSERT INTO cafe (kakao_id, name, address, road_address, phone,
        category, longitude, latitude, place_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (kakao_id) DO NOTHING;
                """,(
                    cafe['id'], cafe['place_name'], cafe['address_name'],cafe['road_address_name'],
                    cafe['phone'], cafe['category_group_name'], float(cafe['x']), float(cafe['y']),
                    cafe['place_url']
                ))
    conn.commit()
    cur.close()
    conn.close()
    
def fetch_all_cafe(query="강남 카페"):
    all_cafes = []
    for page in range(1,4):
        params={
            "query": query,
            "size":15,
            "page":page
            }
        res = requests.get(url,headers=headers,params=params)
        data = res.json()
    
        cafes = data['documents']
        if not cafes:
            break
        all_cafes.extend(cafes)
    return all_cafes
    
    
# 실행

def cafe_region_db():
    cafe_region = ["강남 카페","홍대 카페","신촌 카페","이대 카페","이태원 카페","성수 카페","연남동 카페",\
        "한남동 카페","압구정 카페","청담 카페","종로 카페","인사동 카페","건대입구 카페"]

    for cafe_r in cafe_region:
        cafes = fetch_all_cafe(cafe_r)
        for cafe in cafes:
            save_cafe_db(cafe)
            print(f"저장 완료{len(cafes)}개 수집됨")
            
    print("Success")
    