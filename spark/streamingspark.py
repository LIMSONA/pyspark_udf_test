from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession, functions

spark = SparkSession.builder\
    .appName("kafka-to-spark")\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()

df = spark\
    .readStream\
    .format('kafka')\
    .option('kafka.bootstrap.servers', 'kafka:9092')\
    .option('subscribe', 'input')\
    .option("startingOffsets", "earliest")\
    .load()

df1 = df.selectExpr('CAST(value AS STRING) as value')

schema = StructType([\
StructField("video_unique",StringType(),True),\
StructField("num",IntegerType(),True),\
StructField("chat_time",StringType(),True),\
StructField("chat_id",StringType(),True),\
StructField("chat_message",StringType(),True),
])

df2= df1\
    .select(functions.from_json(functions.col("value").cast("string"),schema).alias("parse_value"))\
    .select("parse_value.video_unique","parse_value.num","parse_value.chat_time",
            "parse_value.chat_id","parse_value.chat_message")


df2\
.selectExpr("CAST('data' AS STRING) AS key", "to_json(struct(*)) AS value")\
.writeStream\
.format('kafka')\
.outputMode("Append")\
.option('kafka.bootstrap.servers', 'kafka:9092')\
.option('topic', 'message')\
.option("checkpointLocation", "/tmp/dtn/checkpoint")\
.start().awaitTermination()