from src.logging import logger
from src.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from src.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline

StageName = "Data Ingestion"
try:
    logger.info(f"Stage {StageName} Started")
    pipe = DataIngestionTrainingPipeline()
    pipe.main()
    logger.info(f"Stage {StageName} Completed")
except Exception as e:
    logger.exception(e)
    raise e

StageName = "Data Validation"
try:
    logger.info(f"Stage {StageName} Started")
    pipe = DataValidationTrainingPipeline()
    pipe.main()
    logger.info(f"Stage {StageName} Completed")
except Exception as e:
    logger.exception(e)
    raise e

StageName = "Data Transformation"
try:
    logger.info(f"Stage {StageName} Started")
    pipe = DataTransformationTrainingPipeline()
    pipe.main()
    logger.info(f"Stage {StageName} Completed")
except Exception as e:
    logger.exception(e)
    raise e
