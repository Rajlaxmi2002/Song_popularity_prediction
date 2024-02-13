from src.SongPopularityPrediction import logger
from src.SongPopularityPrediction.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.SongPopularityPrediction.pipeline.stage_2_validation import DataValidationTrainingPipeline
from src.SongPopularityPrediction.pipeline.stage_3_transformation import DataTransformationTrainingPipeline
from src.SongPopularityPrediction.pipeline.stage_4_model_training import ModelTrainerTrainingPipeline
from src.SongPopularityPrediction.pipeline.stage_5_model_evaluation import ModelEvaluationPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"STAGE : {STAGE_NAME} started")
    data_ing=DataIngestionTrainingPipeline()
    data_ing.main()
    logger.info(f"STAGE : {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"

try:
    logger.info(f"STAGE : {STAGE_NAME} started")
    data_ing=DataValidationTrainingPipeline()
    data_ing.main()
    logger.info(f"STAGE : {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f"STAGE : {STAGE_NAME} started")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"STAGE : {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f"STAGE : {STAGE_NAME} started")
   model_train = ModelTrainerTrainingPipeline()
   model_train.main()
   logger.info(f"STAGE : {STAGE_NAME} completed")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Evaluation Stage"
try:
    logger.info(f"STAGE : {STAGE_NAME} started")
    model_eval=ModelEvaluationPipeline()
    model_eval.main()
    logger.info(f"STAGE : {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e) 
    raise e