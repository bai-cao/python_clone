# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-__init__.py
# DateTime:2025/5/16 09:06

import re
import time

# (?P=name)
"""
string="<h1>Hello</h1>"
res=re.match(r"<(?P<tag>[a-zA-Z1-6]+?)>.*?</(?P=tag)>",string)
# re.PatternError: bad character in group name 'num\\d+' at position 4
print(res.group("tag"))
# print(tag)
if __name__ == '__main__':
    pass
"""

# re.subn()
"""
string="<h1>Hello World!</h1>"
# subn(pattern, repl, string, *args, count=0, flags=0)
res=re.subn(r"<(?P<tag>[a-zA-Z1-6]+?)>.*?</(?P=tag)>","html",string)
print(res)
"""

# span|start|end|group
string="<h1>Hello World!</h1>"
res=re.search("<(?P<tag>[a-zA-Z1-6]+?)>",string)
print(res) # <re.Match object; span=(0, 4), match='<h1>'>
print(res.group("tag")) # h1
print(res.start(),res.end()) # 0 4
print(res.span()) # (0, 4)

res=re.escape("<(?P<tag>[a-zA-Z1-6]+?)>")
print(res) # <\(\?P<tag>\[a\-zA\-Z1\-6\]\+\?\)>

string="<h1>Hello World!</h1>"
res=re.search(r"<([a-zA-Z1-6]+?)>",string)
print(res) # <re.Match object; span=(0, 4), match='<h1>'>
# print(res.string) # <h1>Hello World!</h1>
# print(res.pos)  # 0
# print(res.endpos) # 21  # ???不理解
print(res.lastgroup) # tag
# print(res.lastindex) # 1 # 当前只有1个捕获组，所以最后一个捕获组索引是1


# print(res.groupdict()) # {'tag': 'h1'}
# # matchObj.groupdict(default=None)
# # 未命名的分组，则不返回
# # 命名分组没有匹配内容，则键值是default参数的值
#
pattern=r"(?P<area_code>\d{3})-(\d+)-(\d+)"
text="400-881-8611"
res=re.search(pattern,text)
# print(res.expand(r"(\g<area_code>) \2\3")) # (400) 8818611
print(res.lastgroup)

# 清除缓存
re.purge() # Clear the regular expression caches

import time,datetime
print(time.time()) # 1747627002.7477674
string=str(datetime.datetime.now()).split(".")[0] # 2025-05-19 11:57:37.801868
print(string) # 2025-05-19 12:02:54
print(re.sub(r"(\d+)-(\d+)-(\d+)",r"\1/\2/\3",string))
