import os
from dotenv import dotenv_values
from lib.make_config_backup import make_config_backup

config = dotenv_values("./services/.env")

config_path = config["CONFIG_PATH"]
config_backup_path = os.path.join(config["STORAGE_PATH"]+"/config_bak/")
make_config_backup(config_path,config_backup_path)