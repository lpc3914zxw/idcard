#-*- coding: utf-8 -*-
import datetime#导入时间
from collections import Counter
import xlrd
import numpy as np
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Page, Pie
from pyecharts import options as opts
area={
    '11':'北京市','12':'天津市','13':'河北省','14':'山西省','15':'内蒙古自治区',
    '21':'辽宁省','22':'吉林省','23':'黑龙江省',
    '31':'上海市','32':'江苏省','33':'浙江省','34':'安徽省','35':'福建省','36':'江西省','37':'山东省',
    '41':'河南省','42':'湖北省','43':'湖南省',
    '44':'广东省','45':'广西壮族自治区','46':'海南省',
    '50':'重庆市','51':'四川省','52':'贵州省','53':'云南省','54':'西藏自治区',
    '61':'陕西省','62':'甘肃省','63':'青海省','64':'宁夏回族自治区','65':'新疆维吾尔族自治区',
    '81':'香港特别行政区','82':'澳门特别行政区','83':'台湾地区'
}
#全国省的字典,全局变量
key_flag=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
#17位相乘系数数组
flag_lastnumber=[1,0,'X',9,8,7,6,5,4,3,2]
#%11对应的余数得到的校验码，下标为余数
class Id_demo():
        # def __init__(self,number):#一个参数，构造函数
        # number=str(number)#参数为身份证号码数组
        # n_flag=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]#17位相乘数组

    def id_loc(number):#地区切片
        loc=number[0:2]#前2位
        str={11,12,13,14,15,
             21,22,23,
             31,32,33,34,35,36,37,
             41,42,43,44,45,46,
             50,51,52,53,54,61,62,63,64,65,81,82,83}
        if int(loc) in str:
            return area[loc]

        else:
            return '未知'
            print('未知')  # 打印地区
    def id_sex(number):#性别
        sex=number[-2]#倒数第二位
        sex=int(sex)
        if sex/2:
           # print('男')
            return '男'
        else:
           # print('女')
            return '女'
    def id_age(number):
        birthday=number[6:14]#出生年月日
        birth_year=birthday[0:4]#前四位
        age=datetime.datetime.now().year-int(birth_year)#int换算
        #print(str(age)+'岁')
        return age

    def get_zodiac(number):
        """通过身份证号获取生肖"""
        start_year = 1901
        zodiac_interval = (int(number[6:10]) - start_year) % 12
        if zodiac_interval == 1 or zodiac_interval == -11:
            return '鼠'
        if zodiac_interval == 0:
            return '牛'
        if zodiac_interval == 11 or zodiac_interval == -1:
            return '虎'
        if zodiac_interval == 10 or zodiac_interval == -2:
            return '兔'
        if zodiac_interval == 9 or zodiac_interval == -3:
            return '龙'
        if zodiac_interval == 8 or zodiac_interval == -4:
            return '蛇'
        if zodiac_interval == 7 or zodiac_interval == -5:
            return '马'
        if zodiac_interval == 6 or zodiac_interval == -6:
            return '羊'
        if zodiac_interval == 5 or zodiac_interval == -7:
            return '猴'
        if zodiac_interval == 4 or zodiac_interval == -8:
            return '鸡'
        if zodiac_interval == 3 or zodiac_interval == -9:
            return '狗'
        if zodiac_interval == 2 or zodiac_interval == -10:
            return '猪'
        else:
            return np.nan

    def get_starsign(number):
        birth_month=int(number[10:12])
        birth_day = int(number[12:14])
        """通过身份证号获取星座"""
        if (( birth_month == 1 and  birth_day > 19) or ( birth_month == 2 and  birth_day <= 18)):
            return "水瓶座"
        if (( birth_month == 2 and  birth_day > 18) or ( birth_month == 3 and  birth_day <= 20)):
            return "双鱼座"
        if (( birth_month == 3 and  birth_day > 20) or ( birth_month == 4 and  birth_day <= 19)):
            return "白羊座"
        if (( birth_month == 4 and  birth_day > 19) or ( birth_month == 5 and  birth_day <= 20)):
            return "金牛座"
        if (( birth_month == 5 and  birth_day > 20) or ( birth_month == 6 and  birth_day <= 21)):
            return "双子座"
        if (( birth_month == 6 and  birth_day > 21) or ( birth_month == 7 and  birth_day <= 22)):
            return "巨蟹座"
        if (( birth_month == 7 and  birth_day > 22) or ( birth_month == 8 and  birth_day <= 22)):
            return "狮子座"
        if (( birth_month == 8 and  birth_day > 22) or ( birth_month == 9 and  birth_day <= 22)):
            return "处女座"
        if (( birth_month == 9 and  birth_day > 22) or ( birth_month == 10 and  birth_day <= 23)):
            return "天秤座"
        if (( birth_month == 10 and  birth_day > 23) or ( birth_month == 11 and  birth_day <= 22)):
            return "天蝎座"
        if (( birth_month == 11 and  birth_day > 22) or ( birth_month == 12 and  birth_day <= 21)):
            return "射手座"
        if (( birth_month == 12 and  birth_day > 21) or ( birth_month == 1 and  birth_day <= 19)):
            return "魔羯座"
        else:
            return np.nan
    def id_flag(number):#辨别真假
        last=number[-1]#最后一位
        arry_number=list(map(int,number))#map转化数组
        arry_number.pop()#删除最后一个校验位
        tuple_flag=list(zip(key_flag,arry_number))#合成元组
        sum=0#记录相乘之后的和
        for p in tuple_flag:
            #得出一组数
            each=1#系数为1与他们相乘
            for q in p:
                each=q*each
            sum+=each#记录每组数的乘积和
        result=sum%11#对11取余数
        calculate=flag_lastnumber[result]
        if calculate==int(last):
            print('身份证正确')
        else:
            print('身份证错误')
            return 0
        return 1


def extract(inpath):
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号
    result = []
    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result.append(alldata[4])   # 取出表中第二列数据
    return (result)


inpath = 'xxx.xls'  # excel文件所在路径

data=extract(inpath)
data_data=[]
for i in range(len(data)):
    if(len(data[i]) == 18):
        data_data.append(data[i])
    else:
        0
data_loc = []
data_sex = []
data_age = []
data_zo = []
data_starsign= []
for i in range(len(data_data)):
    data_loc.append(Id_demo.id_loc(data_data[i]))
for i in range(len(data_data)):
    data_sex.append(Id_demo.id_sex(data_data[i]))
for i in range(len(data_data)):
    data_age.append(Id_demo.id_age(data_data[i]))
for i in range(len(data_data)):
    data_zo.append(Id_demo.get_zodiac(data_data[i]))
for i in range(len(data_data)):
    data_starsign.append(Id_demo.get_starsign(data_data[i]))

res = Counter(data_loc)#地址
res=dict(res)

res1 = Counter(data_starsign)#星座
res1=dict(res1)
res2 = Counter(data_sex)#星座
res2=dict(res2)
print(res)
print(res1)
print(res2)
dic ={
     '省':data_loc, '性别':data_sex,
     '年龄':data_age,
     '属相':data_zo,
     '星座':data_starsign,

 }

table=pd.DataFrame(dic)

res.values()
writer = pd.ExcelWriter("lemon.xls")
table.to_excel(writer,'sheet_1')
writer.save()
writer.close()
res2_k=list(res2.keys())
res2_v=list(res2.values())
print(res2_k)
print(res2_v)
print(res1.keys())
print(res1.values())
print(res.keys())
print(res.values())
#number=input()
#demo=Id_demo(number)
#demo.id_loc(number)
#demo.id_sex(number)
#demo.id_age(number)
#demo.id_flag(number)