SET hive.execution.engine=mr;

USE projectdb;

DROP TABLE IF EXISTS review_buck purge;
DROP TABLE IF EXISTS beer_buck purge;
DROP TABLE IF EXISTS brewer_buck purge;
DROP TABLE IF EXISTS person_buck purge;

SET hive.enforce.bucketing=true;

CREATE EXTERNAL TABLE review_buck(
    id int,
    appearance decimal(5,2), 
    aroma decimal(5,2), 
    palate decimal(5,2), 
    taste decimal(5,2), 
    time timestamp, 
    total decimal(5,2), 
    beerId int,
    reviewerId int
    ) 
    CLUSTERED BY (id) into 3 buckets
    STORED AS AVRO LOCATION '/project/review_buck' 
    TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

INSERT INTO review_buck SELECT id, cast(appearance as decimal(5, 2)), 
cast(aroma as decimal(5, 2)),cast(palate as decimal(5, 2)),
cast(taste as decimal(5, 2)), time,cast(total as decimal(5, 2)), beerId, reviewerId FROM review;

CREATE EXTERNAL TABLE beer_buck(
    id int, 
    name varchar(255),
    abv decimal(5,2),
    style varchar(50),
    brewerId int
) 
    CLUSTERED BY (id) into 3 buckets
    STORED AS AVRO LOCATION '/project/beer_buck' 
    TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

INSERT INTO beer_buck SELECT * FROM beer;

CREATE EXTERNAL TABLE brewer_buck(
    id int, 
    brewery_name varchar(255)
) 
    CLUSTERED BY (id) into 3 buckets
    STORED AS AVRO LOCATION '/project/brewer_buck' 
    TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

INSERT INTO brewer_buck SELECT * FROM brewer;

CREATE EXTERNAL TABLE person_buck(
    id int, 
    ProfileName varchar(255)
) 
    CLUSTERED BY (id) into 3 buckets
    STORED AS AVRO LOCATION '/project/person_buck' 
    TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

INSERT INTO person_buck SELECT * FROM person;

SET hive.execution.engine=tez;