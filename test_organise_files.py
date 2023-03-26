import os
import pytest
import tempfile
import shutil
from organise_files import organise_files, create_folder


@pytest.fixture
def temporary_directory():
    with tempfile.TemporaryDirectory() as tempdir:
        yield tempdir


def test_create_folder(temporary_directory):
    folder_name = "test_folder"
    create_folder(temporary_directory, folder_name)
    folder_path = os.path.join(temporary_directory, folder_name)
    assert os.path.exists(folder_path) is True


def test_organise_files(temporary_directory):
    file_types = ["txt", "pdf", "jpg"]
    files = []

    for file_type in file_types:
        file_path = os.path.join(temporary_directory, f"sample.{file_type}")
        with open(file_path, "w") as f:
            f.write("dummy content")
        files.append(file_path)

    organise_files(temporary_directory)

    for file_type, file_path in zip(file_types, files):
        organized_path = os.path.join(
            temporary_directory, file_type, os.path.basename(file_path)
        )
        assert os.path.exists(organized_path) is True
        assert os.path.exists(file_path) is False
