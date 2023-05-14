# SQL
This folder contains the necessary SQL file for the Stage I - Data Collection and Ingestion of our project. The db.sql file included here contains SQL statements for creating the project database, defining table schemas, and importing the dataset CSV file into the respective tables.

### File Structure
- `db.sql`: This SQL file contains the necessary commands for creating tables (Person, Beer, Review, Brewer) and importing the dataset into the tables. It also includes statements for defining primary keys and foreign key constraints.

### Usage
To set up the project database and import the dataset, follow these steps:

1. Make sure you have a compatible SQL server or database management system installed.
2. Create a new database for the project
    - `psql -U postgres -c 'DROP DATABASE IF EXISTS project;'`
    - `psql -U postgres -c 'CREATE DATABASE project;'`
    - `c project;`
3. Open the db.sql file in a SQL editor or query tool.
4. Run the SQL statements in the db.sql file in the specified order to create the required tables and import the dataset into the database.
    - `psql -U postgres -d project -f sql/db.sql`
5. Ensure that the dataset file (beer_reviews.csv) is accessible and located in the appropriate directory referenced in the SQL statements.

### Database Schema
The db.sql file creates the following tables with their respective columns:

- `Person`: Stores information about individuals who provided reviews. It has columns for id (primary key) and ProfileName.
- `Beer`: Contains details about different beers, including columns for id (primary key), name, abv, style, and brewerId.
- `Review`: Stores information about the beer reviews, including columns for id (primary key), appearance, aroma, palate, taste, time, total, beerId (foreign key referencing Beer table), and reviewerId (foreign key referencing Person table).
- `Brewer`: Contains information about the brewers, including columns for id (primary key) and brewery_name.

### Note
Please review and modify the SQL statements in the db.sql file based on your specific SQL server or database management system requirements, such as syntax differences or any additional configurations needed.