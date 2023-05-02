DROP DATABASE IF EXISTS projectdb CASCADE;


CREATE DATABASE projectdb;
USE projectdb;

SET mapreduce.map.output.compress = true;
SET mapreduce.map.output.compress.codec = org.apache.hadoop.io.compress.SnappyCodec;


-- beer table
CREATE EXTERNAL TABLE beer STORED AS AVRO LOCATION '/project/beer' TBLPROPERTIES ('avro.schema.url'='/project/avsc/beer.avsc');


-- brewer table
CREATE EXTERNAL TABLE brewer STORED AS AVRO LOCATION '/project/brewer' TBLPROPERTIES ('avro.schema.url'='/project/avsc/brewer.avsc');


-- person table
CREATE EXTERNAL TABLE person STORED AS AVRO LOCATION '/project/person' TBLPROPERTIES ('avro.schema.url'='/project/avsc/person.avsc');

-- review table
CREATE EXTERNAL TABLE review STORED AS AVRO LOCATION '/project/review' TBLPROPERTIES ('avro.schema.url'='/project/avsc/review.avsc');

SELECT * FROM brewer;
SELECT * FROM person;
SELECT * FROM beer;
SELECT * FROM review;