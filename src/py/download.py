# @Time    : 2021/03/18
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from urllib.request import build_opener,install_opener,urlretrieve,urlopen,Request
from re import findall
from socket import timeout
from tkinter.messagebox import showinfo

from time_template import time_template
import temp_dir
import joinfiles

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

def download_file(url, todir, tofilename):
    time_template()
    print("download.py >>> download_file(url, todir, tofilename):" + " url: " + str(url) + " todir: " + str(todir) + " tofilename: " + str(tofilename))
    
    timeout(10)
    path = todir + r'/' + tofilename
    print("download.py >>> download_file(url, todir, tofilename): path: " + str(path))
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        urlretrieve(url, path)
    except:
        print("download.py >>> download_file(url, todir, tofilename) >>> something wrong, maybe timeout")
        showinfo('download_file()','文件下载超时，请重试！')
    else:
        pass

def download_split_files(url, raw_url, todir):
    time_template()
    print("download.py >>> download_split_files(url, todir):"+ " url: " + str(url) + " todir: " + str(todir))
    header = {"User-Agent":user_agent}
    add_header = Request(url, headers=header)
    try:
        dl_link = urlopen(add_header, timeout=10)
    except:
        print("download.py >>> download_split_files(url, raw_url, todir) >>> something wrong, maybe timeout")
        showinfo('download_split_files()','分块文件下载超时，请重试！')
        dl_link = False
    else:
        pass

    if dl_link != False:
        data = dl_link.read().decode('utf-8')
        filter_data = findall(r'>part[0-9][0-9][0-9][0-9]</a>',data)
        hrefs = []
        hrefs.clear()

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
            full_url = raw_url + filename
            print("download.py >>> download_split_files(url, todir) >>> for filename in hrefs: full_url: "+ str(full_url))
            download_file(full_url, todir, filename)
    else:
        pass

def download_github_loc_cn(todir):
    time_template()
    print("download.py >>> def download_github_loc_cn(todir) >>> todir: " + str(todir))
    url = "https://github.com/BDO-CnHope/bdocn/raw/master/ads/languagedata_cn.loc"
    tofilename = "languagedata_cn.loc"
    download_file(url, todir, tofilename)

def download_github_loc_tw(todir):
    time_template()
    print("download.py >>> def download_loc_tw(todir) >>> todir: " + str(todir))
    url = "https://github.com/BDO-CnHope/bdocn/raw/master/ads/languagedata_tw.loc"
    tofilename = "languagedata_tw.loc"
    download_file(url, todir, tofilename)

def download_github_font(todir):
    time_template()
    print("download.py >>> def download_github_font(todir) >>> todir: " + str(todir))
    url = "https://github.com/BDO-CnHope/bdocn/raw/master/prestringtable/font/pearl.ttf"
    tofilename = "pearl.ttf"
    download_file(url, todir, tofilename)

def download_gitee_split_loc_cn(todir):
    time_template()
    print("download.py >>> def download_gitee_split_loc_cn(todir) >>> todir: " + str(todir))
    url = "https://gitee.com/bdo-cnhope/bdocn/tree/master/split_loc_cn/"
    raw_url = "https://gitee.com/bdo-cnhope/bdocn/raw/master/split_loc_cn/"
    tmp_dir = temp_dir.temp_loc_dir()
    tofilename = "languagedata_cn.loc"
    download_split_files(url, raw_url, tmp_dir)
    joinfiles.join_files(tmp_dir, todir, tofilename)

def download_gitee_split_loc_tw(todir):
    time_template()
    print("download.py >>> def download_gitee_split_loc_tw(todir) >>> todir: " + str(todir))
    url = "https://gitee.com/bdo-cnhope/bdocn/tree/master/split_loc_tw/"
    raw_url = "https://gitee.com/bdo-cnhope/bdocn/raw/master/split_loc_tw/"
    tmp_dir = temp_dir.temp_loc_dir()
    tofilename = "languagedata_tw.loc"
    download_split_files(url, raw_url, tmp_dir)
    joinfiles.join_files(tmp_dir, todir, tofilename)

def download_gitee_split_font(todir):
    time_template()
    print("download.py >>> def download_gitee_split_font(todir) >>> todir: " + str(todir))
    url = "https://gitee.com/bdo-cnhope/bdocn/tree/master/split_font/"
    raw_url = "https://gitee.com/bdo-cnhope/bdocn/raw/master/split_font/"
    tmp_dir = temp_dir.temp_font_dir()
    tofilename = "pearl.ttf"
    download_split_files(url, raw_url, tmp_dir)
    joinfiles.join_files(tmp_dir, todir, tofilename)

# old, discared
def download_loc_tw(todir):
    time_template()
    print("download.py >>> def download_loc_tw(todir) >>> todir: " + str(todir))
    url = "http://dn.blackdesert.com.tw/UploadData/ads/languagedata_tw.loc"
    tofilename = "languagedata_en.loc"
    download_file(url, todir, tofilename)

def download_loc_en(todir):
    time_template()
    print("download.py >>> def download_loc_en(todir) >>> todir: " + str(todir))
    en_loc_ver = 'http://dn.sea.playblackdesert.com/UploadData/ads_files'
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        a = urlopen(en_loc_ver, timeout=5)
    except:
        print("download.py >>> def download_loc_en(): something wrong, maybe timeout")
        showinfo('languagedata_en.loc','文件下载超时，请重试！')
        version = False
    else:
        version = a.read().decode('utf-8')

    if version != False:
        fil_version = findall(r'languagedata_en.loc\t(\d+)', version)
        url = 'http://dn.sea.playblackdesert.com/UploadData/ads/languagedata_en/' + "".join(fil_version) + '/languagedata_en.loc'
        tofilename = "languagedata_en.loc"
        download_file(url, todir, tofilename)
    else:
        pass