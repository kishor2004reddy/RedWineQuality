from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logging import logger

STAGE_NAME = "Data Transformation"


class DataTransformationTrainingPipeline:

    @staticmethod
    def main():
        try:
            config = ConfigurationManager()
            data_transform_config = config.get_data_transformation_config()
            data_transform = DataTransformation(config=data_transform_config)
            data_transform.train_test_split()
        except Exception as e:
            logger.exception(f"{e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        pipe = DataTransformationTrainingPipeline()
        pipe.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e
