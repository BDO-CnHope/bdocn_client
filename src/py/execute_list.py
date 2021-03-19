# @Time    : 2021/03/18
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from time_template import time_template
from pathlib import Path
user_home = str(Path.home())
from shutil import copy2

import download
import check_hash
import select_bdo_game_dir

def dm1_font(dir,path,font_var):
    if Path(path).is_file() is True:
        local_font_hash = check_hash.get_local_hash(path)
        online_font_hash = check_hash.get_github_font_hash()
        if local_font_hash != online_font_hash and font_var != '1':
            download.download_github_font(dir)
        else:
            print("execute_list.py >>> def dm1_font(path,font_var) >>> same font")
    else:
        print("execute_list.py >>> def dm1_font(path,font_var) >>> can not find: " +str(path)+" , downloading")
        download.download_github_font(dir)

def dm2_font(dir,path,font_var):
    if Path(path).is_file() is True:
        local_font_hash = check_hash.get_local_hash(path)
        online_font_hash = check_hash.get_gitee_font_hash()
        if local_font_hash != online_font_hash and font_var != '1':
            download.download_gitee_split_font(dir)
        else:
            print("execute_list.py >>> def dm2_font(path,font_var) >>> same font")
    else:
        print("execute_list.py >>> def dm2_font(path,font_var) >>> can not find: " +str(path)+" , downloading")
        download.download_gitee_split_font(dir)

def dm1_hm1(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm1_hm1(dir)")

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/languagedata_en.loc'

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client/languagedata_cn.loc'

    font_dir = dir + r'/prestringtable/font/'
    font_path = dir + r'/prestringtable/font/pearl.ttf'

    local_font_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    local_font_path = user_home + r'/AppData/Roaming/bdocn_client/pearl.ttf'

    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_github_loc_cn_hash()
        if local_loc_hash != online_loc_hash:
            download.download_github_loc_cn(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def dm1_hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def dm1_hm1(dir): can not find: " +str(loc_path))
        download.download_github_loc_cn(loc_dir)
        copy2(loc_path,loc_ads_path)

    dm1_font(local_font_dir,local_font_path,font_var)
    copy2(local_font_path,font_path)

def dm1_hm2(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm1_hm2(dir)")

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/languagedata_en.loc'

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client/languagedata_tw.loc'

    font_dir = dir + r'/prestringtable/font/'
    font_path = dir + r'/prestringtable/font/pearl.ttf'

    local_font_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    local_font_path = user_home + r'/AppData/Roaming/bdocn_client/pearl.ttf'

    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_github_loc_tw_hash()
        if local_loc_hash != online_loc_hash:
            download.download_github_loc_tw(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def dm1_hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def dm1_hm1(dir): can not find: " +str(loc_path))
        download.download_github_loc_tw(loc_dir)
        copy2(loc_path,loc_ads_path)

    dm1_font(local_font_dir,local_font_path,font_var)
    copy2(local_font_path,font_path)

def dm1_hm3(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm1_hm3(dir)")

    font_dir = dir + r'/prestringtable/font/'

    download.download_github_font(font_dir)

def dm1_hm4(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm1_hm4(dir)")

    ads_dir = dir + r'/ads/'
    font_dir = dir + r'/prestringtable/font/'
    font_path = dir + r'/prestringtable/font/pearl.ttf'

    download.download_loc_en(ads_dir)
    dm1_font(font_dir,font_path,font_var)

def dm2_hm1(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm2_hm1(dir)")

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/languagedata_en.loc'

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client/languagedata_cn.loc'

    font_dir = dir + r'/prestringtable/font/'
    font_path = dir + r'/prestringtable/font/pearl.ttf'

    local_font_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    local_font_path = user_home + r'/AppData/Roaming/bdocn_client/pearl.ttf'

    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_gitee_loc_cn_hash()
        if local_loc_hash != online_loc_hash:
            download.download_gitee_split_loc_cn(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def dm2_hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def dm2_hm1(dir): can not find: " +str(loc_path))
        download.download_gitee_split_loc_cn(loc_dir)
        copy2(loc_path,loc_ads_path)

    dm2_font(local_font_dir,local_font_path,font_var)
    copy2(local_font_path,font_path)

def dm2_hm2(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm1_hm2(dir)")

    ads_dir = dir + r'/ads/'
    loc_ads_path = dir + r'/ads/languagedata_en.loc'

    loc_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    loc_path = user_home + r'/AppData/Roaming/bdocn_client/languagedata_tw.loc'

    font_dir = dir + r'/prestringtable/font/'
    font_path = dir + r'/prestringtable/font/pearl.ttf'

    local_font_dir = user_home + r'/AppData/Roaming/bdocn_client/'
    local_font_path = user_home + r'/AppData/Roaming/bdocn_client/pearl.ttf'


    if Path(loc_dir).is_dir() is False:
        Path(loc_dir).mkdir(parents=True, exist_ok=True)

    if Path(loc_path).is_file() is True:
        local_loc_hash = check_hash.get_local_hash(loc_path)
        online_loc_hash = check_hash.get_gitee_loc_tw_hash()
        if local_loc_hash != online_loc_hash:
            download.download_gitee_split_loc_tw(loc_dir)
            copy2(loc_path,loc_ads_path)
        else:
            print("execute_list.py >>> def dm2_hm1(dir): same loc")
            copy2(loc_path,loc_ads_path)
    else:
        print("execute_list.py >>> def dm2_hm1(dir): can not find: " +str(loc_path))
        download.download_gitee_split_loc_tw(loc_dir)
        copy2(loc_path,loc_ads_path)

    dm2_font(local_font_dir,local_font_path,font_var)
    copy2(local_font_path,font_path)

def dm2_hm3(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm2_hm3(dir)")

    font_dir = dir + r'/prestringtable/font/'

    download.download_gitee_split_font(font_dir)

def dm2_hm4(dir,font_var):
    time_template()
    print("execute_list.py >>> def dm2_hm4(dir)")

    ads_dir = dir + r'/ads/'
    font_dir = dir + r'/prestringtable/font/'
    font_path = dir + r'/prestringtable/font/pearl.ttf'

    download.download_loc_en(ads_dir)
    dm2_font(font_dir,font_path,font_var)

