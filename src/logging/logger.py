import logging
import os
import sys

file_name = "running_logs.log"
log_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, file_name)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
    ]
)

logger = logging.getLogger("RedWineLogger")