# -*- coding:UTF-8 -*-
# Author:29447
# FileName:pythonProject1-__init__.py
# DateTime:2025/5/12 15:48
import re
# update

# re.I 忽略大小写
text="Cat cat cAt caT"
res=re.findall(r"cat",text,flags=re.I)
print(res) #['Cat', 'cat', 'cAt', 'caT']
res=re.findall(r"cat",text)
print(res) # ['cat']

# re.M 多行模式,注意针对^和$，匹配每一行的行头和行尾
text="cat\ncat\ncA\n caT"
res=re.findall(r"^cat",text,flags=re.M)
print(res) #['cat', 'cat']
res=re.findall(r"^cat",text)
print(res) # ['cat']

# re.X 为pattern添加注释
a=re.compile(
    r"""\d+ # the integral part
                \. # the decimal point
                \d* # some fractional part""",flags=re.X)
b=re.compile(r"\d+\.\d*")
print(a,b)