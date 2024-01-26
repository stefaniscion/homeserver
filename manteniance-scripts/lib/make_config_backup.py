import os
import tarfile
from datetime import datetime


def make_config_backup(config_path, config_backup_path):
    # if the backup directory doesn't exist, create it
    if not os.path.isdir(config_backup_path):
        os.mkdir(config_backup_path)
    # assemble the archive name with the current date
    now_string = datetime.now().strftime("%Y%m%d%I%M%S")
    archive_name = "config_bak_"+now_string+".tar.xz"
    # archive the config directory in a .tar.xz
    with tarfile.open(os.path.join(config_backup_path, archive_name), "w:xz") as tar:
        tar.add(config_path)