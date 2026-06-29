# docker-practice

Docker를 처음 접하는 분들을 위한 아주 간단한 Python(Flask) 웹앱 예제예요. 🐳

## 구성 파일

| 파일 | 설명 |
| --- | --- |
| `app.py` | "Hello Docker!" 한 줄을 보여주는 Flask 웹앱 |
| `requirements.txt` | 설치할 파이썬 라이브러리 목록 (flask) |
| `Dockerfile` | 이 앱을 도커 이미지로 만드는 방법을 적은 설명서 |
| `docker-compose.yml` | 컨테이너를 띄우고 내리는 걸 간편하게 해주는 설정 |
| `.dockerignore` | 이미지에 넣지 않을 파일 목록 |

## 실행 방법

> 미리 [Docker Desktop](https://www.docker.com/products/docker-desktop/) 이 설치되어 있어야 해요.

이 폴더(`docker-practice`) 안에서 아래 명령어를 실행하세요.

```bash
# 이미지를 빌드하고 컨테이너를 띄워요. (처음엔 빌드하느라 시간이 좀 걸려요)
docker compose up

# 끝내고 싶으면 터미널에서 Ctrl + C 를 누른 뒤,
docker compose down
```

서버가 뜨면 브라우저에서 아래 주소로 접속해보세요.

```
http://localhost:5000
```

"Hello Docker! 🐳" 가 보이면 성공이에요! 🎉
