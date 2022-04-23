import abc
from dataclasses import dataclass
from distutils.command.config import config
from pythonetl.json_reader import DataConnectorParam

# connector interface with abstracted out methods which any connector can use for extensibility purpose of connector module
class DataConnector(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__init__') and 
                callable(subclass.init) and 
                hasattr(subclass, 'data') and 
                callable(subclass.data) or 
                NotImplemented)
    @abc.abstractmethod
    def __init__(self):
        """initialize the data connector with necessary connector configs"""
        raise NotImplementedError
    @abc.abstractmethod
    def data(self):
        """fetch the data from source using data connector props"""
        raise NotImplementedError

@dataclass
class FileDataConnector(DataConnector):
    dcparam: DataConnectorParam
    def __init__(self):
        print("initializing the file data connector")
        config = self.dcparam.config
        print("printing the present config config", config)
        pass
    def data(self) -> str:
        with open(self.dcparam.config.get("path")) as input:
            input.read()



