# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-replace_string
# DateTime:2025/6/2 21:38
import re

# 修改以便第2次测试补丁
def replace_string(olds:str,news:str=""):
    """
    添加函数说明，以便测试补丁
    :param olds:
    :param news:
    :return:
    """
    with open("replace.txt","r+",encoding="utf-8") as f:
        txt=f.read()
    replText=re.sub(olds,news,txt) # 替换
    with open("replace.txt","w",encoding="utf-8") as f:
        f.write(replText)

if __name__ == '__main__':
    old_str1="LAPTOP-wlh MIN" # 待替换string
    # old_str1=r"] (main)"
    old_str2="/py/Python/PycharmProjects/gitproject"
    new_str=""
    replace_string(old_str1, new_str)
    replace_string(old_str2,new_str)
