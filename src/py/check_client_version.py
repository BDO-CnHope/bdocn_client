# @Time    : 2022/01/01
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from urllib.request import build_opener,install_opener,urlopen
from socket import timeout

from time_template import time_template

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

def get_version():
    time_template()
    print("check_client_version.py >>> def check_version()")

    url = 'https://github.com/BDO-CnHope/bdocn_client/raw/main/CHECK/CLIENT_VERSION'
    url_2 = 'https://gitee.com/bdo-cnhope/bdocn_client/raw/main/CHECK/CLIENT_VERSION'
    opener = build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    install_opener(opener)
    try:
        a = urlopen(url_2, timeout=3)
    except:
        print("check_client_version.py >>> def check_version(): something wrong, maybe gitee timeout, try github")
        try: 
            a = urlopen(url, timeout=3)
        except: 
            print("check_client_version.py >>> def check_version(): something wrong, maybe github also timeout")
            version = False
        else:
            version = a.read().decode('utf-8').strip()
        finally:
            return version
    else:
        version = a.read().decode('utf-8').strip()
    finally:
        return version
