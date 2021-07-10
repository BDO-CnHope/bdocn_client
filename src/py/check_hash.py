# @Time    : 2021/03/18
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from hashlib import sha256
from urllib.request import build_opener,install_opener,urlopen
from socket import timeout
from tkinter.messagebox import showinfo

from time_template import time_template

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

def get_online_hash(url):
    time_template()
    print("check_hash.py >>> def get_online_hash()")
    print("check_hash.py >>> def get_online_hash(): url: " + str(url))
    
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        a = urlopen(url, timeout=10)
    except:
        print("check_hash.py >>> def get_online_hash(url): something wrong, maybe timeout")
        showinfo('get_online_hash','获取文件Hash超时，请重试！')
        online_hash = False
    else:
        online_hash = a.read().decode('utf-8').strip()
        print("check_hash.py >>> def get_online_hash(): online_hash: " + str(online_hash))
    return online_hash

def get_local_hash(path):
    time_template()
    print("check_hash.py >>> def get_local_hash()")
    print("check_hash.py >>> def get_local_hash(): path: " + str(path))

    BUF_SIZE = 65536  
    hash_sha256 = sha256()
    
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            else:
                hash_sha256.update(data)

    print("check_hash.py >>> def get_local_hash(): hash_sha256.hexdigest(): " + format(hash_sha256.hexdigest()))
    return(format(hash_sha256.hexdigest()))

def get_github_font_hash():
    time_template()
    print("check_hash.py >>> def get_github_font_hash()")
    url = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/FONT_SHA256'
    if get_online_hash(url) != False:
        a_hash = get_online_hash(url)
        print("check_hash.py >>> def get_github_font_hash(): a_hash: "+str(a_hash))
    else:
        a_hash = False
    return a_hash

def get_gitee_font_hash():
    time_template()
    print("check_hash.py >>> def get_gitee_font_hash()")
    url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/FONT_SHA256'
    if get_online_hash(url) != False:
        a_hash = get_online_hash(url)
        print("check_hash.py >>> def get_gitee_font_hash(): a_hash: "+str(a_hash))
    else:
        a_hash = False
    return a_hash

def get_github_loc_cn_hash():
    time_template()
    print("check_hash.py >>> def get_github_loc_cn_hash()")
    url = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/LOC_CN_SHA256'
    if get_online_hash(url) != False:
        a_hash = get_online_hash(url)
        print("check_hash.py >>> def get_github_loc_cn_hash(): a_hash: "+str(a_hash))
    else:
        a_hash = False
    return a_hash

def get_gitee_loc_cn_hash():
    time_template()
    print("check_hash.py >>> def get_gitee_loc_cn_hash()")
    url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/LOC_CN_SHA256'
    if get_online_hash(url) != False:
        a_hash = get_online_hash(url)
        print("check_hash.py >>> def get_gitee_loc_cn_hash(): a_hash: "+str(a_hash))
    else:
        a_hash = False
    return a_hash

def get_github_loc_tw_hash():
    time_template()
    print("check_hash.py >>> def get_github_loc_tw_hash()")
    url = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/LOC_TW_SHA256'
    if get_online_hash(url) != False:
        a_hash = get_online_hash(url)
        print("check_hash.py >>> def get_github_loc_tw_hash(): a_hash: "+str(a_hash))
    else:
        a_hash = False
    return a_hash

def get_gitee_loc_tw_hash():
    time_template()
    print("check_hash.py >>> def get_gitee_loc_tw_hash()")
    url = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/LOC_TW_SHA256'
    if get_online_hash(url) != False:
        a_hash = get_online_hash(url)
        print("check_hash.py >>> def get_gitee_loc_tw_hash(): a_hash: "+str(a_hash))
    else:
        a_hash = False
    return a_hash