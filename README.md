`docker-compose` 파일을 정상적으로 실행하기 위해서는 다음과 같은 세팅을 해 주어야 합니다.

- `aihub-ocr-demo` 네트워크가 필요합니다. `docker-compose` 파일을 실행하기 전에 `docker network create aihub-ocr-demo` 명령어를 실행해 주세요. `프론트엔드` 컨테이너와 `금융모델` 컨테이너, `물류모델` 컨테이너가 이 네트워크에 연결되어 있습니다.
- `dockerfiles/publish/pretrained` 에 가중치 파일을 수동으로 넣어야 합니다. 리팩터링 시 컨테이너 내부에서 클라우드 레지스트리를 통해 다운로드받도록 수정하기를 권장합니다.
- `docker-compose` 가 호출하는 `Dockerfile` 의 상당수가 개인 github 계정을 통해 다운로드 받습니다. (1) 저자 `dlwkdgn1@naver.com` 이 개인적으로 만들어 두었던 코드 스니펫을 조합한 경우가 있고, (2) CI/CD 기능 이용 및 GitLab 권한 문제로부터 벗어나 조금 더 빠른 개발을 위한 경우가 있고, (3) Github 에서 지속적으로 업데이트되는 오픈소스 저장소에  풀 리퀘스트를 작성하고 지속적인 rebase 를 받아오기 위해 해당 방식을 채택했습니다. GitLab 에 동일한 이름으로 저장소가 등록되어있을 예정이기 때문에 해당 부분은 제가 퇴사를 하게 되더라도 수정해 사용하면 됩니다.

```bash
docker-compose build && docker-compose up
```