import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.utils import space_remover

from src.components.data_transformation import DataTransformation,DataTransformationConfig

from src.components.model_trainer import ModelTrainer,ModeltrainerConfig

@dataclass
class DataIngestionConfig:
   train_data_path:str = os.path.join('artifacts','train.csv')
   test_data_path:str = os.path.join('artifacts','test.csv')
   raw_data_path:str = os.path.join('artifacts','raw.csv')

#creating class for data ingestion

class DataIngestion:
   def __init__(self):
      self.ingestion_config = DataIngestionConfig()

   def initiate_data_ingestion(self):
      try:
          logging.info('Data Ingestion Method starts')
          #Reading dataset
          df = pd.read_csv('notebook/data/census_income.csv')
          logging.info('Dataset read as pandas Dataframe')
          #Droping duplicates
          df.drop_duplicates(keep='first',inplace=True)
          logging.info('Duplicates droped from Dataset')
          #Removing white space from categorical columns mainly of -> '<=50K'and'>50k'
          df = space_remover(df)
          logging.info('Spaces are removed from the dataset')

          os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
          df.to_csv(self.ingestion_config.raw_data_path,index=False)

          logging.info('train Test Split')
          train_set,test_set = train_test_split(df,test_size=0.25,random_state=42)

          train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
          test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
          logging.info('Ingestion of the data is completed')

          return(
             self.ingestion_config.train_data_path,
             self.ingestion_config.test_data_path
          )
      except Exception as e:
         logging.info('EException Occured at Data Ingestion Stage')
         raise CustomException(e,sys)
      
