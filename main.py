from src.logging import logger
from src.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline, STAGE_NAME

try:
    logger.info(f"Stage {STAGE_NAME} Started")
    pipe = DataIngestionTrainingPipeline()
    pipe.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
