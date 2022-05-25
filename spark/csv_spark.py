from pyspark.sql.functions import col

spark = SparkSession.builder.master("local").appName("SparkSQL").getOrCreate()

# csv 불러오기
df = spark.read.option("header", True).option("encoding","utf-8").csv("/spark-work/model/prepro_total_cr_naver.csv")
# df 확인
df.show()

# 5행만 가지고 테스트
df.createOrReplaceTempView("test")
tmp=spark.sql("SELECT * FROM test LIMIT 5")
# 5행만 보기
tmp.show()

# 파일 추가하기
sc.addFile("/spark-work/model/QA.py")
import QA as qa

# return 값이 정수형으로 나오는 predict 함수를 udf
qa_udf = udf(lambda x: qa.predict(x), IntegerType())

#5행만 있는 tmp에 적용해서 보기
tmp.withColumn("qa_score", qa_udf(col('comment'))).show()
