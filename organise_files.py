import os
import shutil
from typing import Optional

def create_folder(directory: str, folder_name: str) -> None:
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def organise_files(directory: Optional[str] = None) -> None:
    if directory is None:
        directory = os.getcwd()

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1].lower()
            create_folder(directory, file_extension)
            shutil.move(file_path, os.path.join(directory, file_extension, filename))

if __name__ == "__main__":
    organise_files()