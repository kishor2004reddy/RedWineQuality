import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.logging import logger
from src.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        dataframe = pd.read_csv(self.config.data_path)
        train, test = train_test_split(dataframe, test_size=0.2)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Data is split into train and test")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")
