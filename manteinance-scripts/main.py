import os
import logging
import argparse
from dotenv import dotenv_values
from lib.make_config_backup import make_config_backup
from lib.clean_config_backup_directory import clean_config_backup_directory


# set up logging
logging.basicConfig(level=logging.INFO)

# parse arguments
parser = argparse.ArgumentParser(description='Run some maintenance operations.')
parser.add_argument('--configbackup', action=argparse.BooleanOptionalAction, default=True)
parser.add_argument('--cleanbackup', action=argparse.BooleanOptionalAction, default=True)
parser.add_argument('--snapraidscrub', action=argparse.BooleanOptionalAction, default=True)
parser.add_argument('--snapraidsync', action=argparse.BooleanOptionalAction, default=True)
args = parser.parse_args()

# get the config path from the .env file
config = dotenv_values("./services/.env")

# get some paths
config_path = config["CONFIG_PATH"]
config_backup_path = os.path.join(config["STORAGE_PATH"] + "/config_bak/")

# run the operations

# start config backup
if args.configbackup:
    logging.info("Making config backup...")
    make_config_backup(config_path, config_backup_path)
else:
    logging.info("Skipping config backup.")

# clean config backup directory
if args.cleanbackup:
    logging.info("Cleaning config backup directory...")
    clean_config_backup_directory(config_backup_path)
else:
    logging.info("Skipping config backup cleaning.")

# TODO add snapraid sync and scrub

# logging.info("Launching snapraid scrub...")
# snapraid_scrub()

# logging.info("Launching snapraid sync...")
# sync()

logging.info("Done.")
