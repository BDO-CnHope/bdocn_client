# -*- coding: utf-8 -*-
# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

import os

def join_files(fromdir, todir, tofilename):
    readsize = 1024
    path = todir + '\\' + tofilename
    output = open(path, 'wb')
    parts  = os.listdir(fromdir)
    parts.sort(  )
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj  = open(filepath, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )

