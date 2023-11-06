import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
def space_remover(dataframe):
   for i in dataframe:
      if dataframe[i].dtype == 'O':
         dataframe[i] = dataframe[i].map(str.strip)
      else:
         pass
   return dataframe

def save_object(file_path,obj):
   try:
      dir_path = os.path.dirname(file_path)

      os.makedirs(dir_path,exist_ok=True)

      with open(file_path,'wb') as file_obj:
         pickle.dump(obj,file_obj)
   except Exception as e:
      raise CustomException(e,sys)
   
def evaluate_model(X_train,y_train,X_test,y_test,models):
   try:
      report = {}
      for i in range(len(list(models))):

         model = list(models.values())[i]
         #train model
         model.fit(X_train,y_train)

         #prediction
         y_pred = model.predict(X_test)

         #Get R2 scores for train and test data
         test_model_score = accuracy_score(y_test,y_pred)
         
         report[list(models.keys())[i]]=test_model_score


      return report
      
   except Exception as e:
      logging.info('Exception occured at utils evalute model')
      CustomException(e,sys)

def load_object(file_path):
   try:
      with open(file_path,'rb') as file_obj:
         return pickle.load(file_obj)
   except Exception as e:
      logging.info('Exception occured at load object method')
      raise CustomException(e,sys)