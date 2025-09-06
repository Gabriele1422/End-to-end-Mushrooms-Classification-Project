
from box import ConfigBox
from box.exceptions import BoxValueError
from cnnMushroomsClassifier import logger
import yaml
import os
from pathlib import Path

def read_yaml(yaml_file_path : Path)-> ConfigBox:
    
    """
    read a yaml file and return a configuration dict
    
    Args:
        yaml_file_path: (str) path like input
    Raises:
        ValueError: if the file is empty
        e: empty file
    
    Return:
        ConfigBox: configbox type
    """
    project_root = Path(__file__).resolve().parent.parent.parent.parent

    try:
        yaml_file_path = os.path.join(project_root, yaml_file_path) 
        print(yaml_file_path)
        with open(yaml_file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file {yaml_file_path} loadel successfully.")
            return ConfigBox(content)
    
    except BoxValueError as e:
        print(e)
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e


def create_directory(directory_list : list , verbose: bool = True):
    """
    takes a list of directories as list of string and create them one by one.
    
    Args: 
        directory_list : (list) list of directory names as string
        verbose: (bool) Enable logging message
    
    Returns:
    Raises: 
    """
    for dir in directory_list:
        os.makedirs(dir, exist_ok=True)
        
    if verbose:
        logger.info(f"Create new directory {dir}")
    