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
            .config("spark.sql.catalogImplementation","hive")\
            .config("hive.metastore.uris", "thrift://localhost:9083")\
            .config("spark.sql.avro.compression.codec", "snappy")\
            .enableHiveSupport()\
            .getOrCreate()
        self.sc = self.spark.sparkContext