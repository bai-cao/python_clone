# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-re_20250512
# DateTime:2025/5/12 16:12

import re
# re.compile
"""
pattern=re.compile(r"\d+\.\d+") # 匹配浮点数; # re.compile('\\d+\\.\\d+')
res=pattern.search("This is $5.12.") # <re.Match object; span=(9, 13), match='5.12'>
print(res.group()) # 5.12
"""

# re.fullmatch
# re.split
# def split(pattern, string, *args, maxsplit=0, flags=0):
#     Split the source string by the occurrences of the pattern,
#     returning a list containing the resulting substrings.  If
#     capturing parentheses are used in pattern, then the text of all
#     groups in the pattern are also returned as part of the resulting
#     list.  If maxsplit is nonzero, at most maxsplit splits occur,
#     and the remainder of the string is returned as the final element
#     of the list.
string="This is my  string"
"""
res=re.split(r"\s+", string) # 按\s+即空白字符分隔
print(res) # ['This', 'is', 'my', 'string']
res=re.findall(r"\S+", string) # 匹配非空白字符；与上述结果等同
print(res) # ['This', 'is', 'my', 'string']
res=re.split(r"\s+", string,maxsplit=1) # 分隔1次；超出后按最大次数分隔
print(res) # ['This', 'is my  string']
"""
res=re.finditer(r"\S+", string)
print(res) # <callable_iterator object at 0x0000029382A600D0>
for match in res:
    # print(match) # <re.Match object; span=(0, 4), match='This'>
    print(match.group()) # This # is # my # string

re.fullmatch()