import pyautogui
import time
import pyperclip

import win32api
import win32gui
from win32con import WM_INPUTLANGCHANGEREQUEST

# 切换中英文输入法
def change_language(language="EN"):
    """
    切换语言
    :param language: EN––English; ZH––Chinese
    :return: bool
    """
    LANGUAGE = {
        "ZH": 0x0804,
        "EN": 0x0409
    }
    hwnd = win32gui.GetForegroundWindow()
    language = LANGUAGE[language]
    result = win32api.SendMessage(
        hwnd,
        WM_INPUTLANGCHANGEREQUEST,
        0,
        language
    )
    if not result:
        return True

# 判断字符串是否包含中文
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


if __name__ == '__main__':

    time.sleep(5)  # 延迟5秒

    # 文件路径
    # file_path = './xin/index.html'
    file_path = r'E:\Desktop\auto_send.py'

    # 实例化pyautogui
    au = pyautogui

    # 实例化pyperclip
    pe = pyperclip

    # 读取文件
    with open(file_path,'r',encoding='utf-8')as fp:
        # 读取所有内容  得到以行为单位的一个list
        content = fp.readlines()

        # 遍历list内容
        for i in content:
            # 控制台输出查看
            # 判断内容是否包含中文
            if is_Chinese(i):
                change_language()

                # print('有中文！！！！', i)

                # 复制每一行
                pe.copy(i)

                # 查看复制的内容
                # print(r"'ctrl','v' 内容：",pe.paste())

                ## pyautogui.typewrite() 写入方式    写入不了中文
                # pyautogui.typewrite(pe.paste(),'0.01')

                # 采用键盘组合键 粘贴复制的内容
                au.hotkey('ctrl','v')
            else:
                # print('无无无无无无无无无无无无',i)
                change_language()

                au.typewrite(i,'0.01')
    change_language('ZH')






























