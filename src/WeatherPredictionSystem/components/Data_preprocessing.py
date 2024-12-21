import os
from pathlib import Path
from WeatherPredictionSystem import logger
from WeatherPredictionSystem.entity.config_entity import DataPreprocessorConfig
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from WeatherPredictionSystem.utils.common import save_bin
import pandas as pd

class DataPreprocessor:
    def __init__(self, config: DataPreprocessorConfig):
        """
        Initializes the DataPreprocessor with the provided configuration.

        Args:
            config (DataPreprocessorConfig): Configuration for data preprocessing.
        """
        self.config = config

    def create_preprocessor(self):
        """
        Creates and saves the input and target preprocessors.
        
        - Input processor: A pipeline with a StandardScaler.
        - Target processor: A LabelEncoder for encoding categorical target values.
        
        Raises:
            Exception: If any error occurs during the process.
        """
        try:
            logger.info("Creating Preprocessor ---------- Start")
            df=pd.read_csv("artifacts//data_ingestion//Dataset.csv")
            df=df[['temp_max','temp_min','wind','weather']]
            df_sun=df[df.weather == "sun"]
            df_rain=df[df.weather == "rain"]
            df=pd.concat([df_sun,df_rain])
            X=df.drop(columns=['weather'])
            Y=df[['weather']]
            # Create processors
            target_processor = LabelEncoder()
            input_processor = Pipeline(steps=[
                ('scaler', StandardScaler())
            ])
            target_processor=target_processor.fit(Y)
            input_processor=input_processor.fit(X)

            # Save processors to specified paths
            save_bin(target_processor, Path(self.config.target_processor_path))
            save_bin(input_processor, Path(self.config.input_processor_path))
            
            logger.info(f"Target processor saved at: {self.config.target_processor_path}")
            logger.info(f"Input processor saved at: {self.config.input_processor_path}")
            logger.info("Creating Preprocessor ---------- Done")
        except Exception as e:
            logger.error(f"Error occurred while creating preprocessors: {str(e)}")
            raise e
