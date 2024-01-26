import os
import logging
from dotenv import dotenv_values
from lib.make_config_backup import make_config_backup
from lib.clean_config_backup_directory import clean_config_backup_directory

# set up logging
logging.basicConfig(level=logging.INFO)

# get the config path from the .env file
config = dotenv_values("./services/.env")

# get some paths
config_path = config["CONFIG_PATH"]
config_backup_path = os.path.join(config["STORAGE_PATH"]+"/config_bak/")

logging.info("* Making config backup...")
make_config_backup(config_path,config_backup_path)

logging.info("* Cleaning config backup directory...")
clean_config_backup_directory(config_backup_path)