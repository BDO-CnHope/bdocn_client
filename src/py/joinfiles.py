# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from pathlib import Path,PureWindowsPath
from time_template import time_template

def join_files(fromdir, todir, tofilename):
    time_template()
    print("joinfiles.py >>> def join_files(fromdir, todir, tofilename)")

    readsize = 1024
    path = todir + r'/' + tofilename
    output = open(path, 'wb')
    path = Path(fromdir)
    parts  = sorted(path.glob('*'))
    print('joinfiles.py >>> parts: ' + str(parts))
    for filename in parts:
        filepath = PureWindowsPath(fromdir).joinpath(filename)
        print('joinfiles.py >>> filepath is: ' + str(filepath))
        fileobj  = open(filepath, 'rb')
        print('joinfiles.py >>> combine '+ str(filename) + ' to ' + str(path))
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )
