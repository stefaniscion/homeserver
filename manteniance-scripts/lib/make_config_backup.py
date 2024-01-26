import tarfile
from os.path import join

def make_config_backup(config_path,config_backup_path):
    # archive the config directory in a .tar.xz
    tar_file_path = join(config_backup_path, "config.tar.xz")
    with tarfile.open(tar_file_path, "w:xz") as tar:
        tar.add(config_path, arcname=config_path.stem)