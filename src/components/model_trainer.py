import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

from src.utils import save_object,evaluate_model
from dataclasses import dataclass

@dataclass
class ModeltrainerConfig:
   trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
   def __init__(self):
      self.model_trainer_config = ModeltrainerConfig()

   def initiate_model_trainer(self,train_array,test_array):
      try:
         logging.info('Splitting Independent and Dependent variables from train and test array')
         X_train,y_train,X_test,y_test = (
            train_array[:,:-1],
            train_array[:,-1],
            test_array[:,:-1],
            test_array[:,-1]
         )

         models = {
         'LogisticRegression':LogisticRegression(),
         'Decision Tree':DecisionTreeClassifier(),
         'Support vector Machine':SVC(),
         'Naive Bayes':GaussianNB(),
         'Random Forest':RandomForestClassifier(),
         'KNN':KNeighborsClassifier()
         }
         model_report:dict= evaluate_model(X_train,y_train,X_test,y_test,models)
         print(model_report)
         print('\n============================================================================================')
         logging.info(f'Model report : {model_report}')

         #To get best Model score from dictionary
         best_model_score = max(sorted(model_report.values()))

         best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
         ]
         best_model = models[best_model_name]

         print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
         print('\n====================================================================================\n')
         logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
        
         save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=best_model
         )

      except Exception as e:
         logging.info('Exception occured at model Training')
         raise Exception(e,sys)