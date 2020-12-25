# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

from zipfile import ZipFile

def un_zip(src_path, filename, unzip_to):
    path = src_path + '\\' + filename
    frzip = ZipFile(path, 'r')
    frzip.extractall(unzip_to)
    frzip.close()