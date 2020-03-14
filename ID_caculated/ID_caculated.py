#!/usr/bin/python3
import time,os,sys;
#将输入的年分分配365或366个list
def dateRange(year):
    fmt ='%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(year+'-01-01',fmt)))
    end = int(time.mktime(time.strptime(year+'-12-31',fmt)))
    list_date = [time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]
    return [i.replace('-','') for i in list_date]
ID_10 = input("请输入身份证号前十位：")
while(len(ID_10)!=10):
    print("非法输入,请重新输入!")
    ID_10 = input("请输入身份证号前十位：")
year = ID_10[6:]
ID_L4 = input("请输入身份证号后四位：")
while(len(ID_L4)!=4):
    print("非法输入,请重新输入!")
    ID_L4 = input("请输入身份证号后四位：")
area={"11":"北京","12":"天津","13":"河北","14":"山西","15":"内蒙古","21":"辽宁","22":"吉林","23":"黑龙江","31":"上海","32":"江苏","33":"浙江","34":"安徽","35":"福建","36":"江西","37":"山东","41":"河南","42":"湖北","43":"湖南","44":"广东","45":"广西","46":"海南","50":"重庆","51":"四川","52":"贵州","53":"云南","54":"西藏","61":"陕西","62":"甘肃","63":"青海","64":"宁夏","65":"新疆","71":"台湾","81":"香港","82":"澳门","91":"国外"}
if(int(ID_L4[2]) % 2):
   print("欢迎！"+ area[ID_10[0:2]] + "的帅气小伙子(●ˇ∀ˇ●)")
else:
   print("欢迎！"+ area[ID_10[0:2]] + "的漂亮大姑娘(●ˇ∀ˇ●)")
ID_list =[ID_10[:6]+i+ID_L4 for i in dateRange(year)]
#实体码权重
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
#对应的校验码
validate=['1','0','X','9','8','7','6','5','4','3','2']
ID_last=[]
for i in ID_list:
    sum=0
    for j in range(0,17):
        sum += int(i[j])*weight[j]
    if(i[17]== validate[sum % 11]):
        ID_last.append(i)
print("以下一共有"+str(len(ID_last))+"种身份证号的可能：")
for list in ID_last:
    print(list)