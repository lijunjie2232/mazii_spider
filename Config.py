import yaml


class SpiderConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(
        self,
        config_path="config.yaml",
    ):
        self.config_path = config_path
        config = self.load_config()
        for key, value in config.items():
            setattr(self, key, value)

    def load_config(self, encoding="utf-8"):
        """
        Load configuration from a YAML file and autowire key-value pairs
        to SpiderConfig member properties.
        """
        with open(self.config_path, "r", encoding=encoding) as f:
            return yaml.safe_load(f)  # Parse the YAML file

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
    config = SpiderConfig()
    print(config)
