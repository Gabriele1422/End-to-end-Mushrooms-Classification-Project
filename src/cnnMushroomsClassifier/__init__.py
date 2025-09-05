import logging
import os
import sys



logging_str = "[%(asctime)s : %(levelname)s: %(module)s: %(message)s]"
log_dir = 'logs'

os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(log_dir, "running_logs.log")
# If the directory doesn't exist create a new one.

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ])


# This logger will be imported and used in all modules
logger = logging.getLogger("cnnClassifierLogger")