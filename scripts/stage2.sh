#!/bin/bash 
hdfs dfs -mkdir -p /project/avsc 
 
hdfs dfs -put /project/avsc/*.avsc /project/avsc 
 
hive -f ../hql/db.hql > ../hql/hive_results.txt 
 
hive -f ../hql/queries.hql 
 
 
mkdir ../output 
 
bash outputs.sh 
 
mkdir ../clean_output