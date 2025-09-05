from Text_Summarization_Project.config.configuration import ConfigurationManager
from Text_Summarization_Project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from transformers import pipeline, AutoTokenizer


class PredictionPipeline:
    def __init__(self):
        # Pass config and params file paths
        self.config = ConfigurationManager(
            config_file_path=CONFIG_FILE_PATH,
            params_file_path=PARAMS_FILE_PATH
        ).get_model_evaluation_config()

    def predict(self, text):
        # Load the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        # Generation parameters for summarization
        gen_kwargs = {"max_length": 128, "num_beams": 8, "length_penalty": 0.8}

        # Create summarization pipeline
        pipe = pipeline(
            "summarization",
            model=self.config.model_path,
            tokenizer=tokenizer
        )

        # Generate summary
        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]['summary_text']
        print("\nSummary:")
        print(output)

        return output
