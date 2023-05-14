# Models
This folder contains various scripts and modules related to the models used in our project. It includes implementations of machine learning algorithms, data services, and utilities to train, load, and utilize the models effectively.

### File Structure
- `__init__.py`: This file is empty and is included to mark the folder as a Python package.
- `alsmodel.py`: This module contains the implementation of the ALS (Alternating Least Squares) model for collaborative filtering. It includes functions for training the model, saving and loading the trained model, and making predictions based on the trained model.
- `BRPKNN.py`: This module implements the BRP-KNN (Bucketed Random Projection with K-Nearest Neighbors) model for item-based recommendation. It provides functions for training the model, loading the trained model and pipeline, and finding nearest neighbors based on the trained model.
- `DataService.py`: This module defines the DataService class, which handles data-related operations and provides access to the datasets used in the project. It includes functions for loading and preprocessing the data, as well as creating Spark views for easy querying.
definitions.py: This module defines the ROOT_DIR constant, which represents the root directory of the project. It is used to specify file paths and ensure portability across different environments.
- `ModelService.py`: This module implements the ModelService class, which acts as a central service for managing and utilizing the trained models. It provides functions for retraining the models, making predictions, and finding similar items or users based on the trained models.
- `SparkService.py`: This module defines the SparkService class, which handles the initialization of the SparkSession and provides the Spark context for the project. It ensures the proper configuration and setup of Spark for data processing and model training.

### Usage
To use the modules and scripts in this folder effectively, follow these steps:

1. Ensure that you have the necessary dependencies and libraries installed, such as Apache Spark and required Python packages.
2. Review the module files and modify them if needed, considering any specific configurations or environment variables relevant to your setup.
3. Utilize the functions and classes provided in the modules based on your project requirements.
4. Use the ModelService class to manage and utilize the trained models effectively, including retraining, making predictions, and finding similar items or users.
5. Leverage the DataService class to load and preprocess the datasets, providing access to the data for training and model evaluation.
6. Utilize the SparkService class to initialize the SparkSession and obtain the Spark context for data processing and model training.

> Note: Make sure to configure the necessary environment variables, file paths, or other settings based on your project's requirements.