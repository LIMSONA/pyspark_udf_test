# pyspark_udf_test

* Ubuntu18.04 Spark3.1.2 환경에서 pyspark udf test를 위해 필요한 data

┌ model/
│  ├ .cache/ : pyspark에서 분석 모델을 불러오면서 생기는 캐시
│  ├ .gitignore : 분석 모델 캐시
│  ├ prepro_toal_cr_naver.csv : 정규식 전처리된 네이버라이브커머스 데이터
│  ├ QA.pt : kobert pytorch 질문분류 가중치 모델 
│  └ QA.py : udf로 적용할 모델 실행 py파일
├ spark/
│  ├ csv_spark.py : 디렉토리에 있는 csv 데이터를 가져와 분석모델 적용하고 확인
│  ├ Dockerfile : ubuntu18.04 & cuda 11.4 base이미지 & spark 3.1.2 & python 3.8.5 
│  ├ entrypoint.sh : 스파크 master/worker의 host,port env
│  ├ kafka_spark.py : kafka에 쌓이는 json 데이터를 가져와 dataframe화 시키고 분석모델 적용하는 py파일
│  ├ requirements.txt : 데이터 분석시 사용한 라이브러리 및 버젼 
│  └ spark-sql-kafka-0-10_2.12-3.2.1.jar : pyspark SQL 사용 시 필요한 jar파일
├ build-spark.sh : spark 이미지 빌드 및 docker-compose 컨테이너 띄우기
├ docker-compose-spark.yml : 스파크 마스터, 워커3 docker-compose
├ README.md : pyspark_udf_test 안내
└ run-spark.sh : 도커 컨테이너 실행 및 접속

1. 네이버 크롤링 data
2. 필요한 패키지가 담긴 reaquirement.txt
3. udf로 추가할 모델분석 .py파일
4. 가중치 저장된 파이토치 .pt파일
