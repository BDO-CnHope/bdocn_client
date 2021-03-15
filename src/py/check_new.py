# @Time    : 2021/03/14
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from urllib.request import build_opener,install_opener,urlretrieve,urlopen,Request
from hashlib import sha256
from datetime import datetime

time_stamp = datetime.now()

def get_client_version():
    print("[BEGIN] get_client_version >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    github_client_version = 'https://github.com/BDO-CnHope/bdocn_client/raw/main/CHECK/CLIENT_VERSION'
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0')]
    install_opener(opener)
    a = urlopen(github_client_version)
    client_version = a.read().decode('utf-8').strip()
    return(client_version)

def get_font_hash(num):
    print("[BEGIN] get_font_hash >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    github_font_hash = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/FONT_SHA256'
    gitee_font_hash = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/FONT_SHA256'
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0')]
    install_opener(opener)
    if num == 1:
        a = urlopen(github_font_hash)
        font_hash = a.read().decode('utf-8').strip()
        return(font_hash)
    elif num == 2:
        a = urlopen(gitee_font_hash)
        font_hash = a.read().decode('utf-8').strip()
        return(font_hash)
    else:
        return None

def get_loc_hash(num):
    print("[BEGIN] get_loc_hash >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    github_loc_hash = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/LOC_SHA256'
    gitee_loc_hash = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/LOC_SHA256'
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0')]
    install_opener(opener)
    if num == 1:
        a = urlopen(github_loc_hash)
        loc_hash = a.read().decode('utf-8').strip()
        return(loc_hash)
    elif num == 2:
        a = urlopen(gitee_loc_hash)
        loc_hash = a.read().decode('utf-8').strip()
        return(loc_hash)
    else:
        return None

def get_hash(path):
    print("[BEGIN] get_hash >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    print("get_hash: got path " + path)
    BUF_SIZE = 65536  
    hash_sha256 = sha256()
    
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            hash_sha256.update(data)
    return(format(hash_sha256.hexdigest()))
