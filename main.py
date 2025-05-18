# 타입 힌트를 위한 모듈 임포트
from typing import Union

# FastAPI 모듈에서 FastAPI 클래스 임포트
from fastapi import FastAPI

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 루트 경로('/')에 대한 GET 요청 처리 함수 정의
@app.get("/")
def read_root():
    # JSON 형태로 응답 반환
    return {"Hello": "World"}

# "/items/{item_id}" 경로에 대한 GET 요청 처리 함수 정의
# 경로 매개변수 item_id는 정수형, 쿼리 매개변수 q는 선택적인 문자열
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # item_id와 q 값을 JSON 형태로 응답
    return {"item_id": item_id, "q": q}
