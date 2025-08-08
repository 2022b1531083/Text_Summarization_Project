
import os
from Text_Summarization_Project.logging  import logger
from Text_Summarization_Project.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False
                    break  # No need to check further if a file is missing

            # Save the result
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
