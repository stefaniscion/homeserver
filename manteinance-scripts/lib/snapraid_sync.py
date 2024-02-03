import os
import logging


def snapraid_sync():
    logging.info("Launching snapraid sync...")
    os.system("snapraid sync")
    logging.info("Done.")