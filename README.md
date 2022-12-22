개발용 도커 컨테이너 내에서 `gitlab` 저장소를 clone/push 하기 위해 다음 작업을 수행합니다.
다음 명령어를 통해 생성된 `id_rsa` 파일은 `dockerfiles/develop/id_rsa` 에 위치해 있어야 합니다.
또한, `dockerfiles/develop/pretrained` 내부에 사전학습 가중치가 존재해야 합니다.

```bash
cd dockerfiles/develop
ssh-keygen -o -f ./id_rsa
```

위 명령어를 실행하면 적절한 디렉토리에 비밀키 `id_rsa` 와 공개키 `id_rsa.pub` 가 생성됩니다. 공개키를 코그넷나인 GitLab 계정에 등록합니다. 구체적인 과정은 https://docs.gitlab.com/ee/user/ssh.html#see 에서 모두 확인할 수 있습니다.

최종 디렉토리 구조는 아래와 같은 형태가 됩니다.

```
dockerfiles
├── develop
│   ├── Dockerfile
│   ├── id_rsa
│   ├── id_rsa.pub
│   ├── pretrained
│   │   ├── dbnet_resnet18_fpnc_20e_aihubfinance10of100_sparkling-cloud-104.pth
│   │   ├── dbnet_resnet18_fpnc_2e_aihubtransit100of100_hopeful-leaf-117.pth
│   │   ├── sar_resnet31_parallel-decoder_100e_aihubtransit1of100_pretrained_stilted-grass-112.pth
│   │   ├── sar_resnet31_parallel-decoder_500e_aihubfinance1of100_pretrained_zesty-sun-97.pth
│   │   ├── satrn_shallow_5e_aihubfinance10of100_pretrained_lrtune_peachy-sun-152.pth
│   │   └── satrn_shallow_5e_aihubtransit1of100_pretrained_lrtune_desert-sunset-150.pth
│   ├── run_finance.sh
│   ├── run_script.sh
│   └── run_transit.sh
├── nvidia
├── publish
├── pytorch
└── ssh
```