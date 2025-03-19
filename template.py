import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: [%(message)s]')

list_of_files = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    path = Path(filepath)
    dir_name, file_name = os.path.split(path)

    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)
        logging.info(f"Creating empty folder: {dir_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{file_name} is already exists")
