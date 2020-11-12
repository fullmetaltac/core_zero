import hashlib
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from os import urandom, remove, makedirs, walk
from os.path import exists, join, sep
from pathlib import Path
from random import randint
from shutil import rmtree

from core.managers.string_manager import StringManager as sm


class FileManager:

    @staticmethod
    def size_str_to_bytes(size: str):
        '''
        :param size: Size string where number and units separated with space.
        (e.g. "10.43 KB", "11 GB", "343.1 MB" )
        :return: size in bytes stored in int format
        '''
        units = {"B": 1, "KB": 10 ** 3, "MB": 10 ** 6, "GB": 10 ** 9, "TB": 10 ** 12}
        number, unit = [string.strip() for string in size.split()]
        return int(float(number) * units[unit])

    @staticmethod
    def md5(file_path: str):
        '''
        :param file_path: file path for md5 calculation
        :return: string with md5 value
        '''
        with open(file_path, "rb") as file:
            file_hash = hashlib.md5()
            chunk = file.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = file.read(8192)
            return file_hash.hexdigest()

    @staticmethod
    def file_gen(file_path: str, size: int):
        with open(file_path, 'wb') as file:
            file.write(urandom(size))
            return file

    @staticmethod
    def folder_create(folder_path: str):
        if not FileManager.is_folder_exist(folder_path):
            makedirs(folder_path)

    @staticmethod
    def folder_gen(root_path: str, depth: int = 10, name_max_length: int = 20):
        folders_list = [sm.str_rnd(randint(1, name_max_length)) for _ in range(depth)]
        path = join(root_path, *folders_list)
        makedirs(path)
        return Path(path)

    @staticmethod
    def rnd_file_tree(root_path: str, depth: int = 10, name_max_length: int = 20, max_file_size: int = 1024 * 1024):
        results = []
        folder_path = FileManager.folder_gen(root_path, depth, name_max_length)
        for _ in range(depth):
            relative_path = Path(*folder_path.parts[:randint(len(Path(root_path).parts), depth)])
            results.append(FileManager.file_gen(join(relative_path, sm.str_rnd(name_max_length)), max_file_size))
        return results

    @staticmethod
    def file_del(file_path: str):
        if FileManager.is_file_exist(file_path):
            remove(file_path)

    @staticmethod
    def folder_del(folder_path: str):
        if FileManager.is_folder_exist(folder_path):
            rmtree(folder_path)

    @staticmethod
    def is_file_exist(file_path: str):
        return exists(file_path)

    @staticmethod
    def is_folder_exist(folder_path: str):
        return exists(folder_path)

    @staticmethod
    def file_copy(source: str, destination: str):
        copy_file(source, destination)

    @staticmethod
    def folder_copy(source: str, destination: str):
        copy_tree(source, destination)

    @staticmethod
    def file_find(folder_path: str, file_name: str):
        res = []
        for dir_path, dir_names, file_names in walk(folder_path):
            for file_name in [f for f in file_names if file_name in f]:
                res.append(join(dir_path, file_name))
        return res

    @staticmethod
    def file_name(file_path: str):
        return file_path.split(sep).pop()
