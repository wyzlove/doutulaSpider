#-*- coding:utf-8 -*-
#user/bin/env python

import  requests,re,os
from Requests import get_header

class Download:

    def get_img_html(self,web_url):
        url_res = get_header.get(web_url,3).text
        for i in re.findall(r'<a class="list-group-item" href="(.*?)">',url_res):
            self.save_img(i)

    def save_img(self,group_html):
        html_res= get_header.get(group_html,3).text
        group_name=re.findall(r'<meta property="og:title" content="(.*?)"/>',html_res)[0].strip()
        self.makedir(group_name)
        os.chdir(os.path.join(r"C:\Users\94481\Desktop\doutula\斗图啦", group_name))
        for i in re.findall(r'alt=(.*?) onerror="this.src=(.*?)">', html_res):
            img_url= "https:"+re.sub(r"'",'',i[1]) #去首尾引号
            img_name= re.sub(r"'",'',i[0]).strip('"')
            self.download_img(img_url,img_name)


    def download_img(self,url,name):
        res=get_header.get(url,3).content
        print("开始下载"+name,"url为"+url)
        with open(name+".jpg","wb") as fp:
            fp.write(res)

    def main(self,i):
        for n in range(1,i):
            html="https://www.doutula.com/article/list/?page={}".format(n)
            print("——————————————————————开始下载第"+str(n)+"页图片————————————————————")
            self.get_img_html(html)

    def makedir(self,path):
        os.chdir(r"C:\Users\94481\Desktop\doutula\斗图啦")
        isExist=os.path.exists(os.path.join(r"C:\Users\94481\Desktop\doutula\斗图啦",path))
        if not isExist:
            print("*****************"+'开始新建文件夹'+path+"********************")
            os.makedirs(os.path.join(r"C:\Users\94481\Desktop\doutula\斗图啦",path))
            os.chdir(r"C:\Users\94481\Desktop\doutula\斗图啦")
            return True
        else:
            print( path+'该文件夹已存在')
            return False

if __name__=="__main__":
    download= Download()
    download.main(3)








