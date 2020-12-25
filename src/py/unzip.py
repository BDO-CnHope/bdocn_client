# -*- coding: utf-8 -*-
# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

import zipfile

def un_zip(src_path, filename, unzip_to):
    path = src_path + '\\' + filename
    frzip = zipfile.ZipFile(path, 'r')
    frzip.extractall(unzip_to)
    frzip.close()