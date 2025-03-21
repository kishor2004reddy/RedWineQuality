import pandas as pd
from src.logging import logger
from src.entity.config_entity import DataValidationConfig


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.dataframe = pd.read_csv(self.config.unzip_data_dir)
        self.df_cols = set(self.dataframe.columns)

    def validate_all_columns(self) -> bool:
        try:
            schema_cols = self.config.all_schema.keys()

            validation_status = set(self.df_cols) == set(schema_cols)

            with open(self.config.STATUS_FILE, "w") as status_file:
                status_file.write(f"Column Validation Status: {validation_status}\n")

            return validation_status
        except Exception as e:
            logger.exception(f"{e}")
            raise e

    def validata_dtype_of_columns(self):
        try:
            validation_status = True

            for col in self.df_cols:
                if self.dataframe[col].dtype != self.config.all_schema[col]:
                    validation_status = False
                    logger.error(f"In Schema {col} data type is {self.config.all_schema[col]} but in data the datatype is {self.dataframe[col].dtype}")
                    break

            with open(self.config.STATUS_FILE, "a") as status_file:
                status_file.write(f"Column Data Type Validation Status: {validation_status}\n")
        except Exception as e:
            logger.exception(f"{e}")
            raise e
