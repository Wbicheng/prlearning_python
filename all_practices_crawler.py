import requests;
import time;
import json;
from bs4 import BeautifulSoup ;
import os;
import re;
from urllib.request import urlretrieve
import urllib
import html as hl;

#此文件为一些练习例子，具体解释可以参考img_spider 解释详细些

#爬百度  检测反爬 没有似乎也能爬  加入headers表明身份
# header={
# 'Host': 'www.baidu.com',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# };
# url='https://www.baidu.com/';
# r=requests.get(url,headers=header).content.decode('utf-8');#用headers进行反爬，需要解码
# soup=BeautifulSoup(r,'lxml');
# a=soup.find_all('head');
# print(a);


# #从学习网站上指定url进行下载：
# os.makedirs('./img/',exist_ok=True);#创建文件，目标存在时不会触发异常
# #网页源码查找图片URL
# img_url='https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png';
# #可以使用urllib中的模块下载，也可以使用request
# r=requests.get(img_url).content;#得到网页内容
# with open('./img/img.jpg','wb') as f:
#     f.write(r);#向文件夹中写入内容

# #练习 从国家地理上爬取图片 无法从百度图库爬取？
# header={ #对于国家地理，不需要加入请求头
# 'Host': 'image.baidu.com',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# };
# url='http://www.ngchina.com.cn/animals/';
# html=requests.get(url).content.decode('utf-8'); #获取url内容
# soup=BeautifulSoup(html,'lxml');#解析
# img_li=soup.find_all('li',{'class':'mod_w'});#找到内含图片的标签
# print(img_li);
# for img in img_li:
#     imgs=img.find_all('img');#在标签a中找到所有<img>
#     for imgurl in imgs:
#         img_url=imgurl['src'];
#         r=requests.get(img_url);#请求获取图片
#         img_name=img_url.split('/')[-1];#取末尾为img名
#         with open('./img/%s'%img_name,'wb') as f:
#             f.write(r.content);#写入内容
#         print('Saved '+img_name);

#练习 从百度图库爬取，有些关键词涉及到广告什么的无法爬取
header={
'Host': 'image.baidu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
};
for i in range(1,2):
    #网址
    url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1585496170060_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1585496170062%5E00_965X674&sid=&word=%E7%90%AA%E4%BA%9A%E5%A8%9C';
    html=requests.get(url,headers=header).content.decode('utf-8'); #加不加header都可以，获取url内容
    soup=BeautifulSoup(html,'lxml');#拿网页内容content解析
    img_li=soup.find_all('li',{'class':'imgitem'});#找到内含图片的标签
    for img in img_li:
        imgs=img.find_all('img');#在标签a中找到所有<img>
        for img_url in imgs:
            img_src_url=img_url['data-imgurl'];
            # img_src_url = hl.unescape(img_src_url);#反爬中将&转义成&amp;导致无法找到准确图片地址，将其进行转义
            # print(img_src_url);
            r=requests.get(img_src_url);#请求获取图片  不加header！
            img_name=img_src_url.split('/')[-1];#取末尾为img名
            # img_name=str(a)+'.jpg';
            with open('./img/%s'%img_name,'wb') as f:
                f.write(r.content);#写入内容
            print('Saved '+img_name);


# #练习：九游上游戏名
# url='http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-1-2.html';
# html=requests.get(url).content.decode('utf-8');#请求网页
# soup=BeautifulSoup(html,'lxml');#解析
# ng_uls=soup.find_all(attrs={'class':'ptlist ptlist-pc'});#通过标签的属性查找，省略了标签tag
# for ng_ul in ng_uls:
#     ng_divs=ng_ul.find_all('div',{'class':'c2'});
#     for ng_div in ng_divs:
#         a_s=ng_div.find_all('a',{'target':'_blank'});
#         for a_ in a_s:
#             print(a_.text);#返回标签内容

#练习：拉勾网职位 :爬不到... 需要从ajax里爬取数据
# header={
# 'Referer': 'https://www.lagou.com/jobs/list_%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89?labelWords=&fromSearch=true&suginput=',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
# 'Accept': 'application/json, text/javascript, */*; q=0.01'
# }
# url='https://www.lagou.com/jobs/list_%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89?labelWords=&fromSearch=true&suginput=';
# html=requests.get(url,headers=header).content.decode('utf-8');
# soup=BeautifulSoup(html,'lxml');
# pos_divs=soup.find_all('li',{'class':'con_list_item default_list'});
# print(pos_divs);
# for pos_div in pos_divs:
#     pos_h3=pos_div.find_all('h3');
#     print(pos_h3[0].text);


#练习 爬取拉勾网职位信息
# 翻页时url没有变换，使用json传递数据，故从json爬取数据
# 一直反映操作频繁，需要post和相关cookie来请求
#在network中XHR的header里找General里的目标url  XHR加载的是AJAX请求
# def main():
#     # 在network中XHR的header里的requests headers里找header所需要信息
#     header={
#     'Referer': 'https://www.lagou.com/jobs/list_%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89?labelWords=&fromSearch=true&suginput=',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#     'Accept': 'application/json, text/javascript, */*; q=0.01'
#     }
#     url_start = "https://www.lagou.com/jobs/list_%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89?labelWords=&fromSearch=true&suginput="#用搜索页的网址url
#     url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false';#在network中XHR的header里找General里的目标url
#     s = requests.Session();
#     s.get(url_start, headers=header);  # 请求首页获取cookies
#     cookie = s.cookies;  # 为此次获取的cookies
#     for x in range(1,5):
#         #由XDR中的header的from data可以知道要求的数据
#         data = {
#             'first': 'true',
#             'pn': str(x),
#             'kd': '计算机视觉'
#         }
#         # s = requests.Session();
#         # s.get(url_start, headers=header);  # 请求首页获取cookies
#         # cookie = s.cookies;  # 为此次获取的cookies
#         response = s.post(url, data=data, headers=header, cookies=cookie);  # 获取此次文本
#         # time.sleep(5)
#         text=response.json();
#         # text = json.loads(response.text);#效果同上
#         list_con = text['content']['positionResult']['result'];
#         for pos in list_con:
#             print(pos['positionName'], pos['companyShortName'], pos['workYear'], pos['salary'])
#
# if __name__ =='__main__':
#     main();




#参考CSDN例子
# def main():
#     url_start = "https://www.lagou.com/jobs/list_运维?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="#随意相关网站即可
#     url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=成都&needAddtionalResult=false"
#     headers = {
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#     }
#     for x in range(1, 5):
#         data = {
#             'first': 'true',
#             'pn': str(x),
#             'kd': '计算机视觉'
#                 }
#         s = requests.Session()
#         s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
#         cookie = s.cookies  # 为此次获取的cookies
#         response = s.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false', data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
#         time.sleep(5)
#         response.encoding = response.apparent_encoding
#         text = json.loads(response.text)
#         info = text["content"]["positionResult"]["result"]
#         for i in info:
#             print(i["companyFullName"])
#             companyFullName = i["companyFullName"]
#             print(i["positionName"])
#             positionName = i["positionName"]
#             print(i["salary"])
#             salary = i["salary"]
#             print(i["companySize"])
#             companySize = i["companySize"]
#             print(i["skillLables"])
#             skillLables = i["skillLables"]
#             print(i["createTime"])
#             createTime = i["createTime"]
#             print(i["district"])
#             district = i["district"]
#             print(i["stationname"])
#             stationname = i["stationname"]
#
# if __name__ == '__main__':
# 	main()

#参考爬取百度背包图片例子
# def get_page_html(page_url):
#     headers = {
#         'Referer': 'https://image.baidu.com/search/index?tn=baiduimage',
#         'User - Agent': 'Mozilla / 5.0(Macintosh;IntelMacOSX10_13_1) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.132Safari / 537.36'
#     }
#     try:
#         r = requests.get(page_url, headers=headers)
#         if r.status_code == 200:
#             r.encoding = r.apparent_encoding
#             return r.text
#         else:
#             print('请求失败')
#     except Exception as e:
#         print(e)
#
# # 从文本中提取出真实图片地址
# def parse_result(text):
#     url_real = re.findall('"thumbURL":"(.*?)",', text)
#     return url_real
#
# # 获取图片的content
# def get_image_content(url_real):
#     headers = {
#         'Referer': url_real,
#         'User - Agent': 'Mozilla / 5.0(Macintosh;IntelMacOSX10_13_1) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.132Safari / 537.36'
#
#     #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Sa
# #         else:
# #             print('请求失败')
# #     except Exception as e:fari/537.36'
#     }
#     try:
#         r = requests.get(url_real, headers=headers)
#         if r.status_code == 200:
#             r.encoding = r.apparent_encoding
#             return r.content
#         print(e)
# # 将图片的content写入文件
# def save_pic(url_real, content):
#
#     root = './img/'
#
#     path = root + url_real.split('/')[-1]
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#     #if not os.path.exists(n):
#
#         with open(path, 'wb') as f:
#             f.write(content)
#             print('图片{}保存成功，地址在{}'.format(url_real, path))
#             n = +1
#     else:
#         pass
#
# # 主函数
# def main():
#     #keyword = input('请输入你要查询的关键字: ')
#     #keyword_quote = urllib.parse.quote(keyword)
#     #keyword_quote = urllib.parse.quote(input('输入：'))
#
#     #depth = int(input("请输入要爬取的页数(每页30张图): "))
#     for i in range(30):
#         #url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&word={}&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&step_word={}&pn={}&rn=30&gsm=1e&1541136876386='.format(
#         #    keyword_quote, keyword_quote, i * 30)
#         #url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1568946752063_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=背包'
#         url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1585496001782_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1585496001784%5E00_965X674&sid=&word=%E8%83%8C%E5%8C%85';
#         html = get_page_html(url)
#         real_urls = parse_result(html)
#         for real_url in real_urls:
#             content = get_image_content(real_url)
#             save_pic(real_url, content)
#
#
#
#
# # 函数入口
# if __name__ == '__main__':
#     main()