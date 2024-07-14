#coding=utf-8 
import os
import os.path #文件夹遍历函数  
#获取目标文件夹的路径
filedir = 'output'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('iptv.txt','w')

 # 获取当前时间
        local_tz = pytz.timezone("Asia/Shanghai")
        now = datetime.now(local_tz)
        # now = datetime.now()
        output.write(f"\n更新时间,#genre#\n")
        output.write(f"{now.strftime("%Y-%m-%d")},url\n")
        output.write(f"{now.strftime("%H:%M:%S")},url\n")

#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath):
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()
#https://github.com/sosazi9847/Kowaryou
