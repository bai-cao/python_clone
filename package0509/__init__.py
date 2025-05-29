# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-__init__.py
# DateTime:2025/5/9 18:05

import re

string="abcdefgh12345"

# re.match
"""
# def match(pattern, string, flags=0):
#     Try to apply the pattern at the start of the string, returning
#     a Match object, or None if no match was found.
# 从起始位置匹配模式。匹配失败返回None,否则返回对象Match object
res=re.match(r"(\w{2,})(\d+)",string)
# 匹配成功<re.Match object; span=(0, 1), match='a'>
print(res)

if res: # 非None
    print(res.groups())
    
"""

# re.search
# 扫描整个字符串并返回第一个成功的匹配
"""
res=re.search(r"(?P<letters>[a-zA-Z]{2,3})(?P<num>\d+?)",string)
print(res) # <re.Match object; span=(5, 9), match='fgh1'>
if res:
    print(res.groups()) # ('fgh', '1')
    print(res.group(1)) # fgh
    print(res.group(2)) # 1
    print(res.group("letters"),res.group("num")) # fgh 1
"""

# re.findall
"""
# 扫描整个字符串并以列表形式返回所有匹配成功的子串
res=re.findall(r"(?P<letters>[a-zA-Z]{2,3})(?P<num>\d+?)",string)
print(res) # [('fgh', '1')]
res=re.findall(r"\d{9}",string)
print(res) # ['1', '2', '3', '4', '5']  # ['12', '34']
"""

# re.sub
"""
res=re.sub(r"\d{9}","abc",string)
# 若无匹配项，count非0，报错DeprecationWarning: 'count' is passed as positional argument(因为没有那么多替换次数)
# 若无匹配项，count=0,则返回原来字符串
print(res) # abcdefghabc2345
def jia1(matchobj):
    # print(matchobj)  # <re.Match object; span=(8, 9), match='1'>
    match_res=matchobj.group()
    if len(match_res)>1: # 报错TypeError: object of type 're.Match' has no len()
        string=''.join([chr(ord(i)+1) for i in match_res])
        # print(string)
        return string # ascii值+1，返回对应的字符
    return chr(ord(match_res)+1)
res=re.sub(r"\d{4}",jia1,string,)
print(res)
"""