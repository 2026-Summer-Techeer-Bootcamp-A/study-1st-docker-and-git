# Flask 라이브러리에서 Flask 클래스를 가져와요.
from flask import Flask

# Flask 애플리케이션 객체를 만들어요. 이 app 이 우리 웹 서버예요.
app = Flask(__name__)


# "/" 주소(루트 경로)로 접속하면 아래 함수가 실행돼요.
@app.route("/")
def hello():
    return "<h1>Hello Docker! 🐳</h1><p>도커 컨테이너 안에서 실행되고 있어요.</p>"


# 이 파일을 직접 실행했을 때만 서버를 띄워요.
if __name__ == "__main__":
    # host="0.0.0.0" 으로 해야 컨테이너 바깥에서도 접속할 수 있어요.
    # 5000번 포트로 서버를 열어요.
    app.run(host="0.0.0.0", port=5000)
