# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

from urllib.request import build_opener,install_opener,urlretrieve,urlopen,Request
from re import findall
from time import sleep
from ran_useragent import GetUserAgent
import ui4

def download_file(url, todir, tofilename):
    path = todir + '\\' + tofilename
    user_agent = GetUserAgent()
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    urlretrieve(url, path)
    

def download_split_files(url, todir):
    user_agent = GetUserAgent()
    header = {"User-Agent":user_agent,}
    add_header = Request(url, headers=header)
    dl_link = urlopen(add_header)
    data = dl_link.read().decode('utf-8')
    filter_data = findall(r'>part[0-9][0-9][0-9][0-9]</a>',data)
    hrefs = []
    hrefs.clear()

    if 'github' in url and 'split_font' in url:
        raw_url = 'https://github.com/BDO-CnHope/bdocn/raw/master/split_font/'
    elif 'github' in url and 'split_font' not in url:
        raw_url = 'https://github.com/BDO-CnHope/bdocn/raw/master/split/'
    elif 'gitee' in url and 'split_font' in url:
        raw_url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/split_font/'
    elif 'gitee' in url and 'split_font' not in url:
        raw_url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/split/'
    else:
        pass

    for i in filter_data:
        href = findall(r'>(.*)</a>',i)
        href = str(href)
        href = href.replace(">",'')
        href = href.replace("</a>",'')
        href = href.replace("['",'')
        href = href.replace("']",'')
        hrefs.append(href)
    
    for filename in hrefs:
        full_url = ''
        full_url = raw_url + '/' + filename
        download_file(full_url, todir, filename)
        #sleep(0.5)
        print(filename)
        print(full_url)

def download_en_loc():
    en_loc_ver = 'http://akamai-gamecdn.blackdesertonline.com/live001/game/config/config.language.version'
    user_agent = GetUserAgent()
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    a = urlopen(en_loc_ver)
    version = a.read().decode('utf-8')
    en_loc_zip = 'http://akamai-gamecdn.blackdesertonline.com/live001/game/language/BDOLanguage_' + version + '.zip'
    return(en_loc_zip)