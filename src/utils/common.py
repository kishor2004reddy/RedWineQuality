import os
from box.exceptions import BoxValueError
import yaml
from src.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
       Reads a YAML file and returns its contents as a ConfigBox object.


       :param path_to_yaml: The path to the YAML file.

       :return: ConfigBox: A ConfigBox object containing the parsed YAML data with dot-access support.

       :raises:
           FileNotFoundError:
                If the specified YAML file is not found.
           RuntimeError:
               If an unexpected error occurs while reading the file.
       """
    try:
        with open(path_to_yaml, 'r') as file:
            data = yaml.safe_load(file)
            if data is None:
                raise BoxValueError(f"{path_to_yaml} file is empty")
            logger.info(f"{path_to_yaml} file loaded successfully")
            return ConfigBox(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path_to_yaml}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Invalid YAML format in file '{path_to_yaml}': {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while reading {path_to_yaml}: {e}")


@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose=True) -> None:
    """ Creates Directories of the passed paths of list

    :param path_to_directories: list of paths of directories to be created
    :param verbose: False if logging of creation of directories is not required
    :return: None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"{path} directory created successfully")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
        Saves a dictionary to a JSON file.

        :param path:
            The path where the JSON file will be saved.
        :type path: Path
        :param data:
            The dictionary containing data to be written to the file.
        :type data: dict

        :return: None

        :raises TypeError:
            If `data` is not serializable to JSON.
        :raises RuntimeError:
            If an unexpected error occurs.
    """
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        logger.info(f"json file saved at: {path}")
    except TypeError as e:
        raise TypeError(f"Failed to serialize data to JSON: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while saving JSON to {path}: {e}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its content as a ConfigBox object.

    :param path:
        The path to the JSON file to load.
    :type path: Path

    :return:
        A ConfigBox object containing the parsed JSON data.
    :rtype: ConfigBox

    :raises FileNotFoundError:
        If the specified file is not found.
    :raises BoxValueError:
        If the file is empty.
    :raises json.JSONDecodeError:
        If the file contains invalid JSON.
    :raises RuntimeError:
        If an unexpected error occurs while loading the file.
    """
    try:
        with open(path, 'r') as file:
            content = json.load(file)
            if not content:
                raise BoxValueError(f"{path} file is empty")
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in file '{path}': {e}", e.doc, e.pos)
    except BoxValueError as e:
        raise BoxValueError(f"{path} file is empty: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while loading JSON from {path}: {e}")


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data to a binary file using joblib.

    :param data:
        The data to be saved.
    :type data: Any
    :param path:
        The path where the binary file will be saved.
    :type path: Path

    :return: None

    :raises PermissionError:
        If the program does not have permission to write to the file.
    :raises OSError:
        If there is a system-related error during file writing.
    :raises RuntimeError:
        If an unexpected error occurs while saving the file.
    """
    try:
        with open(path, 'wb') as file:
            joblib.dump(data, file)
        logger.info(f"Binary file saved at: {path}")
    except PermissionError as e:
        raise PermissionError(f"Permission denied while saving binary file to {path}: {e}")
    except OSError as e:
        raise OSError(f"Error saving binary file at {path}: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while saving binary file to {path}: {e}")


@ensure_annotations
def load_bin(path: Path) -> ConfigBox:
    """
    Loads a binary file using joblib and returns its content as a ConfigBox object.

    :param path:
        The path to the binary file to load.
    :type path: Path

    :return:
        A ConfigBox object containing the loaded data.
    :rtype: ConfigBox

    :raises FileNotFoundError:
        If the specified file is not found.
    :raises BoxValueError:
        If the file is empty.
    :raises RuntimeError:
        If an unexpected error occurs while loading the file.
    """
    try:
        with open(path, 'rb') as file:
            content = joblib.load(file)
            if not content:
                raise BoxValueError(f"{path} file is empty")
        logger.info(f"Binary file loaded successfully from: {path}")
        return ConfigBox(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except BoxValueError as e:
        raise BoxValueError(f"{path} file is empty: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while loading binary file from {path}: {e}")

