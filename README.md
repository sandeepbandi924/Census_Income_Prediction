# END to End Census Income Predcition - Sandeep Bandi

## Problem Statement:
- The Goal is to predict whether a person has an income of more than 50K a year or not.
- This is basically a binary classification problem where a person is classified into the
  >50K group or <=50K group.

## Introduction About the Data

Prediction task is to determine whether a person makes over 50K a year. (Classification problem)

There are 14 Independent Variables.
- age: continuous.
- workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- fnlwgt: continuous.- education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate 5th-6th, Preschool.
- education-num: continuous.
- marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct,Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.- sex: Female, Male.
- capital-gain: continuous.
- capital-loss: continuous.
- hours-per-week: continuous.
- native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

Target Varibale:
- income: >50K, <=50K.

Dataset Source Link : https://archive.ics.uci.edu/ml/datasets/census+income

## Approach of the project

1. Data Ingestion :
   * In Data Ingestion phase the data is first read as csv.
   * Then the data is split into training and testing and saved as csv file.

2. Data Transformation :
   * In this phase a ColumnTransformer Pipeline is created.
   * for Numeric Variables first SimpleImputer is applied with strategy median ,then Standard Scaling is performed on numeric data.
   * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
   * This preprocessor is saved as pickle file.

3. Model Training :
   * In this phase base model is tested . The best model found was Logistic Regression.
   * This model is saved as pickle file.

4. Prediction Pipeline :
   * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation :
   * Flask app is created with User Interface to predict the Census Income price wheather <=50K or >50K inside a Web Application.

# EDA Notebbok:

Link: [EDA Notebook](./notebook/EDA.ipynb)

# Model Traing Approach Notebook:

Link: [Model training Notebook](./notebook/model_trainer.ipynb)

# Deployment:

## AWS Deployment link:

AWS ELastic Beanstalk link: [http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/](http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/)
