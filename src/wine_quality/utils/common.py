import os
import yaml
from box.exceptions import BoxValueError
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.wine_quality.logging import logger
from box import ConfigBox
import json

@ensure_annotations # type: ignore
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Loaded yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("ymal file is empty")
    except Exception as e:
        raise e

@ensure_annotations # type: ignore
def create_directories(path_to_directories: list,verbose=True):
    """
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created Directory  at {path}")

@ensure_annotations # type: ignore
def save_json(path:Path, data:dict):
    """
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file save at : {path}")

@ensure_annotations # type: ignore
def load_json(path:Path)-> ConfigBox:
    """
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded succesfully from : {path}")
    return ConfigBox(content)

@ensure_annotations # type: ignore
def save_bin(data:Any,path:Path):
    """
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file save at : {path}")

@ensure_annotations # type: ignore
def load_bin(path:Path)-> Any:
    """
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded succesfully from : {path}")
    return data