from Text_Summarization_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
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