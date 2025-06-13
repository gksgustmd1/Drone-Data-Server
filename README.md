# Drone-Data-Server

초기버전이라 추후 계속 기능 추가 예정

### 주요 기능 
1. DB 테이블 생성
2. 제품 license 값 생성
3. 장비의 라이센스 값과 서버에 등록된 라이센스 값 확인 후 펌웨어 파일 다운로드
4. 장비 로그 값 저장

---

### 환경 정보

- **OS**: Ubuntu 24.04 LTS (x86 아키텍처)

## 테스트 환경 준비 방법

### 필수 패키지 설치

```bash
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y
sudo apt install sqlite3
```

---

### root 계정으로 전환

```bash
sudo su
```

> Ubuntu 23버전부터는 `root` 계정에서 `pip install`을 권장하지 않기 때문에  
> **가상환경**을 만들어서 설치해야 합니다.

---

### 가상환경 만들기

```bash
python3 -m venv Flask-server
source Flask-server/bin/activate
```

- 프롬프트가 `(Flask-server)` 로 바뀌었는지 확인  
- `root` 옆에 `(Flask-server)`가 붙었다면 정상

---

### Flask, SQLAlchemy 설치

```bash
pip install flask flask_sqlalchemy
```

---

### 설치 확인

```bash
pip list | grep -i flask
```

> 예시 출력:
```text
Flask              3.1.1  
Flask-SQLAlchemy   3.1.1
```

## Drone-Data-Server 디렉토리 구조

```
Drone-Data-Server/
├── README.md                    # 프로젝트 개요 및 사용법 설명 문서
├── __pycache__/                 # Python이 자동 생성하는 바이트코드 캐시 디렉토리
├── check_license.py             # Flask 서버 메인 파일 (라이센스 검증, 로그 업로드 등 HTTP API 제공)
├── config.py                    # 데이터베이스 및 경로 등 설정을 담은 Flask Config 클래스
├── create_db.py                 # license.db SQLite 데이터베이스(license 테이블) 생성 스크립트
├── create_license.py            # 새로운 라이센스 정보를 DB에 삽입하는 유틸리티 스크립트
├── firmwares/                   # 장비가 다운로드할 펌웨어 파일이 저장되는 디렉토리
│   └── test.txt                 # 예제 펌웨어 파일 (또는 firmware.bin 등)
├── license.db                   # SQLite3로 만든 실제 라이센스 데이터베이스 파일
├── schema.py                    # SQLAlchemy 모델 정의 (License 클래스 등 포함)
└── start_check_license.sh       # 부팅 시 check_license.py를 자동으로 실행시키는 서비스 등록 파일 (가상환경 활성화 포함)
```

---

### Drone-log-data 디렉토리 구조

```
ABC123456789/  ← (가짜 데이터로 만든 라이센스 키)
```

해당 라이센스 키를 가지고 있는 임베디드 장비에서 `log` 파일을 보내게 되면  
해당 라이센스 키 값으로 디렉토리가 생성되며, 그 안에 `log` 파일이 저장됩니다.

```
Drone-log-data/
└── ABC123456789/
    ├── log_20250611_176628.txt
    └── log_20250611_176650.txt
```

### DB 컬럼 구조

| 컬럼 이름        | 자료형         | 제약 조건               | 설명                                   |
|------------------|----------------|--------------------------|----------------------------------------|
| `id`             | Integer        | PRIMARY KEY              | ID 자동 증가                           |
| `model`          | String(32)     | NOT NULL                 | 제품 모델명 (예: 정한 1호기)           |
| `serial`         | String(64)     | NOT NULL, UNIQUE         | 고유 라이센스 번호                    |
| `firmware_version` | String(16)   | NOT NULL                 | 펌웨어 버전 (예: v1.0.0, v1.1.0 등)    |
| `valid_until`    | Date           | NOT NULL                 | 유효 기간                              |
| `created_at`     | DateTime       | default=datetime.utcnow  | 등록된 시간 (자동 생성)               |


