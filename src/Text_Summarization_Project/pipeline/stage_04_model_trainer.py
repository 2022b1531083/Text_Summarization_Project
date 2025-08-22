from Text_Summarization_Project.config.configuration import ConfigurationManager
from Text_Summarization_Project.components.model_trainer import ModelTrainer  
from Text_Summarization_Project.logging import logger
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

class ModelTrainingPipeline:
    def __init__(self):
        pass
        

    def run(self):
        config = ConfigurationManager(config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH)
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
    
