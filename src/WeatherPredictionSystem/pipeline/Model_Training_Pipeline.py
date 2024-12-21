from WeatherPredictionSystem.config.configuration import ConfigurationManager
from WeatherPredictionSystem.components.Model_Trainer import ModelTrainer
from WeatherPredictionSystem import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        con=ConfigurationManager()
        configuration=con.get_model_trainer_config()
        obj=ModelTrainer(configuration)
        obj.Train()