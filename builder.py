from abc import abstractmethod, ABC
from driver import JsonFileDriver
from driver import CSVFileDriver


class Builder(ABC):
    @abstractmethod
    def build(self):
        pass


class JsonBuilder(Builder):

    def build(self, filename=None):
        filename = input('enter the path')
        if not filename:
            filename = 'tmp.json'
        else:
            filename = filename.strip()
            if not filename.endswith('.json'):
                filename = filename + '.json'

        return JsonFileDriver(filename)


class CSVBuilder(Builder):

    def build(self):
        filename = input('enter the path')
        if not filename:
            filename = 'tmp.csv'
        else:
            filename = filename.strip()
            if not filename.endswith('.csv'):
                filename = filename + '.csv'

        return CSVFileDriver(filename)


class DriverFactory:

    @staticmethod
    def get_driver(driver_name):
        drivers = {
            'json': JsonBuilder,
            'csv': CSVBuilder
        }
        if driver_name in drivers:
            return drivers[driver_name]().build()

