USE projectdb;

-- Get the number of beers for top 10 brewers
INSERT OVERWRITE LOCAL DIRECTORY '/root/q1' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT COUNT(*) as num_beers, brewer.brewery_name FROM beer
JOIN brewer ON beer.brewerId = brewer.id
GROUP BY beer.brewerId, brewer.brewery_name
ORDER BY num_beers DESC
LIMIT 10;

-- Get the number of brewers that produced only 1 beer
INSERT OVERWRITE LOCAL DIRECTORY '/root/q2' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT COUNT(t1.brewerId)
FROM (SELECT brewerId FROM beer
GROUP BY brewerId
HAVING COUNT(*) = 1) t1;

-- Get the beers that have above average overall review
INSERT OVERWRITE LOCAL DIRECTORY '/root/q3' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT b.id AS beerid, b.name, AVG(r.total) AS avg_total
FROM beer b
JOIN review r ON b.id = r.beerId
JOIN (
  SELECT AVG(total) AS avg_total
  FROM review
) t1
WHERE r.total > t1.avg_total
GROUP BY b.id, b.name;

-- Get beer with highest abv; Get beer with least abv
INSERT OVERWRITE LOCAL DIRECTORY '/root/q4' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT * FROM beer WHERE abv IN (SELECT MIN(b1.abv) FROM beer AS b1);

INSERT OVERWRITE LOCAL DIRECTORY '/root/q5' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT * FROM beer WHERE abv IN (SELECT MAX(b1.abv) FROM beer AS b1);

--  Get styles of top 10 highest reviewed beers
INSERT OVERWRITE LOCAL DIRECTORY '/root/q6' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT beer.id, beer.name, AVG(r1.total) AS avg_total_review FROM beer
JOIN review AS r1 ON beer.id = r1.beerId
GROUP BY beer.id, beer.name
ORDER BY avg_total_review DESC
LIMIT 10;

-- Get aroma, taste, appearance and palate of 5
INSERT OVERWRITE LOCAL DIRECTORY '/root/q7' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT appearance, COUNT(*) FROM review GROUP  BY appearance;

INSERT OVERWRITE LOCAL DIRECTORY '/root/q8' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT aroma, COUNT(*) FROM review GROUP  BY aroma;

INSERT OVERWRITE LOCAL DIRECTORY '/root/q9' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT total, COUNT(*) FROM review GROUP  BY total;

INSERT OVERWRITE LOCAL DIRECTORY '/root/q10' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT taste, COUNT(*) FROM review GROUP  BY taste;

INSERT OVERWRITE LOCAL DIRECTORY '/root/q11' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT palate, COUNT(*) FROM review GROUP  BY palate;

-- Get users that reviewed a particular beer;
INSERT OVERWRITE LOCAL DIRECTORY '/root/q12' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT beer.name, collect_list(person.profileName) AS reviewers
FROM review
JOIN beer ON beer.id = review.beerId
JOIN person ON person.id = review.reviewerId
GROUP BY beer.name;

-- Get timestamp over overall time of top 5 users with most activity
INSERT OVERWRITE LOCAL DIRECTORY '/root/q13' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT 
  profileName, 
  collect_list(time),
  collect_list(review.total),
  COUNT(*) AS num_reviews
FROM 
  person 
  JOIN review ON person.id = review.reviewerId 
GROUP BY 
  profileName
ORDER BY 
  num_reviews DESC;

-- Get number of reviews per year of top 5 active users
INSERT OVERWRITE LOCAL DIRECTORY '/root/q14' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT 
  person.profileName, 
  date_format(from_unixtime(CAST((r1.time / 1000) AS BIGINT)), 'yyyy') AS year,
  COUNT(*) AS num_reviews
FROM 
  person 
  JOIN review AS r1
  ON person.id = r1.reviewerId 
GROUP BY 
  person.profileName,
  date_format(from_unixtime(CAST((r1.time / 1000) AS BIGINT)), 'yyyy')
ORDER BY 
  num_reviews DESC;

-- Get beer reviews over time for a particular beer (maybe the most reviewed and least reviewed beers)
INSERT OVERWRITE LOCAL DIRECTORY '/root/q15' ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT 
  b.name,
  date_format(from_unixtime(CAST((r.time / 1000) AS BIGINT)), 'yyyy-MM') AS month,
  COUNT(*) AS num_reviews
FROM 
  review AS r
  JOIN beer AS b
  ON b.id = r.beerId
GROUP BY 
  b.name,
  date_format(from_unixtime(CAST((r.time / 1000) AS BIGINT)), 'yyyy-MM')
ORDER BY
  num_reviews DESC;