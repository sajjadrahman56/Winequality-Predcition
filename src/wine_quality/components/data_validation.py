import pandas as pd
from src.wine_quality.constants import *
from wine_quality.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = set(data.columns)
            all_schema = self.config.all_schema

            validation_status = True

            # Use self.config.STATUS_FILE instead of self.status
            with open(self.config.STATUS_FILE, "w") as file:
                for col, dtype in all_schema.items():
                    if col not in all_columns:
                        validation_status = False
                        file.write(f"Column '{col}' is missing.\n")
                    elif str(data[col].dtype) != dtype:
                        validation_status = False
                        file.write(f"Column '{col}' has incorrect dtype. Expected: {dtype}, Found: {str(data[col].dtype)}\n")
                    else:
                        file.write(f"Column '{col}' dtype matches the expected dtype.\n")

                file.write(f"Data Validation status : {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e
