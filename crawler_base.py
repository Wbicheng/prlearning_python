from urllib.request import urlopen
from bs4 import BeautifulSoup;
import re;#使用正则表达式进行网页内容匹配
html= urlopen('https://www.runoob.com/regexp/regexp-syntax.html').read().decode('utf-8');
#用正则表达式进行匹配
res=re.search(r'href="(.*?)"',html);
print(res.group());
#用beautifulsoup4
#根据html内容进行匹配
soup=BeautifulSoup(html,features="lxml");#选择解析方式feature
print(soup.title);#根据标签tag输出，不需要再写正则表达式
all_href=soup.find_all('link');#找到所有link标签的内容
for l in all_href:
    print(l['href']);#找到所以link tag的属性为href的内容

#根据css的class进行匹配
jan=soup.find('ul',{"class":"jan"});#选择ul css属性为jan   {}里写属性  没有all只返回第一个
d_jan=jan.find_all("li");#在u1里查找里面的的li标签
for f in d_jan:
    print(f.get_text());#get_text只显示内容 不含标签

#bs4使用正则表达式进行匹配
links=soup.find_all('a',{'href':re.compile("https://.*")});#找标签为a  属性href的值符合正则表达式的内容
for l in links:
    print(l['href'])

#requests模块的post和get
#post：与服务器有数据交互，如登录等操作
#get：与服务器无数据交互，单纯得到网页信息
#在登录状态下，下次访问时需要用cookie，若不使用cookie 可用session



