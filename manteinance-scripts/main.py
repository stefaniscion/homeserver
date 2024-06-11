import os
import logging
import argparse
from dotenv import dotenv_values
from lib.make_config_backup import make_config_backup
from lib.clean_config_backup_directory import clean_config_backup_directory
from lib.snapraid_scrub import snapraid_scrub
from lib.snapraid_sync import snapraid_sync

# get the config path from the .env file
config = dotenv_values(".env")

# get some paths
config_path = config["CONFIG_PATH"]
config_backup_path = os.path.join(config["STORAGE_PATH"] + "/config_bak/")
logging_path = os.path.join(config["LOGGING_PATH"] + "/manteniance.log")

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[logging.FileHandler(logging_path), logging.StreamHandler()],
)


# parse arguments
parser = argparse.ArgumentParser(description="Run some maintenance operations.")
parser.add_argument(
    "--configbackup", action=argparse.BooleanOptionalAction, default=True
)
parser.add_argument(
    "--cleanbackup", action=argparse.BooleanOptionalAction, default=True
)
parser.add_argument(
    "--snapraidscrub", action=argparse.BooleanOptionalAction, default=True
)
parser.add_argument(
    "--snapraidsync", action=argparse.BooleanOptionalAction, default=True
)
args = parser.parse_args()

# valorize things to do
do_config_backup = args.configbackup
do_clean_backup = args.cleanbackup
do_snapraid_scrub = args.snapraidscrub
do_snapraid_sync = args.snapraidsync


# run the operations

# start config backup
if do_config_backup:
    logging.info("Making config backup...")
    try:
        make_config_backup(config_path, config_backup_path)
    except Exception as e:
        logging.error("Error while making config backup: " + str(e))
else:
    logging.info("Skipping config backup.")

# clean config backup directory
if do_clean_backup:
    logging.info("Cleaning config backup directory...")
    try:
        clean_config_backup_directory(config_backup_path)
    except Exception as e:
        logging.error("Error while cleaning config backup directory: " + str(e))
else:
    logging.info("Skipping config backup cleaning.")

# do snapraid scrub
if do_snapraid_scrub:
    logging.info("Launching snapraid scrub...")
    try:
        snapraid_scrub()
    except Exception as e:
        logging.error("Error while launching snapraid scrub: " + str(e))
else:
    logging.info("Skipping snapraid scrub.")

# do snapraid sync
if do_snapraid_sync:
    logging.info("Launching snapraid sync...")
    try:
        snapraid_sync()
    except Exception as e:
        logging.error("Error while launching snapraid sync: " + str(e))
else:
    logging.info("Skipping snapraid sync.")

logging.info("Done.")
