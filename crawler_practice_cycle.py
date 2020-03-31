import random;
from urllib.request import urlopen;
from bs4 import BeautifulSoup;
import re;

base_url="https://baike.baidu.com";#url进行分离，便于不断更新
history=["/item/%E6%9D%8E%E5%BD%A6%E5%AE%8F/125160?fr=aladdin"];

for i in range(20):#爬取20次  会报错，可能爬到一些地方没有url连接

    url=base_url+history[-1];#一直取最新的网址
    html=urlopen(url).read().decode("utf-8");#打开url
    soup=BeautifulSoup(html,features="lxml");#bs进行解析
    print('爬取次数 '+str(i)+': '+soup.title.get_text());#显示当前网页内容
    #print(soup.title.get_text());
    his_alls=soup.find_all('a',{'target':'_blank','href':re.compile("/item/(%.{2})+$")})#结合tag的属性进行筛选  +为重复1次以上，$为前面内容结尾
 #   for l in his_alls:
 #       print(l['href']);

    if len(his_alls)!=0:
        history.append(random.sample(his_alls,1)[0]['href'])#随机选择一个
    else:
        history.pop();#若没有内容 将当前去除，向上一层寻找
   # print('爬取次数 '+str(i)+': '+history[-1]);