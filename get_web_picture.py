# -*- coding: UTF-8 -*-
import os,re,urllib,uuid

#首先定义云端的网页,以及本地保存的文件夹地址
urlPath='http://gamebar.com/'
localPath='d:\\pic'


#从一个网页url中获取图片的地址，保存在
#一个list中返回
def getUrlList(urlParam):
	urlStream=urllib.urlopen(urlParam)
	htmlString=urlStream.read()
	if( len(htmlString)!=0 ):
		patternString=r'http://.{0,50}\.jpg'
		searchPattern=re.compile(patternString)
		imgUrlList=searchPattern.findall(htmlString)
		return imgUrlList

		
#生成一个文件名字符串	
def generateFileName():
	return str(uuid.uuid1())

	
#根据文件名创建文件	
def createFileWithFileName(localPathParam,fileName):
	totalPath=localPathParam+'\\'+fileName
	if not os.path.exists(totalPath):
		file=open(totalPath,'a+')
		file.close()
		return totalPath
	

#根据图片的地址，下载图片并保存在本地	
def getAndSaveImg(imgUrl):
	if( len(imgUrl)!= 0 ):
		fileName=generateFileName()+'.jpg'
		urllib.urlretrieve(imgUrl,createFileWithFileName(localPath,fileName))





#下载函数
def downloadImg(url):
	urlList=getUrlList(url)
	for urlString in urlList:
		getAndSaveImg(urlString)
		
downloadImg(urlPath)
