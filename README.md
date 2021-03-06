# 黑色沙漠汉化工具客户端

汉化目标群体是Steam的黑色沙漠美服/欧服，但按理其他区域（比如：韩服，日服，大洋，俄服等）应该都能用，但并未测试过。如果有测试过可行的同学可以发个issue。

![image](./images/cn1.PNG)

# 使用方法
## 1. 使用客户端安装汉化补丁
1. 下载最新版本(Latest release)的[`bdocn_client.exe`](https://github.com/BDO-CnHope/bdocn_client/releases)
    - 由于不可抗拒的因素，无法成功的在Gitee上传文件，国内用户可以到这里下载: [https://share.weiyun.com/BtJgJGUX](https://share.weiyun.com/BtJgJGUX)
3. 正确的选择黑沙的游戏目录
4. 按指示完成汉化补丁的安装
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
### 20210319
更新版本: 2021031404
- 版本详细请看 [#7](https://github.com/BDO-CnHope/bdocn_client/issues/7)
- 应B站粉丝观众要求，做了个台服繁转简的脚本，功能以后有时间再加入本体(咕)
  - [下载脚本](https://raw.githubusercontent.com/BDO-CnHope/bdocn_client/main/%E5%8F%B0%E6%9C%8D%E7%B9%81%E8%BD%AC%E7%AE%80.bat)

### 20210206
- 添加新功能: 不覆盖现有字体文件. [issue #2](https://github.com/BDO-CnHope/bdocn_client/issues/2)

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
- [Make your client English](https://steamcommunity.com/sharedfiles/filedetails/?id=1561979491)
- [[Guide Update] New English Patch Links.](https://www.reddit.com/r/blackdesertonline/comments/lrid4g/guide_update_new_english_patch_links/?sort=new)

# 赞助和帮助
[![Foo](https://www.vultr.com/media/banners/banner_468x60.png)](https://www.vultr.com/zh/?ref=8385583-6G)
