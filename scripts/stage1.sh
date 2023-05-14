#!/bin/bash 
psql -U postgres -f ../sql/db.sql 
 
wget https://jdbc.postgresql.org/download/postgresql-42.6.0.jar --no-check-certificate 
 
cp  postgresql-42.6.0.jar /usr/hdp/current/sqoop-client/lib/ 
 
mkdir ../project 
 
sqoop import-all-tables \ 
    -Dmapreduce.job.user.classpath.first=true \ 
    --connect jdbc:postgresql://localhost/project \ 
    --username postgres \ 
    --warehouse-dir /project \ 
    --as-avrodatafile \ 
    --compression-codec=snappy \ 
    --outdir /project/avsc \ 
    --m 1