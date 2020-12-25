# 黑色沙漠汉化工具客户端

# 使用方法
## 1. 通过客户端打汉化补丁
1. 下载`bdocn_client.exe`
2. 正确的选择黑沙的游戏目录
3. 按指示完成汉化补丁的安装
## 2. 手动安装汉化补丁
1. 前往[黑沙汉化语言包](https://github.com/BDO-CnHope/bdocn_client)
2. 打包下载`ads`和`prestringtable`这两个文件夹
3. 找到你本地的黑沙的游戏根目录
4. 将下载的两个文件夹覆盖到目录
## 3. 手动编译客户端安装汉化补丁
1. 安装`python`环境
2. 安装`pyinstaller`
3. 下载`https://github.com/BDO-CnHope/bdocn_client/tree/main/src/py`里的文件包
4. 通过终端执行命令`pyinstaller.exe --clean -D -p .\ -i .\logo_og.ico .\ui4.py`
5. 在`dist`下能找到打包好的执行文件
## 4. 使用旧版的客户端
1. 旧版的客户端是使用`powershell`写的，然后打包成exe可执行文件
2. 已不再维护，但应该还能用
3. https://github.com/BDO-CnHope/bdocn_client/tree/main/src/ps

# 注意
新发布的`python`版的汉化客户端可能会被安全软件识别为可疑的执行文件/病毒/木马等, 这是`pyinstaller`的锅。但可以放心的跑。
如果你不放心/谨慎的话：
1. 请手动安装汉化补丁
2. 请自己编译文件
3. 请自己仔细浏览过源文件后再做决定
4. 如果不清楚/不懂的，请不要下载和运行
5. 如有问题，请开issue讨论

# issue
- 如有问题请开issue提问，比如发现有乱码或者显示不正确等问题。
- 有的话还请关注收藏点个Star，谢谢你的支持！

# 声明
本软件和代码仅供学习交流，如作他用所承受的法律责任一概与作者无关！

# 相关链接
- [bdocn - Github](https://github.com/BDO-CnHope/bdocn)
- [bdocn - Gitee](https://gitee.com/bdo-cnhope/bdocn)
- [黑沙汉化语言包](https://github.com/BDO-CnHope/bdocn)
- [黑沙汉化工具客户端](https://github.com/BDO-CnHope/bdocn_client)

