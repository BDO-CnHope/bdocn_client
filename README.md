# 黑色沙漠汉化工具客户端

本汉化工具是以`Steam`的黑色沙漠美服/欧服为主而设计的。汉化文本使用的是台服的繁简文本。按理其他区域（比如：韩服，日服，大洋，俄服等）应该都能用，但并未测试过。如果有测试过可行的同学可以发个issue。

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

# issues
- 如有问题**请开issue提问**！
- 或者加Q群(不定时回复): 104039903

# 声明
- 本汉化工具和代码仅供学习交流，如作他用所承受的法律责任一概与作者无关！
- 本汉化汉化开放给所有的玩家学习和使用，与`黑沙公会CnHope`现在并无任何利益关联，完全是用爱发电维持着这个项目。如不喜欢请另寻高明。
  - 账号和命名只是因为历史遗留原因没法随意改动, 还会导致汉化工具也需要大幅修改。
  - 如现任`黑沙CnHope公会`/会长认为我不应该再使用这个命名，请联系我(`Naunter`)进行商讨解决办法。
- 请文明游戏，不要恶意引战!

# 相关链接
- [bdocn](https://github.com/BDO-CnHope/bdocn)
- [bdocn_client](https://github.com/BDO-CnHope/bdocn_client)
- [黑沙汉化语言包](https://gitee.com/bdo-cnhope/bdocn)
- [黑沙汉化工具客户端](https://gitee.com/bdo-cnhope/bdocn_client)
- [Make your client English](https://steamcommunity.com/sharedfiles/filedetails/?id=1561979491)
- [[Guide Update] New English Patch Links.](https://www.reddit.com/r/blackdesertonline/comments/lrid4g/guide_update_new_english_patch_links/?sort=new)

# 赞助和帮助
## 用以下的链接在Vultr开一个新的VPS账号可获得$100刀的使用额度
- 至于VPS用来干嘛的请自行搜索科学上网(狗头
[![Foo](https://www.vultr.com/media/banners/banner_468x60.png)](https://www.vultr.com/zh/?ref=8385583-6G)
