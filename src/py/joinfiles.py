# @Time    : 2020/12/25
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from pathlib import Path,PureWindowsPath
from datetime import datetime

time_stamp = datetime.now()

def join_files(fromdir, todir, tofilename):
    print("[BEGIN] join_files >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    readsize = 1024
    path = todir + r'/' + tofilename
    output = open(path, 'wb')
    path = Path(fromdir)
    parts  = sorted(path.glob('*'))
    print('join_files: parts is: ' + str(parts))
    for filename in parts:
        filepath = PureWindowsPath(fromdir).joinpath(filename)
        print('join_files: filepath is: ' + str(filepath))
        fileobj  = open(filepath, 'rb')
        print('join_files: combine '+ str(fromdir) + ' to ' + str(filename))
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )
