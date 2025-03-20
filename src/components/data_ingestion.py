import os
from urllib import request
import zipfile
from src.logging import logger
from src.utils.common import get_size
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    """
    A class to handle data ingestion tasks, including downloading and extracting files.

    Attributes:
        config (DataIngestionConfig): Configuration object containing paths and URLs for data ingestion.
    """

    def __init__(self, config: DataIngestionConfig) -> None:
        """
        Initializes the DataIngestion class with the provided configuration.

        Args:
            config (DataIngestionConfig): Configuration object for data ingestion.
        """
        self.config = config

    def download_file(self) -> None:
        """
        Downloads the file from the source URL specified in the configuration.

        The downloaded file is saved to the path specified in `self.config.local_data_file`.
        If the file already exists, it logs the file size instead of re-downloading.

        Raises:
            Exception: If the download fails due to network issues or invalid URLs.
        """
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"File downloaded successfully: {filename}")
                logger.debug(f"Download headers: {headers}")
            except Exception as e:
                logger.error(f"Failed to download file from {self.config.source_URL}: {e}")
                raise
        else:
            file_size = get_size(Path(self.config.local_data_file))
            logger.info(f"File already exists: {self.config.local_data_file} (Size: {file_size})")

    def extract_zip_file(self) -> None:
        """
        Extracts the contents of the zip file specified in `self.config.local_data_file`.

        The contents are extracted to the directory specified in `self.config.unzip_dir`.
        If the extraction directory does not exist, it is created.

        Raises:
            Exception: If the extraction fails due to invalid zip files or I/O errors.
        """
        unzip_path = self.config.unzip_dir
        try:
            # Create the extraction directory if it doesn't exist
            os.makedirs(unzip_path, exist_ok=True)
            logger.info(f"Extracting zip file to: {unzip_path}")

            # Extract the zip file
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(path=unzip_path)
            logger.info(f"Successfully extracted zip file: {self.config.local_data_file}")
        except zipfile.BadZipFile:
            logger.error(f"Invalid zip file: {self.config.local_data_file}")
            raise
        except Exception as e:
            logger.error(f"Failed to extract zip file: {e}")
            raise
