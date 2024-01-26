import os
import tarfile

def make_config_backup(config_path,config_backup_path):
    # if the backup directory doesn't exist, create it
    if not os.path.isdir(config_backup_path):
        os.mkdir(config_backup_path)
    # archive the config directory in a .tar.xz
    tar_file_path = os.path.join(config_backup_path, "config.tar.xz")
    with tarfile.open(tar_file_path, "w:xz") as tar:
        tar.add(config_path, arcname=config_path.stem)