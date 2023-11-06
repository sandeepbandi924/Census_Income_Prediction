# END to End Census Income Predcition

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
   * In this phase base model is tested . The best model found was Supoort vector classifier.
   * This model is saved as pickle file.

4. Prediction Pipeline :
   * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation :
   * Flask app is created with User Interface to predict the Census Income price wheather <=50K or >50K inside a Web Application.

# EDA Notebbok:

Link: [EDA Notebook](./notebook/EDA.ipynb)

# Model Traing Approach Notebook:

Link: [Model training Notebook](./notebook/model_trainer.ipynb)

# AWS Deployment link:

AWS ELastic Beanstalk link: [http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/](http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/)
