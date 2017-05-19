# user/bin/env python
# -*- coding=utf-8 -*-

import re,random,requests,time

class Requests:
    def __init__(self):
        """获取user-agent列表"""
        self.ua_list=["Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221",
                 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
                 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
                 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
                 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7"]
        """获取ip"""
        ip_url="http://www.ip181.com/"
        self.ip_list=[]
        res=requests.get(ip_url).text
        for i in re.findall(r'<(tr|tr class="warning")>.*?<td>(.*?)</td>', res, re.S):
            #print(i[-1])
            self.ip_list.append(i[-1].strip())

    def get(self,web_url,timeout,proxy=None,num_retries=6):
        print("开始获取：",web_url)
        UA=random.choice(self.ua_list)
        headers={"User-Agent":UA}
        if proxy==None:
            try:
                return requests.get(web_url,headers=headers,timeout=timeout)
            except:
                if num_retries>0:
                    time.sleep(10)
                    print("获取网页出错，10s后将倒数第"+num_retries+"次获取")
                    return self.get(web_url,timeout,num_retries-1)
                else:
                    print("开始使用代理")
                    time.sleep(10)
                    IP=str(random.choice(self.ip_list))
                    proxy={"http":IP}
                    return self.get(web_url,timeout,proxy,num_retries-1)
        else:
            try:
                print("开始使用代理")
                IP = str(random.choice(self.ip_list))
                proxy = {"http": IP}
                return requests.get(web_url, proxies=proxy,timeout=timeout)

            except:
                if num_retries>0:
                    time.sleep(10)
                    IP = str(random.choice(self.ip_list))
                    proxy = {"http": IP}
                    print("正在更换代理，10s后将倒数第" + num_retries + "次获取")
                    print("当前代理是：",proxy)
                    return self.get(web_url,timeout,proxy,num_retries-1)
                else:
                    print("代理也不好使了！取消代理")
                    return self.get(web_url,3)

get_header=Requests()










