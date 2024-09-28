from src.wine_quality.logging import logger
from wine_quality.components.model_trainer import ModelTrainer
from wine_quality.config.configuration import ConfigurationManager

STAGE_NAME = 'Model Trainer Stage'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == '__main__':
    
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.error(e)
        raise e
    