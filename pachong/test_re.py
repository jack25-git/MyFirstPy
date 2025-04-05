import re

obj=re.compile(r"\d+")

ret=obj.finditer("我的科技馆1264，我i哦还不够好79544")
for i in ret:
    print(i.group())