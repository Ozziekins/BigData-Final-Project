SET hive.execution.engine=mr;

USE projectdb;

DROP TABLE IF EXISTS review_part;
DROP TABLE IF EXISTS beer_part;
DROP TABLE IF EXISTS brewer_part;
DROP TABLE IF EXISTS person_part;

SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

-- CREATE EXTERNAL TABLE beer_part(id int, name varchar(255), abv decimal(5,2),  style varchar(50))
-- PARTITIONED BY (brewerId int) STORED AS AVRO LOCATION '/project/beer_part' TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- INSERT INTO beer_part partition (brewerId) SELECT * FROM beer;

-- CREATE EXTERNAL TABLE brewer_part(brewery_name varchar(255))
-- PARTITIONED BY (id int) STORED AS AVRO LOCATION '/project/brewer_part' TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- INSERT INTO brewer_part partition (deptno) SELECT * FROM brewer;

-- CREATE EXTERNAL TABLE person_part(ProfileName varchar(255))
-- PARTITIONED BY (id int) STORED AS AVRO LOCATION '/project/person_part' TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- INSERT INTO person_part partition (deptno) SELECT * FROM person;

-- CREATE EXTERNAL TABLE review_part(id int, appearance decimal(2,2), aroma decimal(2,2), palate decimal(2,2), taste decimal(2,2), timestamp date, total decimal(2,2), beerId int)
-- PARTITIONED BY (reviewerId int) STORED AS AVRO LOCATION '/project/review_part' TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- INSERT INTO review_part partition (reviewerId) SELECT * FROM review;

SET hive.execution.engine=tez;