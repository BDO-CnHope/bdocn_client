# @Time    : 2021/07/06
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from re import sub,M

from time_template import time_template

def change_ui_font(path):
    time_template()
    print("replace_text.py >>> def change_ui_font(path)")

    with open(path, 'r+') as f:
        content = f.read()
        new_content = sub(r"(UIFontType =.*)", r"UIFontType = 1", content, flags = M)
        f.seek(0)
        f.write(new_content)
        f.truncate()
        f.close()

def change_lang_update_check(path):
    time_template()
    print("replace_text.py >>> def change_lang_update_check(path)")

    with open(path, 'r+') as f:
        content = f.read()
        new_content = sub(r"(RES =.*)", r"RES = _TW_", content, flags = M)
        f.seek(0)
        f.write(new_content)
        f.truncate()
        f.close()

def change_steam_lang_update_check(path):
    time_template()
    print("replace_text.py >>> def change_steam_lang_update_check(path)")

    with open(path, 'r+') as f:
        content = f.read()
        new_content = sub(r"(RES_STEAM =.*)", r"RES_STEAM = _TW_", content, flags = M)
        f.seek(0)
        f.write(new_content)
        f.truncate()
        f.close()