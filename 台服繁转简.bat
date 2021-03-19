@echo off
:start
setlocal
setlocal enabledelayedexpansion
cls
echo.
echo   黑沙台服繁转简脚本By Naunter@20210319
echo  ==============================================================
echo   执行本脚本前，请先使用黑色沙漠汉化工具(bdocn_client)下载汉化补丁
echo  ==============================================================
echo   下载黑色沙漠汉化工具(bdocn_client)：
echo   路线1: https://github.com/BDO-CnHope/bdocn_client/releases
echo   路线2: https://share.weiyun.com/BtJgJGUX
echo ==============================================================
echo   此脚本仅用于台服黑沙替换繁体中文为简体中文。要配合
echo   黑色沙漠汉化工具(bdocn_client)来使用
echo  ==============================================================
echo.
echo   1. 先运行黑色沙漠汉化工具(bdocn_client)下载(简体)汉化补丁
echo.
echo   2. 然后运行此脚本
echo.
echo   3. 选择“黑沙的游戏根目录”
echo      举例：C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online\
echo.
echo   4. 选择“替换繁体中文为简体中文”
echo.
echo  ==============================================================
echo.
echo  1. 替换繁体中文为简体中文
echo.
echo  2. 重选黑沙的游戏根目录
echo.
:cho

set "psCommand="(new-object -COM 'Shell.Application')^.BrowseForFolder(0,'请选择黑沙的游戏根目录',0,0).self.path""
for /f "usebackq delims=" %%I in (`powershell %psCommand%`) do (
set "folder=%%I"
)

set choice=
set /p choice=  请输入数字编号:
if not "%choice%"=="" set choice=%choice:~0,1%
if /i "%choice%"=="1" goto tc2sc
if /i "%choice%"=="2" set choice=%choice:~0,1%
echo "%choice%" 无效选项，请重选
echo.
goto start

:tc2sc
set from_loc="%AppData%\bdocn_client\languagedata_cn.loc"
set to_loc="%folder%\ads\languagedata_tw.loc"
set from_font="%AppData%\bdocn_client\pearl.ttf"
set to_font="%folder%\prestringtable\font\pearl.ttf"

mkdir %folder%\ads\
copy /y %from_loc% %to_loc%
mkdir %folder%\prestringtable\font\
copy /y %from_font% %to_font%

goto end
endlocal
:end
pause

