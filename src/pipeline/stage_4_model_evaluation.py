from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logging import logger

STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline:

    @staticmethod
    def main():
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.save_results()


if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        pipe = ModelEvaluationPipeline()
        pipe.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e