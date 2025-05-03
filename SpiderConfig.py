import yaml
from collections import namedtuple
from omegaconf import OmegaConf
from pprint import pprint
from functools import wraps


class SpiderConfig(OmegaConf):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None or ("reload" in kwargs and kwargs["reload"]):
            if "config_path" in kwargs:
                cls._instance = cls.load(kwargs["config_path"])
            elif "dot_list" in kwargs:
                cls._instance = cls.from_dotlist(kwargs["dot_list"])
            elif "cli" in kwargs:
                cls._instance = cls.from_cli(kwargs["argv"])
            else:
                cls._instance = cls.create(*args, **kwargs)

        return cls._instance

    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

    def __repr__(self):
        # return string of all properties
        return self.__str__()

    def __str__(self):
        return (
            "******* SpiderConfig *******\n"
            + "\n".join(f"{k}: {v}" for k, v in self.__dict__.items())
            + "\n******** config end ********"
        )


if __name__ == "__main__":
    config = SpiderConfig(config_path="config.yaml")
    pprint(config)
    pass