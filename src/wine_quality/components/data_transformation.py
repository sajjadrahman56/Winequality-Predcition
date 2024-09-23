from src.wine_quality.logging import logger
from sklearn.model_selection import train_test_split as tts
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split as tts
from wine_quality.entity.config_entity import DataTransformationConfig
import os 

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # Shuffle the data
    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)
        logger.info("Data has been shuffled.")
        
        data = data.drop_duplicates()
        logger.info(f"Removed duplicates. Shape: {data.shape}")
        
        data = data.dropna()
        logger.info(f"Removed null values. Shape after removing nulls: {data.shape}")
        
        return data

    # MinMaxScaler
    def scale_data(self, data: pd.DataFrame) -> pd.DataFrame:
        scaler = MinMaxScaler()  
        numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
        data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
        logger.info("Data has been scaled using MinMaxScaler (range 0-1).")
        
        return data

    # Train-test split method
    def train_test_datasplit(self):
        data = pd.read_csv(self.config.data_path)
        
        # Preprocess and scale data
        data = self.preprocess_data(data)
        data = self.scale_data(data)

        # Split into train and test sets
        train, test = tts(data, test_size=0.2, random_state=42)
        
        # Save train and test data
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Logging the details
        logger.info(f"Train shape: {train.shape}, Test shape: {test.shape}")
        print(f"Train shape: {train.shape}, Test shape: {test.shape}")