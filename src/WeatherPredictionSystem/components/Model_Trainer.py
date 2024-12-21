import os
from pathlib import Path
from WeatherPredictionSystem import logger
from WeatherPredictionSystem.entity.config_entity import ModelTrainerConfig
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config=config
        self.input_processor=joblib.load(self.config.input_processor_path)
        self.target_processor=joblib.load(self.config.target_processor_path)
    
    def Train(self):
        try:
            logger.info(f"Loading Dataset from {self.config.Data_dir}")
            df=pd.read_csv(self.config.Data_dir)
            logger.info(f"Feature Selection")
            df=df[['temp_max','temp_min','wind','weather']]
            df_sun=df[df.weather == "sun"]
            df_rain=df[df.weather == "rain"]
            df=pd.concat([df_rain,df_sun])
            logger.info(f"Selecting X and Y feature")
            X=df.drop(columns=["weather"])
            Y=df[['weather']]
            logger.info("Applying preprocessing")
            X=self.input_processor.fit_transform(X)
            Y=self.target_processor.fit_transform(Y)
            logger.info(f"Splitting Data into training and validation part")
            X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=45)
            logger.info(f"Perform training on train data")
            model=RandomForestClassifier()
            model.fit(X_train,Y_train)
            logger.info("Training Done Successfully")

            logger.info("Start Evaluating the Model")
            y_pred_prob = model.predict_proba(X_test)[:, 1]  
            y_pred_binary = (y_pred_prob >= 0.5).astype(int)  
            accuracy=accuracy_score(Y_test,y_pred_binary)
            precision=precision_score(Y_test,y_pred_binary)
            recall=recall_score(Y_test,y_pred_binary)
            f1=f1_score(Y_test,y_pred_binary)
            model_results={
                "accuracy":[accuracy],
                "precision":[precision],
                "recall":[recall],
                "f1_score":[f1]
            }
            logger.info(f"Saving Model Results at {self.config.training_result}")
            results_df=pd.DataFrame(model_results)
            results_df.to_csv(self.config.training_result)
            cm=confusion_matrix(Y_test,y_pred_binary)
            plt.figure(figsize=(6, 5))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Sunny", "Rainy"],             yticklabels=["Sunny", "Rainy"])
            plt.title("Confusion Matrix")
            plt.xlabel("Predicted Labels")
            plt.ylabel("Actual Labels")
            plt.savefig(self.config.confusion_matrix)
            plt.close()

            logger.info(f"Saving Model At {self.config.model_path}")
            joblib.dump(model,self.config.model_path)
        except Exception as e:
            logger.info(e)
            raise e

