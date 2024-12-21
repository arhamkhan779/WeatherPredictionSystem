from WeatherPredictionSystem.constants import *
from WeatherPredictionSystem.utils.common import read_yaml,create_directories
from WeatherPredictionSystem.entity.config_entity import DataIngstionConfig,DataPreprocessorConfig,ModelTrainerConfig
import os
from pathlib import Path

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngstionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngstionConfig(
            root_dir=config.root_dir,
            source_url=config.data_url,
            local_data_file=config.Dataset_dir,
            prefix=config.prefix
        )

        return data_ingestion_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessorConfig:
        config=self.config.data_preprocessing
        create_directories([config.root_dir])

        data_preprocessing_config=DataPreprocessorConfig(
           root_dir=config.root_dir,
           input_processor_path=config.input_processor_path,
           target_processor_path=config.target_processor_path
        )

        return data_preprocessing_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config=self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir,
            input_processor_path=config.input_processor_path,
            target_processor_path=config.target_processor_path,
            Data_dir=config.data_dir,
            model_path= config.train_model_path,
            training_result=config.training_results,
            confusion_matrix=config.confusion_matrix,
            n_estimators=self.params.n_estimators,
            max_depth=self.params.max_depth,
            min_samples_split=self.params.min_samples_split,
            min_samples_leaf=self.params.min_samples_leaf,
            max_features=self.params.max_features,
            bootstrap=self.params.bootstrap,
            random_state=self.params.random_state,
            criterion=self.params.criterion
            
        )
        return model_trainer_config
    


    

    
