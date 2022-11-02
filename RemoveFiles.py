import os, shutil, time

def main():
  del_folders = 0
  del_files = 0

  path = "Path to delete"
  days = 30
  sec = time.time() - (24*60*60)
  if os.path.exists(path):
    for root_folder,folders,files in os.walk(path):
        if sec >= get_age(root_folder):
            remove_folder(root_folder)
            del_folders += 1

            break
        else:
            for folder in folders:
                folder_path = os.path.join(root_folder,folder)
                if sec >= get_age(folder_path):
                    remove_folder(folder_path)
                    del_folders += 1
            
            for file in files:
                file_path = os.path.join(root_folder,file)
                if sec >= get_age(file_path):
                    remove_file(file_path)
                    del_files += 1
    else:
        if sec >= get_age(path):
            remove_file(path)
            del_files += 1
  else:
    print("Path is not found")
    del_files += 1
  print(f"Deleted files: {del_folders}")
  print(f"Deleted folders: {del_files}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete {path}")

def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete {path}")

def get_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == "__main__":
    main()