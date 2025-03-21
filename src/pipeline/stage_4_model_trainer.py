from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.logging import logger

STAGE_NAME = "Model Training"


class ModelTrainerPipeline:

    @staticmethod
    def main():
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        pipe = ModelTrainerPipeline()
        pipe.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e
