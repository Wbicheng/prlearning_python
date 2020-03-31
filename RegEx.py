import re;
x=r'r[au]n';#r表示正则表达式，没有r也可以
print(re.search(x,'ran run '));
print(re.search(x,'ran run ').group());#group只输出匹配内容，无其他信息

#寻找所有匹配
print(re.findall(r"r[au]n","ran run"));#

# 使用group(index)输出匹配结果也只是括号内的内容
#若为group() 则输出完整匹配内容
match=re.search(r"(\d+),Date: (.+)","id:1212,Date: Feb/12/2101");
print(match.group());#将匹配到的结果直接打印出来 \d匹配数字  +不限制个数 .任意字符
print(match.group(1));#将匹配的第一个内容输出  1212
print(match.group(2));#将匹配的第二个内容输出  Feb/12/2101

#当匹配内容多时 可以分配标签 ?P<>
match=re.search(r"(?P<id>\d+),Date: (?P<date>.+)","id:1212,Date: Feb/12/2101");
print(match.group());#将匹配到的结果直接打印出来 \d匹配数字  +不限制个数 .任意字符
print(match.group('id'));#将id匹配的内容输出  1212
print(match.group('date'));#将date匹配的输出  Feb/12/2101

#替换
print(re.sub(r"r[au]n","swim","i  run"));#得到i  swim

#分裂
print(re.split(r"[,;]","a,b;c")); #以中间的符号分隔
