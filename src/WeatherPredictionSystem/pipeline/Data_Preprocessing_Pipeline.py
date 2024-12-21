from WeatherPredictionSystem.components.Data_preprocessing import DataPreprocessor
from WeatherPredictionSystem.config.configuration import ConfigurationManager
from WeatherPredictionSystem import logger

class DataPreprocessingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        configuration=config.get_data_preprocessing_config()
        Obj=DataPreprocessor(config=configuration)
        Obj.create_preprocessor()