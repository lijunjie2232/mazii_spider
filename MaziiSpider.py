import requests
import pickle
from SpiderConfig import SpiderConfig
from pathlib import Path


class MaziiSpider:

    def __init__(
        self,
        config,
    ):
        self._config = config
        self.spider = self._config.spider
        self.headers = self.header_init()
        self.session = self.session_load()
        self.session.proxies = self._config.session.proxies

    def header_init(self):
        return self._config.session.headers

    def session_init(self):
        pass
        for k, v in self.headers.items():
            setattr(self.session, k, v)
        pass

    def session_load(self):
        if Path(self._config.session.binary_path).is_dir():
            with open(self._config.session.binary_path, "rb") as f:
                return pickle.load(f)
        else:
            return requests.Session()

    def session_save(self):
        with open(self._config.session.binary_path, "wb") as f:
            pickle.dump(self.session, f)

    def login():
        pass


if __name__ == "__main__":
    ROOT = Path(__file__).parent.resolve()
    config = SpiderConfig(config_path=ROOT / "config.yaml")
    spider = MaziiSpider(config=config)
    print(spider.spider)
    print(spider.session.headers)
    print(spider.session.proxies)
    print(spider.session.verify)
    print(spider.session.trust_env)
