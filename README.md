# 黑色沙漠汉化工具客户端
[点击查看汉化补丁效果展示](SHOW_SC.md)

汉化目标是Steam的黑色沙漠美服/欧服，但按理其他区域（比如：韩服，日服，大洋，俄服等）应该都能用，但并未测试过。如果有测试过可行的同学可以发个issue或discussion里说一下。

![image](./images/cn1.PNG)

# 使用方法
## 1. 使用客户端安装汉化补丁
1. 下载[`bdocn_client.exe`](https://github.com/BDO-CnHope/bdocn_client/raw/main/bdocn_client.exe)
2. 正确的选择黑沙的游戏目录
3. 按指示完成汉化补丁的安装
## 2. 手动安装汉化补丁
1. 前往[黑沙汉化语言包](https://github.com/BDO-CnHope/bdocn)
2. 打包下载`ads`和`prestringtable`这两个文件夹
3. 找到你本地的黑沙的游戏根目录
4. 将下载的两个文件夹覆盖到目录
## 3. 手动编译客户端安装汉化补丁
1. 安装`python`环境
2. 安装`pyinstaller`
3. 下载`https://github.com/BDO-CnHope/bdocn_client/tree/main/src/py`里的文件包
4. 通过终端执行命令`pyinstaller.exe --clean -F -p .\ -i .\logo_og_han.ico .\run.py`
5. 在`dist`下能找到打包好的执行文件
## 4. 使用旧版的客户端
1. 旧版的客户端是使用`powershell`写的，然后打包成exe可执行文件
2. 已不再维护，但应该还能用
3. https://github.com/BDO-CnHope/bdocn_client/tree/main/src/ps

# Update
### 20210313
- 更新版本: 2021031200
- 修复了汉化文字显示问题[issue #3](https://github.com/BDO-CnHope/bdocn_client/issues/3)
- 修复了英语文件的位置
- 添加功能，允许steam的用户在开启汉化工具同时启动steam的黑沙
- 修正了一些其它的错误和问题
- 已知但还未解决的问题(有时间再搞，或者等大佬们提出解决办法，先咕了)：
  - 因为新版本的黑沙调用了新的启动器，导致每次启动黑沙时，启动器都会自动检查游戏文件并修复/更新不匹配的文件，导致已汉化了的语言包每次都会被启动器替换。
  - 所以暂行的解决办法就是先运行黑沙的启动器，然后等启动器扫描和更新完后，再执行汉化。

### 20210311
- 已知问题: 由于黑沙更新了版本（运营商更替)的原因，旧版本的很多地方在新版本黑纱里都被修改了，主要原因就是汉化字体显示错误[issue #3](https://github.com/BDO-CnHope/bdocn_client/issues/3)
  - 感谢@Rokker提出了一个临时的解决办法, 可到这里查看：https://github.com/BDO-CnHope/bdocn_client/issues/3#issuecomment-796784987
  - 但注意要先运行黑沙的启动器后，在保持启动器运行的状态下，再执行汉化

### 20210206
- 添加新功能: 不覆盖现有字体文件. [issue #2](https://github.com/BDO-CnHope/bdocn_client/issues/2)

# 注意
- 已在Windows 10 x64上测试过客户端可正常运行，但未测试在其它版本Windows上的兼容性如何。
- 新发布的`python`版（练手版🙈)的汉化客户端可能会被安全软件误报为可疑的执行文件，但可以放心的运行。如果你不放心的话, 请自行斟酌。

# issue
- 如有问题请开issue提问，比如发现有乱码或者显示不正确等问题。
- 或者加Q群(不定时回复): 104039903

# 声明
- 本软件和代码仅供学习交流，如作他用所承受的法律责任一概与作者无关！

# 相关链接
- [bdocn](https://github.com/BDO-CnHope/bdocn)
- [bdocn_client](https://github.com/BDO-CnHope/bdocn_client)
- [黑沙汉化语言包](https://gitee.com/bdo-cnhope/bdocn)
- [黑沙汉化工具客户端](https://gitee.com/bdo-cnhope/bdocn_client)

