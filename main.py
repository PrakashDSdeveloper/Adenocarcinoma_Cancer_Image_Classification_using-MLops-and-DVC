from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNN_Classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e
