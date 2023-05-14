START TRANSACTION; 
 
CREATE TABLE Person ( 
    id serial PRIMARY KEY, 
    ProfileName varchar(255) NOT NULL  
); 
 
CREATE TABLE Beer( 
    id integer not null primary KEY, 
    name varchar(255) not null, 
    abv decimal, 
    style text, 
    brewerId integer 
); 
 
CREATE TABLE Review(  
    id serial PRIMARY KEY,    
    appearance decimal, 
    aroma decimal, 
    palate decimal, 
    taste decimal, 
    time timestamp, 
    total decimal, 
    beerId integer, 
    reviewerId integer
); 
 
Create TABLE Brewer(   
    id integer not null primary KEY,
    brewery_name text   
); 
 
ALTER TABLE Beer ADD CONSTRAINT fk_beer_brewer_brewerId FOREIGN KEY(brewerId) REFERENCES Brewer (id); 
 
ALTER TABLE Review ADD CONSTRAINT fk_beer_review_beerId FOREIGN KEY(beerId) REFERENCES Beer(id); 
 
ALTER TABLE Review ADD CONSTRAINT fk_person_review_reviewerId FOREIGN KEY(reviewerId) REFERENCES Person(id); 
 
CREATE TEMP TABLE temp(
    brewery_id text,
    brewery_name text,
    review_time text,
    review_overall text,
    review_aroma text,
    review_appearance text,
    review_profilename text,
    beer_style text,
    review_palate text,
    review_taste text,
    beer_name text,
    beer_abv text,
    beer_beerid text
);

\COPY temp FROM '../data/beer_reviews.csv' DELIMITER ',' CSV HEADER NULL AS 'null';

INSERT INTO Brewer (id, brewery_name)
SELECT DISTINCT (brewery_id)::integer, brewery_name
FROM temp;

INSERT INTO Person (ProfileName)
SELECT DISTINCT review_profilename
FROM temp;

INSERT INTO Beer (id, name, abv, style, brewerId)
SELECT DISTINCT (beer_beerid)::integer, beer_name, cast(nullif(beer_abv, '') AS decimal), beer_style, (brewery_id)::integer
FROM temp;

INSERT INTO Review (appearance, aroma, palate, taste, time, total, beerId, reviewerId)
SELECT DISTINCT (review_appearance)::decimal, (review_aroma)::decimal, (review_palate)::decimal, (review_taste)::decimal, to_timestamp(cast(review_time as bigint)), (review_overall)::decimal, (beer_beerid)::integer, id
FROM temp
JOIN Person ON temp.review_profilename = Person.ProfileName;

DROP TABLE temp;

Commit;

SELECT * FROM Brewer;
SELECT * FROM Person;
SELECT * FROM Beer;
SELECT * FROM Review;