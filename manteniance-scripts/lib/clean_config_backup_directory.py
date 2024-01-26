import os

def clean_config_backup_directory(config_backup_path):
    max_files = 10
    # get the list of files in the backup directory
    files = os.listdir(config_backup_path)
    # if there are more than x files, delete the oldest one
    if len(files) > max_files:
        files.sort()
        print(files)
        # get the list of files to delete
        files_to_delete = []
        num_files_to_delete = len(files)-max_files
        files_to_delete = files[:num_files_to_delete]
        print(files_to_delete)
        #delete the files
        for file_to_delete in files_to_delete:
            file_to_delete_path = os.path.join(config_backup_path,file_to_delete)
            os.remove(file_to_delete_path)
            print("- Deleted: "+file_to_delete)