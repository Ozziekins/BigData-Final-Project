#!/bin/bash

echo "Number beers, Brewery name" > output/q1.csv
cat /root/q1/* >> output/q1.csv

echo "Brewers with 1 beer" > output/q2.csv
cat /root/q2/* >> output/q2.csv

echo "Beer id, Beer name, Average review" > output/q3.csv
cat /root/q3/* >> output/q3.csv

echo "Beer id, Beer name, Beer abv, Beer style, Brewer id" > output/q4.csv
cat /root/q4/* >> output/q4.csv

echo "Beer id, Beer name, Beer abv, Beer style, Brewer id" > output/q5.csv
cat /root/q5/* >> output/q5.csv

echo "Beer id, Beer name, Average total review" > output/q6.csv
cat /root/q6/* >> output/q6.csv

echo "Beer appearance, Count" > output/q7.csv
cat /root/q7/* >> output/q7.csv

echo "Beer aroma, Count" > output/q8.csv
cat /root/q8/* >> output/q8.csv

echo "Beer total, Count" > output/q9.csv
cat /root/q9/* >> output/q9.csv

echo "Beer taste, Count" > output/q10.csv
cat /root/q10/* >> output/q10.csv

echo "Beer palate, Count" > output/q11.csv
cat /root/q11/* >> output/q11.csv

echo "Profile name, Year, Number of reviews" > output/q14.csv
cat /root/q14/* >> output/q14.csv

echo "Profile name, Month, Number of reviews" > output/q15.csv
cat /root/q15/* >> output/q15.csv