from src.entity.config_entity import DataValidationConfig
from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
from src.logging import logger

STAGE_NAME = "Data Validation"


class DataValidationTrainingPipeline:

    @staticmethod
    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validata_dtype_of_columns()


if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        pipe = DataValidationTrainingPipeline()
        pipe.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e
