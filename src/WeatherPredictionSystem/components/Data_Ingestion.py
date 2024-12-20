import os
from pathlib import Path
import gdown
from WeatherPredictionSystem import logger
from WeatherPredictionSystem.entity.config_entity import DataIngstionConfig

class DataIngestion:
    '''
    Data Ingestion Component to download Data From Google Drive
    '''
    def __init__(self,config:DataIngstionConfig):
        self.config=config

    def Ingest_Dataset(self):

        logger.info("Ingesting Dataset -------------Start")
        try:
            url=self.config.source_url
            prefix=self.config.prefix
            data_dir=self.config.local_data_file

            url_id=url.split('/')[5]
            logger.info(f"Start Downloading Data from {url} in the directory {data_dir}")
            gdown.download(prefix+url_id,data_dir)
            logger.info("Ingesting Dataset ----------- Completed")

        except Exception as e:
            logger.info(e)
            raise e

