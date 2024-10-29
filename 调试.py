import csv
import pandas as pd
import re

#单位均是国际单位
#弹性模量
E=206*1000000000
#短斜杆面积
S1=144*8*0.000001
#短斜横长度
L1=144*0.001
#横，竖杆面积
S2=100*8*0.000001
#横，竖杆长度
L2=0.1
#设置斜，横/竖短杆判断列表，1，2，7，4为横/竖杆；3，5为斜杆斜为真
bia=[0,0,1,0,1,0]
#面积列表
Sm=[S2,S2,S1,S2,S1,S2]
#长度列表
Lm=[L2,L2,L1,L2,L1,L2]
#定义计算应变量函数
def Ff(Xuhao:int,YingBianLu:float):
    Fy=E*Sm[Xuhao]*YingBianLu #进行单位转化
    return Fy

def XiDuShCh(Xuhao:int,length:float):
    e=(length/Lm[Xuhao])*0.000001*(0.001)#括号内的是毫米修正单位（不知对不对）
    #print(e) 计算没问题
    return e

BioaTou=[['项目'],['一号杆'],['二号杆'],['三号杆'],['四号杆'],['五号杆'],['七号杆']]
#应变量未进行单位转化
#第一组数据0N
# Ndata=[[68.25],[-326.2],[-945.15],[33138.7],[16262.5],[-7322.85]]
#第二组数据100N
# Ndata=[[34.45],[14599.8],[151.4],[-1058.11],[-29061.5],[20.35]]
#第三组数据200N
# Ndata=[[386.3],[4194.65],[-5609.15],[2.5],[3890.9],[16462.65]]
#第四组数据300N
# Ndata=[[3868.5],[2450.55],[242.4],[8310.65],[-269.9],[53.75]]
#第五组数据400N
Ndata=[[-12849.0],[-126.25],[5710.8],[-5733.55],[-104.5],[-246.8]]


####
with open("F=400--data.csv", mode='w', newline='',encoding='utf-8') as file:  
    writer = csv.writer(file)  
    writer.writerows(BioaTou) 
print("done1!")

####
df1=pd.read_csv('F=400--data.csv')
df1["负载400N的时候的应变平均值/10^-6"]=Ndata
df1.to_csv('F=400--data.csv',index=False)
print("done1!")

output=[]
a=-2
####
with open("F=400--data.csv", mode='r', newline='',encoding='utf-8') as file:  
    reader=csv.reader(file)
    for rows in reader:
        a=a+1
        if(a==-1):
            continue
        else:
            strr=rows[1]
            print(a)
            print(strr)
            lis=re.findall(r'\d+\.\d+',strr)
            tar=float(lis[0])
            res1=XiDuShCh(a,tar)
            #res1 已经进行了单位的转化，此时Ff无需单位转化
            f=Ff(a,res1)
            output.append([f])
print(output)            


# 使用pd库写入新的列
####
df2=pd.read_csv('F=400--data.csv')
df2['轴向力/N']=output
df2.to_csv('F=400--data.csv',index=False)
print("done1!")