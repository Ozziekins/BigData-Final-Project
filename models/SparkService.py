from pyspark.sql import SparkSession
import sys

class SparkService:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SparkService, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        reload(sys)

        sys.setdefaultencoding('utf-8')

        self.spark = SparkSession.builder\
            .appName("BDT Project")\
            .master("local[*]")\
            .config("hive.metastore.uris", "thrift://sandbox-hdp.hortonworks.com:9083")\
            .config("spark.sql.catalogImplementation","hive")\
            .config("spark.sql.avro.compression.codec", "snappy")\
            .config("spark.jars", "file:///usr/hdp/current/hive-client/lib/hive-metastore-1.2.1000.2.6.5.0-292.jar,file:///usr/hdp/current/hive-client/lib/hive-exec-1.2.1000.2.6.5.0-292.jar")\
            .config("spark.jars.packages","org.apache.spark:spark-avro_2.12:3.0.3")\
            .enableHiveSupport()\
            .getOrCreate()
        self.sc = self.spark.sparkContext