#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import urllib.request
import re 

name=sys.argv
name=str(name[1])
print('读取的文件为',name)


with open("01234567tempout.md","w") as tempout:
    with open(name+".md") as f:
        num=1;
        for line in f:
            if line[0]=='!':
                newurl=str()
                newtype=str()
                onflag=0
                for letter in line:
                    if letter =='h':#启动读取URL
                        onflag=1
                    if onflag==1 and letter =='?':#读取URL完成，准备读取文件类型
                        onflag=2
                    if onflag ==3:#开始读取文件类型
                        onflag=4
                    if onflag==2 and letter =='=':#即将开始读取文件类型
                        onflag=3
                    if onflag==4 and (not letter.isalpha()):#文件类型读取完成
                        onflag=5

                    if onflag==1:
                        newurl=newurl+letter
                    if onflag==4:
                        newtype=newtype+letter
                print("转换中……")
                print(newurl)
                figname=name+'/'+str(num)+"."+newtype
                print(figname)
                urllib.request.urlretrieve(newurl , filename=figname)
                tempout.write("{% asset_img "+str(num)+"."+newtype+" %}")
                num=num+1
            else:
                tempout.write(line)

with open("01234567tempout.md","r") as tempout:
    with open(name+".md",'w') as f:
        for line in tempout:
            f.write(line)

os.remove("01234567tempout.md")


