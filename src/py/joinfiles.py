# @Time    : 2020/12/25
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from os import listdir
from os.path import join

def join_files(fromdir, todir, tofilename):
    readsize = 1024
    path = todir + '\\' + tofilename
    output = open(path, 'wb')
    parts  = listdir(fromdir)
    parts.sort(  )
    for filename in parts:
        filepath = join(fromdir, filename)
        fileobj  = open(filepath, 'rb')
        print('combine '+ fromdir + ' to ' + filename)
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )

