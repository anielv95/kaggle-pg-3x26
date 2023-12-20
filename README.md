# Kaggle - Playground Series - Multi-Class Prediction of Cirrhosis Outcomes

## Problem Description

This solution is for the Kaggle Playground Series Competition https://www.kaggle.com/competitions/playground-series-s3e26/overview and the purpose is to predict a categorical feature called "Status". In that feature there are three categories, C, CL and D, the proportion for those can be viewed in notebooks/eda.ipynb notebook.

The metric used to evaluate the performance is cross-entropy loss https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html. 

## Deploying model

The deployment is made with flask in a docker container with all the dependencies, to deploy de container in Linux you need:

1. Docker engine
2. Docker-compose

If you're a windows user you just need:

1. Docker Desktop

After that requirement matched you just need to execute inside the repository folder at the same path of docker-compose.yml file:

1. docker-compose up

## Setting environment

If you want to execute the notebooks/eda.ipynb notebook you need to create a virtual environment and then install the packages, for Linux:

1. python3 -m virtualenv my_virtual_environment_name
2. source ./my_virtual_environment_name/bin/activate
3. pip install -r requirements.txt

For windows users:

1. python -m virtualenv my_virtual_environment_name
2. .\my_virtual_environment_name\Scripts\Activate
3. python -m pip install -r requirements.txt