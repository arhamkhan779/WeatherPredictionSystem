from WeatherPredictionSystem.components.Data_Ingestion import DataIngestion
from WeatherPredictionSystem.config.configuration import ConfigurationManager
from WeatherPredictionSystem import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        configuration=config.get_data_ingestion_config()
        Obj=DataIngestion(config=configuration)
        Obj.Ingest_Dataset()