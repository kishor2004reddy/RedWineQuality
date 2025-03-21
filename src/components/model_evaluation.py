import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.entity.config_entity import ModelEvaluationConfig
from src.utils.common import save_json
from src.logging import logger
from pathlib import Path
import pandas as pd
import numpy as np


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    @staticmethod
    def eval_metrics(actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)
        return rmse, mae, r2

    def save_results(self):
        test = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test.drop(columns=[self.config.target_column])
        y_test = test[self.config.target_column]

        predicted = model.predict(X_test)

        rmse, mae, r2 = ModelEvaluation.eval_metrics(y_test, predicted)

        scores = {
            "Root Mean Squared Error": rmse,
            "Mean Absolute Error": mae,
            "R2 Score": r2
        }

        logger.info(scores)

        save_json(path=Path(self.config.metric_file_name), data=scores)
