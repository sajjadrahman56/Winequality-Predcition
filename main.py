import sys
import os


# Add the directory containing the wine_quality module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from wine_quality.logging import logger
from wine_quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine_quality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wine_quality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wine_quality.pipeline.satge_04_model_trainer import ModelTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(e)
    raise e



STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(e)
    raise e