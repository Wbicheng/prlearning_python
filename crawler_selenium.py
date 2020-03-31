#selenuim类似按键精灵  需要pip安装，之后需要下载浏览器驱动并在windows环境变量Path进入路径才能使用，若在pycharm中使用，将驱动放入python根目录即可
#先用chrome插件Kataton Recorder得到访问流程，export（python2）生成访问流程代码
import unittest, time, re;
from selenium import webdriver;
driver=webdriver.Chrome();#打开chrome

#复制访问流程代码  点击网页进行跳转可以，一些链接不行
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E6%AD%8C%E6%89%8B2020%E5%9C%A8%E7%BA%BF%E8%A7%82%E7%9C%8B&oq=%25E8%25A7%2586%25E9%25A2%2591%25E8%25A7%25A3%25E6%259E%2590&rsv_pq=e5edadfe000cdc48&rsv_t=21ffZsDc4lY6vTXey4hsrA6Vm8Wq2zviVu4thZEJMIOopM2BjLCDhuk1Ifs&rqlang=cn&rsv_enter=0&rsv_dl=tb&inputT=5408&rsv_sug3=84&rsv_sug1=41&rsv_sug7=100&rsv_sug2=0&rsv_sug4=5408")
driver.find_element_by_xpath("//div[@id='1']/div/div[2]/div").click()
driver.find_element_by_xpath("//div[@id='3']/div/article/section/div/div[2]/div/div[2]/div/div").click()
driver.find_element_by_xpath("//div[@id='3']/div/article/section/div/div[2]/div/div[2]/div/div[3]/div/ul/li[4]").click()
driver.find_element_by_xpath("//img[contains(@src,'https://dss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=2919666388,1968199383&fm=58&app=83&f=JPEG?w=161&h=112&s=3AA1218A64073AF11884438D0300B09F')]").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
driver.find_element_by_xpath("//body/txpdiv/txpdiv[2]").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
driver.find_element_by_xpath("//div[@id='head']/div/div/div").click()
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys(u"视频解析")
driver.find_element_by_id("form").submit()
driver.find_element_by_link_text(u"全民解析-vip视频在线解析").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]
driver.find_element_by_id("url").click()
driver.find_element_by_id("url").clear()
driver.find_element_by_id("url").send_keys("https://v.qq.com/x/page/l00338s4qbu.html")
driver.find_element_by_xpath("(//button[@id='bf'])[2]").click()

driver.close();