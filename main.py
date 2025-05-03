from MaziiSpider import MaziiSpider
from SpiderConfig import SpiderConfig
from pathlib import Path
from tqdm import tqdm
from multiprocessing.pool import ThreadPool

if __name__ == "__main__":
    ROOT = Path(__file__).parent.resolve()
    OUTPUT = ROOT / "xml"
    OUTPUT.mkdir(exist_ok=True)

    config = SpiderConfig(config_path=ROOT / "config.yaml")
    spider = MaziiSpider(config=config)
    sp_list = spider.get_specialized_list()
    pool = ThreadPool(processes=config.threads)

    for mz_dict in tqdm(["jaen", "jacn", "jatw"]):
        for sp in tqdm(sp_list.keys()):
            # use ThreadPool to run spider.word_list in raync parallel
            # recall function: spider.word_list(sp, mz_dict).save_xml(f"{sp}_{mz_dict}.xml")
            pool.apply_async(
                spider.word_list,
                args=(sp,),
                kwds={"mz_dict": mz_dict},
                callback=lambda x: x.save_xml(f"{sp}_{mz_dict}.xml"),
            )
    pool.close()
    pool.join()
