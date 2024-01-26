import os
from dotenv import dotenv_values
from lib.make_config_backup import make_config_backup
from lib.clean_config_backup_directory import clean_config_backup_directory

# get the config path from the .env file
config = dotenv_values("./services/.env")

# get some paths
config_path = config["CONFIG_PATH"]
config_backup_path = os.path.join(config["STORAGE_PATH"]+"/config_bak/")

print("* Making config backup...")
#make_config_backup(config_path,config_backup_path)

print("* Cleaning config backup directory...")
clean_config_backup_directory(config_backup_path)