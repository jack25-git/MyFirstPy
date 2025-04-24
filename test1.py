import math
temp_dict={"111":36,"112":37,"113":38,"114":35,"115":39}
print(temp_dict.items())

for emp_id,temp_d in temp_dict.items():
    print(f"员工{emp_id}你的提问是{temp_d:.2f}")
    if temp_d>37.5:
        print("工号："+emp_id+" 完蛋了,你的体温是"+str(temp_d))
sum=0
for i in range(101):
    sum=sum+i
print(sum)

# summ=0
# while True:
#     num=input("请输入数字：")
#     if str.upper(num)=="Q":
#         break1

    # sum=sum+int(num)


var=math.sin(30)

print(type(var))
print(var)
print("hello"+"    world!\n!")
type(var)
print(""" 你好呀
老朋友
""")

shopping_list=["电脑","键盘"]
print(shopping_list)
shopping_list.append("显示器")
print(shopping_list)
shopping_list.remove("键盘")
print(shopping_list)

contacts={"张三":12345,
          "李四":67890
          }
print(contacts)
contacts["王五"]=2458
print(contacts)
del contacts["张三"]
print(contacts)

https://shop.mango.com/cn/zh/p/%E5%A5%B3%E5%BC%8F/%E8%BF%9E%E8%A1%A3%E8%A3%99%E5%92%8C%E8%BF%9E%E8%BA%AB%E8%A3%A4/%E8%BF%9E%E8%A1%A3%E8%A3%99%E5%92%8C%E8%BF%9E%E8%BA%AB%E8%A3%A4/%E7%9F%AD%E6%AC%BE%E8%8A%B1%E6%9C%B5%E5%8D%B0%E8%8A%B1%E8%BF%9E%E8%A1%A3%E8%A3%99_77054018