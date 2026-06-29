from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv() # .env 파일 읽어오기
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'  # 시크릿 키 설정
ENV_NAME = os.environ.get('ENV_NAME', 'Unknown')  # 환경 변수에서 ENV_NAME 가져오기, 없으면 'Unknown'으로 설정


# "/" 주소(루트 경로)로 접속하면 아래 함수가 실행돼요.
@app.route("/")
def hello():
    return f"<h1>Hello Docker! 🐳</h1><p>도커 컨테이너 안에서 실행되고 있어요. 이름은 {ENV_NAME} 입니다.</p>"


# 이 파일을 직접 실행했을 때만 서버를 띄워요.
if __name__ == "__main__":
    # host="0.0.0.0" 으로 해야 컨테이너 바깥에서도 접속할 수 있어요.
    # 5000번 포트로 서버를 열어요.
    app.run(host="0.0.0.0", port=5000)
