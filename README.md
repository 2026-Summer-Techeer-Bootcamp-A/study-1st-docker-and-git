# study-1st-docker-and-git
Docker, Github를 스터디한 내용을 테스트 해 봅시다.


## README.md
README.md 파일은 말 그대로 사용자 혹은 개발자에게 어떠한 내용을 알려주기 위해 작성되는 파일이며, 레포지토리 페이지에 들어가면 가장 먼저 보이게 됩니다.

## 스터디 과제
### 1. {자신의 이름}.txt 파일 만들어 보기
 - `docs/(자신 이름 영어로)` 이름으로 된 브랜치를 만든 후, 이 프로젝트의 루트 폴더에 {자신의 이름}.txt 로 된 파일을 추가하세요.
 - 그 후, 커밋한 다음 푸시해 보세요.
 - 그 후에 Pull Request까지 올려 보세요.
 
 
### 2. Issue 만들어 보기
 - 간단한 과제입니다. Issue 탭에 들어가 아무 이슈나 하나 올려보세요.


### 3. 다른 사람 PR에 리뷰 남겨 보기
협업의 핵심인 "코드 리뷰"를 경험해 보는 과제입니다. PR을 올리는 것만큼이나, 다른 사람의 PR을 읽고 의견을 남기는 것도 중요합니다.

 - 스터디원 중 다른 사람이 올린 Pull Request 하나를 골라 들어가세요.
 - PR 페이지 상단의 `Files changed` 탭을 눌러, 어떤 파일이 어떻게 바뀌었는지 확인하세요. (초록색은 추가된 줄, 빨간색은 삭제된 줄입니다.)
 - 특정 줄에 마우스를 올리면 나타나는 파란색 `+` 버튼을 눌러, 그 줄에 코멘트를 남겨 보세요. (일단은 아무 내용이나 올리셔도 됩니다.)
 - 코멘트 작성을 끝냈다면, 우측 상단의 `Review changes` 버튼을 누르세요.
 - `Comment`(단순 의견), `Approve`(승인), `Request changes`(수정 요청) 중 하나를 선택하고 `Submit review`를 눌러 리뷰를 제출하세요.


### 4. 내 PR을 직접 머지(Merge)하고 브랜치 정리하기
1번 과제에서 PR을 "올리는 것"까지 했다면, 이번에는 그 PR이 실제로 `main` 브랜치에 합쳐지는 과정을 진행할 것입니다.

 - 1번 과제에서 자신이 올렸던 Pull Request로 다시 들어가세요.
 - 페이지 아래쪽의 `Merge pull request` 버튼을 누른 뒤, `Confirm merge`를 눌러 변경 내용을 `main` 브랜치에 합치세요.
 - 머지가 끝나면 나타나는 `Delete branch` 버튼을 눌러, 이제 역할이 끝난 작업 브랜치를 삭제하세요. (GitHub 원격 저장소에서 지워집니다.)
 - 마지막으로 내 컴퓨터(로컬)에도 합쳐진 내용을 가져옵니다. 터미널에서 아래 명령어를 실행하세요.

```bash
# 먼저 main 브랜치로 이동
git switch main

# 원격 저장소(GitHub)의 최신 내용을 내 컴퓨터로 가져오기
git pull origin main

# (선택) 로컬에 남아있는 작업 브랜치도 삭제
git branch -d docs/your-name
```


### 5. Docker로 웹앱 띄워보기
이번에는 Docker를 사용해 봅시다. `docker-practice` 폴더에 아주 간단한 Python(Flask) 웹앱이 준비되어 있어요.

> 미리 [Docker Desktop](https://www.docker.com/products/docker-desktop/) 을 설치해 두세요.

 - 터미널에서 `docker-practice` 폴더로 이동하세요.

```bash
cd docker-practice
```

 - 아래 명령어로 컨테이너를 빌드하고 실행하세요. (처음엔 이미지를 만드느라 시간이 조금 걸려요.)

```bash
docker compose up
```

 - 브라우저를 열고 `http://localhost:5000` 으로 접속하세요. "Hello Docker! 🐳" 가 보이면 성공입니다.
 
 
 - 열어둔 컨테이너를 닫으려면, `docker compose down` 을 입력하세요. 볼륨까지 삭제하고 싶으시다면 `docker compose down -v` 를 입력하시면 됩니다.

