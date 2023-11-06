
import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer



if __name__ == '__main__':
   dataingestion = DataIngestion()
   train_data,test_data = dataingestion.initiate_data_ingestion()
   datatransformation = DataTransformation()
   train_array,test_array,_ = datatransformation.initiate_data_transformation(train_data,test_data)
   model_trainer = ModelTrainer()
   model_trainer.initiate_model_trainer(train_array,test_array)