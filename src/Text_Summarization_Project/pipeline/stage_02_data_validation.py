from Text_Summarization_Project.config.configuration import ConfigurationManager
from Text_Summarization_Project.components.data_validation import DataValidation  
from Text_Summarization_Project.logging import logger
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

class DataValidationPipeline:
    def __init__(self):
        pass
        

    def run(self):
        config_manager = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        data_validation_config = config_manager.get_data_validation_config()
        
        data_validation = DataValidation(config=data_validation_config)
        status = data_validation.validate_all_files_exist()
        logger.info(f"Data Validation Status: {status}")
