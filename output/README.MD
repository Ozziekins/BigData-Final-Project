# Output

This folder contains the output files generated from executing the queries in the `hql/queries.hql` script. The queries are designed to perform exploratory data analysis (EDA) on the dataset and extract useful insights and information. Each query corresponds to a specific analysis or investigation task.

### Folder Structure
The output folder contains 19 CSV files (`q1.csv` - `q19.csv`) corresponding to the results of the queries mentioned above. Each file contains the query result data in a comma-separated format.

To access the query results, navigate to the output folder and open the respective CSV file.

Please note that the CSV files may be overwritten each time the queries are executed, so it is recommended to make a backup of the files if you need to preserve previous results.

### Files Descriptions
- `q1.csv`: **Number of Beers for Top 10 Brewers** - This query retrieves the number of beers produced by the top 10 brewers based on the count of beers associated with each brewer. The results are ordered in descending order by the number of beers produced.

- `q2.csv`: **Number of Brewers with Only 1 Beer** - This query calculates the count of brewers who have produced only one beer. It identifies brewers with a single beer by grouping the dataset by brewerId and counting the occurrences. Brewers with only one beer are selected, and the count is returned.

- `q3.csv`: **Average Total Review** - This query calculates the average total review score across all reviews in the dataset. It provides an overall measure of the review scores' central tendency.

- `q4.csv`: **Beers with Above Average Overall Review** - This query retrieves the beers that have an overall review score higher than the average total review score. It joins the beer, brewer, and review tables to obtain the beer details, average total review scores, and brewery information.

- `q5.csv`: **Minimum ABV (Alcohol By Volume)** - This query finds the beer with the minimum ABV value (Alcohol By Volume) by selecting the beer with the smallest ABV value from the beer table.

- `q6.csv`: **Maximum ABV (Alcohol By Volume)** - This query identifies the beer with the maximum ABV value (Alcohol By Volume) by selecting the beer with the highest ABV value from the beer table.

- `q7.csv`: **Styles of Top 10 Highest Reviewed Beers** - This query retrieves the beer styles of the top 10 beers with the highest average review scores. It calculates the average review score for each beer and selects the top 10 beers based on the average review scores.

- `q8.csv`: **Number of Reviews per Beer Appearance Score** - This query counts the number of reviews for each distinct beer appearance score in the dataset. It groups the reviews by appearance score and calculates the count of occurrences.

- `q9.csv`: **Number of Reviews per Beer Aroma Score** - This query calculates the count of reviews for each distinct beer aroma score in the dataset. It groups the reviews by aroma score and counts the occurrences.

- `q10.csv`: **Number of Reviews per Beer Total Score** - This query counts the number of reviews for each distinct beer total score in the dataset. It groups the reviews by total score and calculates the count of occurrences.

- `q11.csv`: **Number of Reviews per Beer Taste Score** - This query calculates the count of reviews for each distinct beer taste score in the dataset. It groups the reviews by taste score and counts the occurrences.

- `q12.csv`: **Number of Reviews per Beer Palate Score** - This query counts the number of reviews for each distinct beer palate score in the dataset. It groups the reviews by palate score and calculates the count of occurrences.

- `q13.csv`: **Users Who Reviewed a Particular Beer** - This query retrieves the list of users who reviewed a specific beer. It collects the profileName of the users who reviewed each beer by joining the review, beer, and person tables.

- `q14.csv`: **Timestamp Over Overall Time of Top 5 Active Users** - This query obtains the timestamp and overall review scores over time for the top 5 active users. It retrieves the profileName, timestamps, and review scores of the reviews made by each user, and groups the results by profileName.

- `q15.csv`: **Number of Reviews per Year of Top 5 Active Users** - This query calculates the count of reviews per year for the top 5 active users. It retrieves the profileName, year, and count of reviews for each user, and groups the results by profileName and year.

- `q16.csv`: **Beer Reviews Over Time for a Particular Beer** - This query generates the number of reviews per month for a specific beer. It retrieves the beer name, month, and count of reviews by joining the review and beer tables and grouping the results by beer name and month.

- `q17.csv`: **Average Rating of Beers by ABV** - This query calculates the average rating of beers based on their ABV (Alcohol By Volume) values. It retrieves the ABV and average review rating for each beer by joining the beer and review tables and grouping the results by ABV.

- `q18.csv`: **Top-Rated Beers by Style** - This query identifies the top-rated beers for each beer style. It selects the beer with the highest review score within each beer style based on the ranking generated using the ROW_NUMBER() function.

- `q19.csv`: **Breweries Mentioned Most Often in Positive Reviews** - This query determines the breweries that are mentioned most frequently in positive reviews. It calculates the count of mentions for each brewery in reviews with a total score greater than 4.0.

