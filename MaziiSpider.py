import requests
import pickle


class MaziiSpider:

    def __init__(
        self,
        word,
        config=None,
    ):
        self.word = word
        self.url = ""
        self.headers = {"User-Agent": ""}
        self.session = requests.Session()
        self.session.headers = self.headers
        self.session.proxies = {"http": "", "https": ""}
        self.session.verify = False
        self.session.trust_env = False

    def session_init():
        pass

    def login():
        pass


if __name__ == "__main__":
    spider = MaziiSpider("hello")
    print(spider.word)
    print(spider.url)
    print(spider.headers)
    print(spider.session.headers)
    print(spider.session.proxies)
    print(spider.session.verify)
    print(spider.session.trust_env)
