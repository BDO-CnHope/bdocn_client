@echo off
:start
setlocal
setlocal enabledelayedexpansion
cls
echo.
echo   ��ɳ̨����ת��ű�By Naunter@20210319
echo  ==============================================================
echo   ִ�б��ű�ǰ������ʹ�ú�ɫɳĮ��������(bdocn_client)���غ�������
echo  ==============================================================
echo   ���غ�ɫɳĮ��������(bdocn_client)��
echo   ·��1: https://github.com/BDO-CnHope/bdocn_client/releases
echo   ·��2: https://share.weiyun.com/BtJgJGUX
echo ==============================================================
echo   �˽ű�������̨����ɳ�滻��������Ϊ�������ġ�Ҫ���
echo   ��ɫɳĮ��������(bdocn_client)��ʹ��
echo  ==============================================================
echo.
echo   1. �����к�ɫɳĮ��������(bdocn_client)����(����)��������
echo.
echo   2. Ȼ�����д˽ű�
echo.
echo   3. ѡ�񡰺�ɳ����Ϸ��Ŀ¼��
echo      ������C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online\
echo.
echo   4. ѡ���滻��������Ϊ�������ġ�
echo.
echo  ==============================================================
echo.
echo  1. �滻��������Ϊ��������
echo.
echo  2. ��ѡ��ɳ����Ϸ��Ŀ¼
echo.
:cho

set "psCommand="(new-object -COM 'Shell.Application')^.BrowseForFolder(0,'��ѡ���ɳ����Ϸ��Ŀ¼',0,0).self.path""
for /f "usebackq delims=" %%I in (`powershell %psCommand%`) do (
set "folder=%%I"
)

set choice=
set /p choice=  ���������ֱ��:
if not "%choice%"=="" set choice=%choice:~0,1%
if /i "%choice%"=="1" goto tc2sc
if /i "%choice%"=="2" set choice=%choice:~0,1%
echo "%choice%" ��Чѡ�����ѡ
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

