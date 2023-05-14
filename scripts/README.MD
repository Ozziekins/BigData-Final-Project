# Scripts 
This folder contains various scripts that are utilized throughout the different stages of our project. These scripts automate specific tasks, such as data preprocessing, post-processing, and executing different stages of our project pipeline.

### File Structure
- `outputs.sh`: This script retrieves the results of the queries specified in the hql/queries folder and concatenates them into a single CSV file for each of the 19 queries then stores it in the `output` folder.
- `postprocess.sh`: This script handles the post-processing steps, such as cleaning up temporary files, organizing outputs, and generating reports or visualizations based on the project's requirements.
- `preprocess.sh`: This script facilitates the data preprocessing tasks, including data cleaning, filtering, transformation, and any necessary data preparation steps required before feeding the data into subsequent stages of the project.
- `stage1.sh`: This script executes the necessary commands for Stage 1 - Data Collection and Ingestion, which involve creating the project database, importing dataset CSV files, and setting up the initial database structure.
- `stage2.sh`: This script encompasses the tasks for Stage 2 - Exploratory Data Analysis (EDA), where it runs queries or analysis on the dataset to gain insights and understand the data characteristics, distributions, correlations, and other relevant information.
- `stage3.sh`: This script handles the tasks for Stage 3 - Predictive Data Analytics (PDA), which involves building machine learning models, performing hyperparameter tuning, evaluating model performance, and generating predictions or recommendations based on the data.
- `stage4.sh`: This script covers the tasks for Stage 4 - Reporting and Visualization, where it generates reports, visualizations, or interactive dashboards to communicate the project findings and insights effectively.

### Usage
To utilize these scripts effectively, follow the steps below:

1. Ensure that the necessary dependencies, tools, and libraries are installed and configured according to the project's requirements.
2. Review and modify the script files if needed, considering any specific configurations, file paths, or environment variables relevant to your setup.
3. The scripts can be executed by running `main.sh` in the root directory of the repo to ensure a smooth progression and successful execution.

> Note: Make sure to grant appropriate permissions (e.g., execute permissions) to the script files before running them.