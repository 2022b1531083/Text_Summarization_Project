from Text_Summarization_Project.config.configuration import ConfigurationManager
from Text_Summarization_Project.components.model_evaluation import ModelEvaluation
from Text_Summarization_Project.logging import logger
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
        

    def run(self):
        config = ConfigurationManager(config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH)
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()