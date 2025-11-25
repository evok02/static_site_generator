import os
import shutil

def delete_from_public(path):
    if not os.path.exists(path):
        raise ValueError("Invalid path")
    for item in os.listdir(path):
        current_path = os.path.join(path, item)
        if os.path.isdir(current_path):
            print(f"Deleting form subdirectory: {current_path}")
            delete_from_public(current_path)
            os.rmdir(current_path)
        if os.path.isfile(current_path):
            print(f"Deleting file {current_path}")
            os.remove(current_path)

def copy_to_folder(source, destination):
    if not os.path.exists(source):
        raise Exception("Path doesn't exist...")
    for item in os.listdir(source):
        current_path = os.path.join(source, item)
        if os.path.isdir(current_path):
            new_destination = os.path.join(destination, item)
            os.mkdir(new_destination)
            copy_to_folder(current_path, new_destination)
        if os.path.isfile(current_path):
            shutil.copy(current_path, destination)

        
    
def copy_to_docs(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    destination_path = (os.path.join(os.getcwd(), "docs"))
    delete_from_public(destination_path)
    copy_to_folder(dir_path, destination_path)


