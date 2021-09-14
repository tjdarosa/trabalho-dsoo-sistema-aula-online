from abc import ABC
import pickle


class AbstractDAO(ABC):
    def __init__(self, datasource="") -> None:
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))

    def load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def add(self, key, obj):
        self.__cache[key] = obj
        self.dump()

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.dump()
        except KeyError:
            pass

    def getAll(self):
        return self.__cache.values()
