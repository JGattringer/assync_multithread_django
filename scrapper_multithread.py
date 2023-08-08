from multiprocessing import Pool
from requests import get


def multithreaded_scrapper(url):
    res = get(url)
    chars = res.json()
    print(chars["id"], chars["name"], chars["status"], chars["species"], chars["origin"]["name"], chars["image"])


urls = [f"https://rickandmortyapi.com/api/character/{character_id}" for character_id in range(1, 827)]

if __name__ == '__main__': # On Windows the subprocesses will import (i.e. execute) the main module at start.
                           # We need to insert an if __name__ == '__main__': to avoid creating subprocesses recursively.
    p = Pool(30)
    p.map(multithreaded_scrapper, urls)
    p.terminate()
    p.join()
