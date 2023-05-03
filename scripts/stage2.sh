#!/bin/bash
hdfs dfs -put *.avsc ../project/avsc

hive -f ../hql/db.hql > ../hql/hive_results.txt

hive -f ../hql.queries.hql

sh outputs.sh