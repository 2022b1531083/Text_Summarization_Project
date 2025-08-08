from Text_Summarization_Project.constants import *
from Text_Summarization_Project.utils.common import read_yaml, create_directories
from Text_Summarization_Project.entity import DataIngestionConfig
from Text_Summarization_Project.entity import DataValidationConfig
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

class ConfigurationManager:
    def __init__(self, config_file_path: CONFIG_FILE_PATH , params_file_path: PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) ->DataIngestionConfig: # type: ignore
        config =self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config =DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            
        )
        
        return data_ingestion_config
    
    
    def get_data_validation_config(self) ->DataValidationConfig: # type: ignore
        config =self.config.data_validation
        
        create_directories([config.root_dir])
        
        data_validation_config =DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
            
        )
        
        return data_validation_config
        
    

