# 🧱 Order-He 이커머스 데이터 파이프라인 구축 프로젝트
### AWS와 Python을 활용하여 데이터 파이프라인부터 BI까지 직접 구축해보는 실무형 프로젝트  

---

## 1. 프로젝트 개요

본 프로젝트는 가상의 이커머스 서비스 ‘Order-He’의 주문데이터를 관리 하기 위한 데이터 저장소(RDS, DW)와 마트(DM)를 생성 하여 BI툴로 대시보드를 제작합니다.
  + 이 프로젝트는 데이터 엔지니어링을 처음 배우는 학습자가 실무 수준의 파이프라인을 직접 구현해보는 것을 목적으로 합니다.

- **목적**: 체계적인 서비스 데이터 운영을 위한 데이터 저장소와 마트를 생성 관리하기 위한 코드 제작, 재사용을 고려한 폴더 구조화를 진행함

### 주요 기술 스택

- **Python 3.10**, **SQL(mysql, postgresql)**
  - 라이브러리 : `pymysql`, `yaml`, `pandas`
- **AWS 기능**
  - **AWS Redshift (Serverless)**
  - **AWS S3**

---

## 2. 📁 프로젝트 구조

```text
project_for_data_pipeline/
│
├── config/ # 데이터베이스 설정 및 쿼리 저장
│ ├── db_info.yml # DB 연결 정보 (예: host, dbname, user 등)
│ ├── sql_queries.py # 테이블 생성 등 SQL 쿼리 모음
│
├── data/ # 데이터 파일 저장 폴더 (CSV 등)
│
├── scripts/ # 실행 스크립트 폴더
│ ├── create_db_and_tables.py # DB 및 테이블 생성 스크립트
│
├── utils/ # 유틸 함수 모음
│ ├── db_helper.py # Redshift 연결 및 쿼리 실행 유틸
│
│
├── main.ipynb # 프로젝트 메인 노트북
├── README.md # 영어 README
├── README.ko.md # 한글 README
```
**github에 config/db_info는 민감한 정보임으로 업로드하지 않았으나 기록을 위해 프로젝트 구조에 포함하였음

---

## 3. 데이터 파이프라인 흐름 구조 요약

**전체 데이터 파이프라인 흐름 요약**:
[data_pipeline](images/data_pipeline_chart_ver1.png)

```text
[AWS RDS workpage 생성] → [Python으로 ETL 처리] → [S3로 백업] → [AWS Redshift 데이터 웨어하우스 생성 & 데이터 복사] → [AWS Redshift 데이터 마트용 데이터 저장] 
```

---

## 4. 구현 단계 (Step-by-Step) [작업 도구]

### 1단계: [AWS] AWS Redshift 웨어하우스 생성

- AWS 콘솔에서 **Serverless Redshift 인스턴스**를 생성합니다.
- Tip. 연결 정보(`host`, `dbname`, `user`, `password` 등)를 ymal형식으로 별도 저장하여 보완성을 높임

---

### 2단계: [VScode] Python으로 Redshift 연결

- `pymysql` 라이브러리를 이용해 Python에서 Redshift로 연결합니다.

- 연결용 python코드 예시
```python
import pymysql

conn = pymysql.connect(
    host="your-host-name",
    dbname="dev",
    user="your-username",
    password="your-password",
    port="5439"
)
cur = conn.cursor()
```

---

### 3단계: [VScode] 테이블 생성 (order, customer, product)

각 테이블은 SQL로 생성합니다. 아래는 `order` 테이블 예시입니다.  

```python
CREATE TABLE order (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    amount INT
);
```
- `customer`, `product` 테이블도 유사한 방식으로 생성합니다.

---

### 4단계: [VScode] 데이터 적재 (CSV → Redshift)

`pandas`를 이용해 로컬 CSV 파일을 읽고, (혹은 딕셔너리 형태로 저장된 데이터셋을 data/initial_data.py에서 불러와서 사용)  
`insert` 쿼리 또는 `COPY` 명령을 통해 Redshift로 데이터를 적재합니다.

---

### 5단계: [AWS] AWS S3로 데이터 백업 전송

적재한 데이터 혹은 원본 CSV 파일을 S3 버킷으로 업로드합니다.

---

### 6단계: [AWS] 데이터 마트 생성 및 저장

Redshift 내 SQL을 활용하여 요약 테이블(Data Mart)을 생성합니다.  
- order테이블을 기준으로 customer, product테이블을 병합하여 저장합니다.

---

### 7단계 : [Looker Studio] BI툴을 활용하여 대시보드 제작
[Dashboard_looker studio](images/looker_studio_dashboard.PNG)
`Looker Studio`에 Redshift의 데이터 마트를 연결하여 대시보드를 제작합니다.

---

## 5. 🧨 프로젝트 실습 중 발생한 주요 오류 정리

### 1️⃣ RDS 접속 실패 – 보안 그룹 설정 누락

- **에러 상황**:  
  Python에서 RDS(MySQL) 연결 시 연결 불가

- **에러 메시지 예시**:  
```text
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server...")
```

- **원인**:  
RDS 인스턴스의 보안 그룹(Inbound Rules)에 현재 내 IP가 허용되지 않음

- **해결 방법**:  
1. RDS 콘솔 → 인스턴스 클릭 → VPC Security Group 확인  
2. 보안 그룹 → Inbound Rules → 규칙 추가  
   - Type: MySQL/Aurora  
   - Port: 3306  
   - Source: 내 IP 주소 또는 `0.0.0.0/0`  
3. 저장 후 Python 연결 재시도

---

### 2️⃣ S3 → Redshift COPY 실패 – IAM Role 권한 부족

- **에러 상황**:  
Query Editor에서 COPY 명령 실행 시 권한 오류 발생

- **에러 메시지 예시**:  
```text
AmazonS3: Access Denied
```

- **원인**:  
Redshift Serverless에 연결된 IAM Role이 S3에 접근할 수 있는 권한이 없음

- **해결 방법**:  
1. AWS 콘솔 → IAM → Roles  
2. Redshift에서 사용하는 IAM Role 선택  
3. [Add permissions] → 정책 검색: `AmazonS3ReadOnlyAccess`  
4. 정책 추가 후, Redshift에서 COPY 재시도

---

### 3️⃣ BI툴에서 Redshift 연동 실패 – Serverless 퍼블릭 접근 제한

- **에러 상황**:  
Metabase, Looker Studio 등 외부 BI툴에서 Redshift 접속 시도 → 실패

- **에러 메시지 예시**:  
연결 시도 시 타임아웃, 인증 실패 등

- **원인**:  
Redshift Serverless는 기본적으로 퍼블릭 네트워크 접근이 차단됨

- **해결 방법 (우회)**:  
1. Redshift Query Editor에서 데이터를 SELECT 후 CSV로 저장  
2. BI툴(Metabase, Looker Studio 등)에 CSV 파일 직접 업로드  
3. 시각화 진행은 CSV 기반으로 진행

- **추가 팁**:  
퍼블릭 접근을 가능하게 하려면 VPC, IAM, 보안 그룹 등 복잡한 설정이 필요함 → 실습 목적이라면 CSV 연동이 현실적인 대안

---

## 6. 부록

- **작성자**: DS_Yujin LEE  
- **프로젝트 기간**: 2025-04-28 ~ 2025-05-03  
- **개발 환경**: Python 3.10, AWS Redshift Serverless, Jupyter Notebook  
- **사용 데이터**: 파이썬 코드를 활용한 랜덤 생성 데이터
