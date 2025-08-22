from Text_Summarization_Project.config.configuration import ConfigurationManager
from Text_Summarization_Project.components.data_transformation import DataTransformation  
from Text_Summarization_Project.logging import logger
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

class DataTransformationPipeline:
    def __init__(self):
        pass
        

    def run(self):
        config_manager = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        data_transformation_config = config_manager.get_data_transformation_config()
        
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert() # fixed the name
    
