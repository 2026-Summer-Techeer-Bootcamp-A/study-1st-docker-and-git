# python 3.12 slim 버전 사용
FROM python:3.12-slim

# 컨테이너 안에서 작업할 폴더를 정해요. 앞으로의 명령어는 이 폴더 기준으로 실행돼요.
WORKDIR /app

# 먼저 requirements.txt 만 복사해요.
COPY requirements.txt .

# requirements.txt 에 적힌 라이브러리(flask)를 설치해요.
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 소스코드(app.py 등)를 컨테이너 안으로 복사해요.
COPY . .

# 이 컨테이너가 5000번 포트를 사용한다는 것을 알려줘요. 
EXPOSE 5000

# 컨테이너가 시작될 때 실행할 명령어예요. "python app.py" 로 서버를 띄워요.
CMD ["python", "app.py"]
