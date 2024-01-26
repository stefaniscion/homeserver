import os

def clean_config_backup_directory(config_backup_path):
    # get the list of files in the backup directory
    files = os.listdir(config_backup_path)
    # if there are more than 10 files, delete the oldest one
    if len(files) > 10:
        files.sort()
        os.remove(os.path.join(config_backup_path,files[0]))