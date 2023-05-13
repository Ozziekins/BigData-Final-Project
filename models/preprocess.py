from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
import sys
from pyspark.sql.types import DecimalType
from pyspark.sql.functions import col, unix_timestamp, from_unixtime, month, translate

reload(sys)

sys.setdefaultencoding('utf-8')

spark = SparkSession.builder\
        .appName("BDT Project")\
        .config("spark.sql.catalogImplementation","hive")\
        .config("hive.metastore.uris", "thrift://localhost:9083")\
        .config("spark.sql.avro.compression.codec", "snappy")\
        .enableHiveSupport()\
        .getOrCreate()


sc = spark.sparkContext
print("Created Spark context")

print(spark.catalog.listDatabases())

# print(spark.catalog.listTables("projectdb"))

beer = spark.read.format("avro").table('projectdb.beer_buck')
beer.createOrReplaceTempView('beer_buck')

brewer = spark.read.format("avro").table('projectdb.brewer_buck')
brewer.createOrReplaceTempView('brewer_buck')

person = spark.read.format("avro").table('projectdb.person_buck')
person.createOrReplaceTempView('person_buck')

review = spark.read.format("avro").table('projectdb.review_buck')
review.createOrReplaceTempView('review_buck')

print("Tables all loaded")




beer = beer.withColumn('name', translate("name","'",""))\
    .withColumn('style', translate("style","'",""))\
    .withColumn('abv', col('abv').cast(DecimalType()))

print("Formatted beer table")


brewer = brewer.withColumn('brewery_name', translate("brewery_name","'",""))
print("Formatted brewery table")

person = person.withColumn('profilename', translate("profilename","'",""))
print("Formatted person table")

review = review.withColumn('appearance', col('appearance').cast(DecimalType()))\
.withColumn('aroma', col('aroma').cast(DecimalType()))\
.withColumn('palate', col('palate').cast(DecimalType()))\
.withColumn('taste', col('taste').cast(DecimalType()))\
.withColumn('total', col('total').cast(DecimalType()))\
.withColumn('month', month('time'))

print("Formatted review table")