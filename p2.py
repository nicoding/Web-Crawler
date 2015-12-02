#coding:UTF-8
import urllib2
import urllib
import re
import os

# 获取页面的html
def get_page(url):
        html=urllib2.urlopen(url).read()
        return html

#获取套图页面中指向最后一个图片的链接
def get_taotu_last_link(taotu_link):
        taotu_page=get_page(taotu_link)
        patt='<a href=\'[^\s]+?-\d+?\.html\'>\d+?</a>'
        taotu_last_link=re.findall(patt,taotu_page)[-1].split("'")[1]
        return taotu_last_link

#获取暂时的图片链接
def get_temp_image_link(taotu_last_link):
        taotu_last_page=get_page(taotu_last_link)
        patt='arrayImg\[\d\]="(http://[^\s]+?\.jpg)"'
        temp_image_link=re.findall(patt,taotu_last_page)
        return temp_image_link

#将图片下载并且保存到D盘的pic文件夹中
def save_image(image_links,dirname):
        global index
        path=unicode('D:\\pic\\'+dirname,'utf8')
        os.mkdir('%s' %(path))
        dirname=dirname.decode('utf8')
        for img_link in image_links:
                urllib.urlretrieve(img_link,'D:\\pic\%s\%d.jpg' % (dirname,index))
                print '%s has been downloaded and saved successfully.'%(img_link)
                index+=1

def start():
        print 'Waiting............'
        global taotu_links
        global index1
        for key in taotu_links:
                dirname='ding%d' % index1
                temp_taotu_last_link=get_taotu_last_link(key)
                taotu_last_link='http://www.22mm.cc/mm/'+key.split("/")[4]+'/'+temp_taotu_last_link
                temp_image_link=get_temp_image_link(taotu_last_link)
                image_links=[]
                for each in temp_image_link:
                        image_links.append(re.sub('big','pic',each))
                save_image(image_links,dirname)
                index1+=1


taotu_links=['http://www.22mm.cc/mm/qingliang/PmadPddddCdaiHPHH.html','http://www.22mm.cc/mm/qingliang/PmaHPJiPPHdaHPPde.html','http://www.22mm.cc/mm/qingliang/PmaddJHaaJeaiiPdi.html', 
'http://www.22mm.cc/mm/qingliang/PiPPaiJbbiiaHiCHi.html']
#links是存储套图链接信息的字典

#index是图片名称的索引
index=0
index1=0
start()