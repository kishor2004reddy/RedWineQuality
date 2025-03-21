import logging

from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logging import logger

STAGE_NAME = "Data Transformation"


class DataTransformationTrainingPipeline:

    @staticmethod
    def main():
        with open("artifacts/data_validation/status.txt", "r") as file:
            line1 = file.readline()
            line2 = file.readline()
            columns_validation_status = line1.split(" ")[-1].strip() == "True"
            columns_dtype_validation_status = line2.split(" ")[-1].strip() == "True"

        if all([columns_validation_status, columns_dtype_validation_status]):
            config = ConfigurationManager()
            data_transform_config = config.get_data_transformation_config()
            data_transform = DataTransformation(config=data_transform_config)
            data_transform.train_test_split()
        else:
            logging.error("Data is not matching with the schema")
            raise ValueError("Data is not matching with the schema")


if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        pipe = DataTransformationTrainingPipeline()
        pipe.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e
