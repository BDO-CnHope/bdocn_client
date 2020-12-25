# -*- coding: utf-8 -*-
# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

import urllib.request
import hashlib
from ran_useragent import GetUserAgent

def get_client_version():
    github_client_version = 'https://github.com/BDO-CnHope/bdocn_client/raw/main/CHECK/CLIENT_VERSION'
    user_agent = GetUserAgent()
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    urllib.request.install_opener(opener)
    a = urllib.request.urlopen(github_client_version)
    client_version = a.read().decode('utf-8').strip()
    return(client_version)

def get_font_hash(num):
    github_font_hash = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/FONT_SHA256'
    gitee_font_hash = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/FONT_SHA256'
    user_agent = GetUserAgent()
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    urllib.request.install_opener(opener)
    if num == 1:
        a = urllib.request.urlopen(github_font_hash)
        font_hash = a.read().decode('utf-8').strip()
        return(font_hash)
    elif num == 2:
        a = urllib.request.urlopen(gitee_font_hash)
        font_hash = a.read().decode('utf-8').strip()
        return(font_hash)

def get_loc_hash(num):
    github_loc_hash = 'https://github.com/BDO-CnHope/bdocn/raw/master/CHECK/LOC_SHA256'
    gitee_loc_hash = 'https://gitee.com/bdo-cnhope/bdocn/raw/master/CHECK/LOC_SHA256'
    user_agent = GetUserAgent()
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    urllib.request.install_opener(opener)
    if num == 1:
        a = urllib.request.urlopen(github_loc_hash)
        loc_hash = a.read().decode('utf-8').strip()
        return(loc_hash)
    elif num == 2:
        a = urllib.request.urlopen(gitee_loc_hash)
        loc_hash = a.read().decode('utf-8').strip()
        return(loc_hash)

def get_hash(path):
    BUF_SIZE = 65536  
    sha256 = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return(format(sha256.hexdigest()))
