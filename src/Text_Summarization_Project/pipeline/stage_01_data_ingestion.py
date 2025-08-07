from Text_Summarization_Project.config.configuration import ConfigurationManager
from Text_Summarization_Project.components.data_ingestion import DataIngestion  
from Text_Summarization_Project.logging import logger
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

class DataIngestionPipeline:
    def __init__(self):
        pass

    def run(self):
        config_manager = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        data_ingestion_config = config_manager.get_data_ingestion_config()
        
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()