from WeatherPredictionSystem.constants import *
from WeatherPredictionSystem.utils.common import read_yaml,create_directories
from WeatherPredictionSystem.entity.config_entity import DataIngstionConfig,DataPreprocessorConfig
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
    
