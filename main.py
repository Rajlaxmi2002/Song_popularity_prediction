from src.SongPopularityPrediction import logger
from src.SongPopularityPrediction.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.SongPopularityPrediction.pipeline.stage_2_validation import DataValidationTrainingPipeline
STAGE_NAME="Data Ingestion stage"

try:
    logger.info("STAGE : {STAGE_NAME} started")
    data_ing=DataIngestionTrainingPipeline()
    data_ing.main()
    logger.info("STAGE : {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"

try:
    logger.info("STAGE : {STAGE_NAME} started")
    data_ing=DataValidationTrainingPipeline()
    data_ing.main()
    logger.info("STAGE : {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e