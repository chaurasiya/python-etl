from dataclasses import dataclass
from dacite import from_dict
from typing import List

# The object which will hold the information related to configuration provided in json format
@dataclass
class ConfigJson:
    reader: Reader
    transform: Transform
    writer: Writer

@dataclass
class Reader:
    connector: DataConnectorParam

@dataclass
class Transform:
    type: List[str]    

@dataclass
class Writer:
    connector: DataConnectorParam

@dataclass
class DataConnectorParam:
    type: str
    config: dict

# ConfigJsonReader class used for reading the config json and return the dataclass object
class ConfigJsonReader:
    def read(self, filepath: str) -> ConfigJson: 
        with open(filepath) as inputjson:
            from_dict(ConfigJson, inputjson)