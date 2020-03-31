import urllib

import requests;
from bs4 import BeautifulSoup;
import os;
import re;

class imgSpider():
    header={#不加也可以
    'Host': 'image.baidu.com',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage',#可以不加
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    };
    reseach='风景';
    def __init__(self,reseach):
        self.reseach=reseach;
    #spider1 对于静态网页可以提高requests打开url，bs进行解析，再用一些标签信息进行查找得到
    #但是对于动态网页 如网页url不变，但是内容变化，则使用json进行数据交互，可以参考spider3的做法
    def spider(self):
        os.makedirs('./{}'.format(self.reseach),exist_ok=True);#创建文件夹，目标存在时不会触发异常#
        a=1;#图片计数
        img_src_urls=set();#存储图片地址的集合，去重
        for i in range(1,3):#翻四页，会重复
            #网址
            url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1585496170060_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1585496170062%5E00_965X674&sid=' \
                '&word={}&pn={}'.format(self.reseach,str(i));
            html=requests.get(url,headers=self.header).content.decode('utf-8'); #加不加header都可以，获取url内容
            soup=BeautifulSoup(html,'lxml');#拿网页内容content解析
            img_li=soup.find_all('li',{'class':'imgitem'});#找到内含图片的标签

            for img in img_li:
                imgs=img.find_all('img');#在标签a中找到所有<img>
                for img_url in imgs:
                    img_src=img_url['data-imgurl'];
                    img_src_urls.update([img_src]);#集合update增加多项,需要加上中括号

        print('爬取到图片共{}张'.format(len(img_src_urls)));
        # for img_src_url in  enumerate(img_src_urls, 1):#第一个为空，从第一个索引开始 会以字典的形式读取
        for img_src_url in img_src_urls:
            r=requests.get(img_src_url);#请求获取图片  不加header！
            # img_name=img_src_url.split('/')[-1];#取末尾为img名
            img_name=self.reseach+str(a)+'.jpg';
            with open('./{}/{}'.format(self.reseach,img_name),'wb') as f:
                f.write(r.content);#写入内容
                a+=1;
            print('Saved '+img_name);
    #除了用标签进行查找外，可以进行在网页用inspect 中找到thumbURL，也是文件地址，此时不能用bs解析，可能因为没有thumb对应的标签
    def spider2(self):
        os.makedirs('./{}'.format(self.reseach), exist_ok=True);  # 创建文件夹，目标存在时不会触发异常#
        a = 1;  # 图片计数
        img_src_urls = set();  # 存储图片地址的集合，去重
        for i in range(1, 3):
            # 网址
            url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1585496170060_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1585496170062%5E00_965X674&sid=' \
                  '&word={}'.format(self.reseach);
            html = requests.get(url, headers=self.header).content.decode('utf-8');  # 加不加header都可以，获取url内容
            imgs = re.findall('{"thumbURL":"(.*?)",', html)#此句用bs搜索不到,因为从html里可以不在标签里
            # img_src_urls.update(set(imgs));  # findall得到一个list，转换为set
            # soup = BeautifulSoup(html, 'lxml');  # 拿网页内容content解析
            # imgs=soup.find_all('li',{"data-thumburl":re.compile("(.*?)")});
            img_src_urls.update(set(imgs));  # findall得到一个list，转换为set
        print('爬取到图片共{}张'.format(len(img_src_urls)));
        for img_url in img_src_urls:
            r = requests.get(img_url);  # 请求获取图片  不加header！
            # img_name=img_src_url.split('/')[-1];#取末尾为img名
            img_name = self.reseach + str(a) + '.jpg';
            with open('./{}/{}'.format(self.reseach, img_name), 'wb') as f:
                f.write(r.content);  # 写入内容
                a += 1;
            print('Saved ' + img_name);
    #网页地址url不变，但是内容会变化，则是使用json进行数据交换，
    #查看方法参考https://www.cnblogs.com/sjfeng1987/p/9902077.html
    #网址url不变，但是内容会变化
    #查看network-xdr(负责json请求)-header-General-Request URl 可知Request URl 会变化（一般是pn网页，word关键词变化），打开此url可以找到一些文件网址thumbUrl
    #因此可以用spider2的方法进行爬取
    # json里Headers里的general中的URL的变化只有pn和一些其他参数
    def spider3(self,pn):

        os.makedirs('./{}'.format(self.reseach),exist_ok=True);#创建文件夹，目标存在时不会触发异常#
        a=1;#图片计数
        img_src_urls=set();#存储图片地址的集合，去重
        keyword_quote = urllib.parse.quote(self.reseach);
        for i in range(pn):#翻四页，会重复
            #取json中 request URL里的网址
            url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&' \
                'lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&i' \
                'stype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1585646849510='.format(keyword_quote,keyword_quote,str(i*30));#m每页30张图片
            html = requests.get(url, headers=self.header).content.decode('utf-8');  # 加不加header都可以，获取url内容
            # print(html);
            imgs = re.findall('"thumbURL":"(.*?)",',html)  # 此句用bs搜索不到,因为从html里可以不在标签里
            img_src_urls.update(set(imgs));  # findall得到一个list，转换为set
        print('爬取到图片共{}张'.format(len(img_src_urls)));
        for img_url in img_src_urls:
            r = requests.get(img_url);  # 请求获取图片  不加header！
            # img_name=img_src_url.split('/')[-1];#取末尾为img名
            img_name = self.reseach + str(a) + '.jpg';
            with open('./{}/{}'.format(self.reseach, img_name), 'wb') as f:
                f.write(r.content);  # 写入内容
                a += 1;
            print('Saved ' + img_name);


if __name__=='__main__':#若被引用不执行，此时__name__不等于__main__
    print('请输入爬取关键词：');
    reseach=input();
    print("请输入爬取页数(一页约30张):");
    pn=int(input());
    imgspider=imgSpider(reseach);
    imgspider.spider3(pn);#爬取2页内容