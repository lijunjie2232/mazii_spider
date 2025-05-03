from MaziiSpider import MaziiSpider
from SpiderConfig import SpiderConfig
from pathlib import Path
from tqdm import tqdm
from multiprocessing.pool import ThreadPool

if __name__ == "__main__":
    ROOT = Path(__file__).parent.resolve()
    OUTPUT_DIR = ROOT / "xml"
    OUTPUT_DIR.mkdir(exist_ok=True)

    config = SpiderConfig(config_path=ROOT / "config.yaml")
    spider = MaziiSpider(config=config)
    sp_list = spider.get_specialized_list()
    pool = ThreadPool(processes=config.threads)

    mz_dict_list = ["jaen", "jacn", "jatw"]
    sp_list_key = list(sp_list.keys())
    loop = tqdm(total=len(sp_list_key) * len(mz_dict_list))

    for mz_dict in mz_dict_list:
        for sp in sp_list_key:
            # use ThreadPool to run spider.word_list in async parallel
            # recall function: spider.word_list(sp, mz_dict).save_xml(f"{sp}_{mz_dict}.xml")
            pool.apply_async(
                spider.word_list,
                args=(sp,),
                kwds={
                    "mz_dict": mz_dict,
                    "save": OUTPUT_DIR / f"{sp}_{mz_dict}.xml",
                },
                callback=lambda x: loop.update(),
            )
    pool.close()
    pool.join()
    loop.close()
