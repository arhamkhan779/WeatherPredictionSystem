from WeatherPredictionSystem import logger
from WeatherPredictionSystem.pipeline.Data_Ingestion_Pipeline import DataIngestionPipeline
from WeatherPredictionSystem.pipeline.Data_Preprocessing_Pipeline import DataPreprocessingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} is Started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} is Completed")
except Exception as e:
    raise e


STAGE_NAME="Data Preprocessing Stage"

try:
    logger.info(f"{STAGE_NAME} is Started")
    obj=DataPreprocessingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} is Completed")
except Exception as e:
    raise e