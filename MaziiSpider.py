import requests
import pickle
from SpiderConfig import SpiderConfig
from utils import to_dict
from pathlib import Path
import json
from pprint import pprint


class MaziiSpider:

    def __init__(
        self,
        config,
    ):
        self.config = config.spider
        self.session_config = config.session
        self.headers = self.header_init()
        self.session = self.session_load()
        self.session.proxies = self.session_config.proxies
        self.routers = config.routers

    def header_init(self):
        return self.session_config.headers

    def session_init(self):
        pass
        for k, v in self.headers.items():
            setattr(self.session, k, v)
        pass

    def session_load(self):
        if Path(self.session_config.binary_path).is_dir():
            with open(self.session_config.binary_path, "rb") as f:
                return pickle.load(f)
        else:
            return requests.Session()

    def session_save(self):
        with open(self.session_config.binary_path, "wb") as f:
            pickle.dump(self.session, f)

    def login(self):
        pass

    def get_i18n(self, lang=None):
        """
        lang in [
            "zh-cn",
            "zh-tw",
            "en",
            "ja",
            # ...
        ]
        """
        if not lang:
            lang = self.config.lang
        resp = self.session.request(
            url=self.routers.i18n.router % lang,
            method=self.routers.i18n.method,
        )
        return json.loads(resp.text)

    def set_dict(self, mz_dict):
        self.config.dict = mz_dict

    def get_specialized_list(self):
        return self.get_i18n()["specialized"]

    def word_list(
        self,
        field,
        mz_dict=None,
        order="asc",
        limit=100,
        skip=0,
    ):
        config = self.routers.words
        url = self.config.api_url + config.router
        json_data = config.json if "json" in config else None
        assert json_data is not None
        json_data["field"] = field
        json_data["dict"] = mz_dict if mz_dict else self.config.dict
        json_data["order"] = order
        json_data["limit"] = limit
        json_data["skip"] = skip
        resp = self.session.request(
            method=config.method,
            url=url,
            json=json_data,
        )
        pass


if __name__ == "__main__":
    ROOT = Path(__file__).parent.resolve()
    config = SpiderConfig(config_path=ROOT / "config.yaml")
    spider = MaziiSpider(config=config)
    sp_list = spider.get_specialized_list()
    pprint(sp_list)
    spider.word_list("it")
    pass
