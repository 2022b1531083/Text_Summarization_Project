from Text_Summarization_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Text_Summarization_Project.pipeline.stage_02_data_validation import DataValidationPipeline  
from Text_Summarization_Project.pipeline.stage_03_data_transformation import DataTransformationPipeline
from Text_Summarization_Project.pipeline.stage_05_model_trainer import ModelTrainingPipeline
from Text_Summarization_Project.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    data_ingestion = DataIngestionPipeline()
    # Run the data ingestion pipeline
    data_ingestion.run()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    data_validation = DataValidationPipeline()
    # Run the data ingestion pipeline
    data_validation.run()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    data_transformation = DataTransformationPipeline()
    # Run the data transformation pipeline
    data_transformation.run()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    model_trainer = ModelTrainingPipeline()
    # Run the data training pipeline
    model_trainer.run()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

