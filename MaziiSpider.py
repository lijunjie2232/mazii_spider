import requests
import pickle
from SpiderConfig import SpiderConfig
from utils import to_dict
from pathlib import Path
import json
from pprint import pprint
from YouDaoXML import YouDaoXML
from YouDaoWord import YouDaoWord
from tqdm import tqdm
from traceback import print_exc


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

    def get_specialized_list(self, lang=""):
        if not lang:
            lang = self.config.lang
        return self.get_i18n(lang=lang)["specialized"]

    def word_list(
        self,
        field,
        mz_dict=None,
        order="asc",
        limit=5000,
        skip=0,
        save=None,
    ):
        try:
            xml = YouDaoXML()
            config = self.routers.words
            url = self.config.api_url + config.router
            json_data = config.json if "json" in config else None
            assert json_data is not None
            json_data["field"] = field
            json_data["dict"] = mz_dict if mz_dict else self.config.dict
            json_data["order"] = order
            json_data["limit"] = 1
            json_data["skip"] = 0
            resp = self.session.request(
                method=config.method,
                url=url,
                json=to_dict(json_data),
            )
            data = json.loads(resp.text)
            assert data["status"] == 200, Exception(data["message"])
            if not "total" in data or data["total"]["value"] < 1:
                return None

            json_data["limit"] = limit
            for skip in tqdm(
                range(0, data["total"]["value"], limit),
                leave=False,
                desc=f"{field}-{mz_dict}"
            ):
                json_data["skip"] = skip
                resp = self.session.request(
                    method=config.method,
                    url=url,
                    json=to_dict(json_data),
                )
                data = json.loads(resp.text)
                assert data["status"] == 200, Exception(data["message"])

                for item in data["results"]:
                    xml.add_word(
                        YouDaoWord(
                            word=item["word"],
                            trans=(
                                f"({item['phonetic']}); "
                                if item["phonetic"]
                                else "" + "; ".join([i["mean"] for i in item["means"]])
                            ),
                            phonetic=item["phonetic"],
                            tags=field,
                        )
                    )
            if save:
                save = Path(save)
                save.parent.mkdir(exist_ok=True, parents=True)
                xml.save_xml(save)
            return xml.words
        except Exception as e:
            print_exc()
            raise e


if __name__ == "__main__":
    ROOT = Path(__file__).parent.resolve()
    config = SpiderConfig(config_path=ROOT / "config.yaml")
    spider = MaziiSpider(config=config)
    sp_list = spider.get_specialized_list()
    pprint(sp_list)
    spider.word_list("it", save=f"it.xml")
    pass
