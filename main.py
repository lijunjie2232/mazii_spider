from MaziiSpider import MaziiSpider
from SpiderConfig import SpiderConfig
from pathlib import Path

# from tqdm import tqdm
from multiprocessing.pool import Pool
from multiprocessing import Lock
from traceback import print_exc
import sys
from YouDaoXML import YouDaoXML

# XML_LOCK = Lock()


def spider_process(
    config,
    sp,
    mz_dict,
    save,
):
    try:
        spider = MaziiSpider(config=config)
        spider.word_list(sp, mz_dict=mz_dict, save=save)
        # if words:
        #     # XML_LOCK.acquire()
        #     xml = YouDaoXML()
        #     xml.words = []
        #     xml.save_xml(save, words)
        #     # XML_LOCK.release()
    except Exception as _:
        print(f"sp: {sp}, mz_dict: {mz_dict}, save: {save}")
        print_exc()
        # XML_LOCK.release()
        exit()


if __name__ == "__main__":
    ROOT = Path(__file__).parent.resolve()
    OUTPUT_DIR = ROOT / "xml"
    OUTPUT_DIR.mkdir(exist_ok=True)

    config = SpiderConfig(config_path=ROOT / "config.yaml")
    spider = MaziiSpider(config=config)

    # pool = ThreadPool(processes=config.threads)
    pool = Pool(processes=config.threads)

    mz_dict_list = [("jaen", "en"), ("jacn", "zh-cn"), ("jatw", "zh-tw")]
    # loop = tqdm()

    sys.stdout.write("spidring...")
    for mz_dict, lang in mz_dict_list:
        sp_list = spider.get_specialized_list(lang)
        for sp in sp_list:
            # use ThreadPool to run spider.word_list in async parallel
            # recall function: spider.word_list(sp, mz_dict).save_xml(f"{sp}_{mz_dict}.xml")
            pool.apply_async(
                spider_process,
                args=(config, sp, mz_dict, OUTPUT_DIR / f"{sp}_{mz_dict}.xml"),
                # callback=lambda x: loop.update(),
                # callback=lambda x: save_xml(x),
            )
    pool.close()
    pool.join()
