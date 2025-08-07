import os
import urllib.request as request
import zipfile
from Text_Summarization_Project.logging import logger
from Text_Summarization_Project.utils.common import get_size
from pathlib import Path
from Text_Summarization_Project.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from: {self.config.source_URL}")
            filename, headers = request.urlretrieve(url =self.config.source_URL, filename = self.config.local_data_file)
            logger.info(f"Downloaded file: {filename}, and info : \n{headers}")
        else:
            logger.info(f"File already exists of Size : {get_size(Path(self.config.local_data_file))}")
            
            
            
    def extract_zip_file(self):
        """zip_file_path: str
        extracts the zip file into the specified directory
        funtion return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file to: {unzip_path}")