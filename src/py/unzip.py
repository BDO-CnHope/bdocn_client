# @Time    : 2020/12/25
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from zipfile import ZipFile

def un_zip(src_path, filename, unzip_to):
    path = src_path + '\\' + filename
    print('unpacking '+path)
    frzip = ZipFile(path, 'r')
    frzip.extractall(unzip_to)
    frzip.close()