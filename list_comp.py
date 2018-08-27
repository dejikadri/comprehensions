import os

"""
This program uses list comprehension to list particular file extension in a directory

"""


def list_file(files_path, file_ext):
    file_ext = file_ext
    file_list = [f for f in os.listdir(files_path) if f.endswith(file_ext)]

    return file_list
