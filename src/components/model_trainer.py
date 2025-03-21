import os
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)

        X_train = train.drop(columns=[self.config.target_column])
        X_test = test.drop(columns=[self.config.target_column])
        y_train = train[self.config.target_column]
        y_test = test[self.config.target_column]

        en = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        en.fit(X_train, y_train)

        joblib.dump(en, os.path.join(self.config.root_dir, self.config.model_name))
