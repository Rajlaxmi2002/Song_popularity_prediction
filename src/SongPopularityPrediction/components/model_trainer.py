import pandas as pd
import os
from src.SongPopularityPrediction import logger
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import joblib
from src.SongPopularityPrediction.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data.pop(self.config.target_column)
        test_y = test_data.pop(self.config.target_column)
        DTC = DecisionTreeClassifier(random_state = 11, max_features = 6, class_weight = "balanced",max_depth=self.config.base_estimator__max_depth)

        my_ensemble = AdaBoostClassifier(estimator=DTC,learning_rate=self.config.alpha,n_estimators=self.config.n_estimators)
        my_ensemble.fit(train_x,train_y)


       

        joblib.dump(my_ensemble, os.path.join(self.config.root_dir, self.config.model_name))

