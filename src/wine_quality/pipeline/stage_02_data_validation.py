from wine_quality.components.data_ingetion import DataIngestion
from wine_quality.components.data_validation import DataValidation
from wine_quality.config.configuration import ConfigurationManager
from wine_quality.logging import logger

STAGE_NAME = 'Data Validation Stage'
class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.error(e)
        raise e
    
