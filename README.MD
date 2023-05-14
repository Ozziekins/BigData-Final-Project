# Project Repository
Welcome to the project repository! This repository is for the final project of big data course in IU-2023. It contains various components and resources related to our beer review analysis project. Our goal is to leverage big data technologies and advanced analytics to gain insights from beer reviews and provide valuable information to beer enthusiasts, brewers, and businesses in the beer industry.

### Project Overview
Beer reviews offer a wealth of information about different beer styles, breweries, and user preferences. By analyzing and processing this data at scale, we can uncover patterns, trends, and recommendations that can enhance decision-making and improve the overall beer experience.

The main objective of this project is to build a comprehensive big data pipeline that ingests, processes, analyzes, and visualizes beer review data. The pipeline encompasses multiple stages, including data collection, data preprocessing, exploratory data analysis (EDA), predictive data analytics (PDA), and the development of machine learning models for recommendation systems.

### Business Goals
The project aims to achieve the following business goals:

1. Enhance Consumer Experience: By analyzing beer reviews, we can provide beer enthusiasts with personalized recommendations, insights into different beer styles, and overall beer quality assessments.
2. Empower Breweries and Businesses: Breweries can leverage the analysis of user preferences and trends to improve their offerings, optimize production, and refine marketing strategies. Additionally, businesses in the beer industry can gain valuable market insights to inform their decision-making processes.
3. Facilitate Data-Driven Decision Making: The big data pipeline allows stakeholders to make informed decisions based on comprehensive analyses of beer review data. This includes identifying popular beer styles, understanding consumer preferences, and predicting trends.

## Getting Started
To get started with the project, follow the instructions in the main README file, which provides an overview of the repository's structure and contents. The README files in each folder offer more specific guidance on running scripts, executing queries, and utilizing the provided resources. 

### Folder Structure
- `dashboard`: This folder contains the Streamlit dashboard application, which allows interactive visualization and exploration of the data.
- `data`: The data folder contains the dataset files used in our project.
- `hql`: The HQL folder includes Hive query scripts for data processing and analysis.
- `models`: This folder houses the machine learning models implemented in our project.
- `notebooks`: The notebooks folder contains Jupyter notebooks used for exploratory data analysis (EDA) and predictive data analytics (PDA).
- `output`: The output folder stores the output files generated from the Hive queries.
- `scripts`: This folder contains various scripts to assist with data processing, pre-processing, and training.
- `sql`: The SQL folder includes the db.sql file, which contains SQL statements for creating the database and importing the dataset CSV files into it.
- `.gitignore`: This file specifies which files and directories should be ignored by Git version control.
- `main.sh`: The main shell script provides a convenient way to execute different stages of the project pipeline.
- `presentation.pdf`: This file contains the slides for the video presentation to be made.
- `report.pdf`: This file contains the full report of the project.
- `requirements.txt`: This file lists the required Python packages and their versions for running the project.

## Collaborative Effort
This project is a collaborative effort from [@CodeSmith](https://github.com/AbdulmueezEmiola) and [@Ozziekins](https://github.com/Ozziekins) to put the practice all we have learnt in our Big Data Course and make use of big data technologies to gain valuable insights from beer review data.

**Important Note:** You cannot change the content of the script `main.sh` since it will be used for assessment purposes.

**Another Note:** The notebooks in `notebooks/` folder are used only for learning purposes since you need to put all Python scripts of the pipeline in `scripts/` folder. During the assessment, the grader can delete the folder `notebooks/` to check that your pipeline does not depend on its content.
