from scraper import PageScraper
from BotStructures import Handler
from BotStructures import Item
from bs4 import BeautifulSoup
from dbController import Config
import requests
import ctypes
files = Config()
cats = files.readCategories()
ctypes.windll.kernel32.SetConsoleTitleW("Souq.com - Products Scraper v 0.1 ")
scraper = PageScraper()
p_handler = Handler()
for cat in cats:
#ls = scraper.page_scraper("https://egypt.souq.com/eg-en/laptop-notebook/l/?sortby=sr&amp;page=1&section=2&page=1")
    ls = p_handler.getPages(cat.link)
    print(ls)
    ans = []
    for p in ls:
        out = scraper.page_scraper(p)
        if out ==-1:
            break
        ans = ans +out
        print(out)
    print(ans)
    cnt=1
    for i in ans:
        print(str(cnt) +" " +i.price +" "+i.offer+" "+i.desc+" "+i.img+" "+i.link)    
        cnt+=1
n = input()