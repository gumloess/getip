import re
import shutil
import os
import glob
import socket
import ftplib 
from ftplib import FTP 

# The script is for finding lost tester's ip
# Author: Malvin
# Rev 0.10	 7/14/2017

testname="b670"
myfile = testname+".txt"
myhost = '10.71.32.138'  
mydir = '/home/kei/MalvinCui/testerip'  
myname = socket.getfqdn(socket.gethostname())
# print(myname)
myhname = myname.split('.')[0]
# print(myhname)
myaddrtemp = socket.gethostbyname_ex(myhname)
myaddr = myaddrtemp[2][0]
# print(myaddr)

myuser = 'kei'
mypasswd = 'keiuser'


f=open(myfile,"w+")
li=["It's come from "+testname+"\n","ip="+myaddr+"\n","dnsname="+myname+"\n"]
f.writelines(li)
f.close()


ftp = FTP()  
timeout = 30  
port = 21  
ftp.connect(myhost,port,timeout)					 # 连接FTP服务器  
ftp.login(myuser,mypasswd) 							 # 登录
ftp.cwd(mydir)    									 # 设置FTP路径  
#ftp.delete(myfile) 
ftp.storbinary('STOR %s'%myfile, open(myfile, 'rb'))	 # 上传FTP文件 
ftp.quit()                 						     # 退出FTP服务器 









