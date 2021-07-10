# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from time import strftime,localtime

def time_template():
    print("\n" + str(strftime("%Y-%m-%d %H:%M:%S", localtime())))