from wine_quality.components.data_ingetion import DataIngestion
from wine_quality.components.data_transformation import DataTransformation
from wine_quality.config.configuration import ConfigurationManager
from wine_quality.logging import logger
from pathlib import Path

STAGE_NAME = 'Data transformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().strip().split(":")[-1].strip()
                
            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_datasplit()
            else:
                raise Exception("Data validation failed, data schema is not valid")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.error(e)
        raise e
