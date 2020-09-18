import json
import csv
from abc import abstractmethod, ABC


class IStructureDriver(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, d):
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'r', encoding='utf8') as f:
            return json.load(f)

    def write(self, some_data=None):
        if not isinstance(some_data, list):
            some_data = list(some_data)
        if not some_data:
            some_data = []
        with open(self.__filename, 'w', encoding='utf8') as f:
            json.dump(some_data, f)
            f.flush()


class CSVFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'r', encoding='utf8') as f:
            file_reader = csv.reader(f, delimiter = ",")
            file_reader = list(file_reader)
            return file_reader

    def write(self, some_data=None):
        if not isinstance(some_data, list):
            some_data = list(some_data)
        if not some_data:
            some_data = []
        with open(self.__filename, "w", encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter=",", lineterminator="\r")
            file_writer.writerow(some_data)

