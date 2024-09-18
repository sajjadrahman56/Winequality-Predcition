from wine_quality.components.data_ingetion import DataIngestion
from wine_quality.config.configuration import ConfigurationManager
from wine_quality.logging import logger

STAGE_NAME = 'Data Ingestion Stage'
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.error(e)
        raise e
    
