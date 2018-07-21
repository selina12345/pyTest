print("6.2使用字典")
print("6.2.1.输出字典中的键和值")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for dict, information in dict.items():
    print("\ndict: ", dict)
    print("information: ", information)

print("\n6.2.2.输出字典中的值")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict["Name"])
print(dict["Age"])
print(dict["Class"])

#注意：
#每个键与值用冒号隔开（:），每对用逗号，每对用逗号分割，整体放在花括号中（{}）
#键必须独一无二，但值则不必。
#值可以取任何数据类型，但必须是不可变的，如字符串，数或元组。

print("\n6.2.3 修改字典中的值信息")
#可以向字典增加新的键/值对，修改或删除已有键/值对  如:
dict = {"Name": "Zara", "Age": 7, "Class": "First"}
dict["Name"] = "Selina"
print(dict)

dict = {"Name": "Zara", "Age": 7, "Class": "First"}
dict["first_name"] = dict.pop("Name")  #修改字典键的信息
print(dict)   #执行语句：dict.pop('Name')，删除 'Name'所对应的键值对,返回 'Name'对应的值；
              #dict["first_name"]相当于给字典新添加一个key，其value为dict["first_name"]返回的值。

print("\n6.2.4.删除字典中的键信息")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict["Name"]
print(dict)

print("\n6.2.5 .新加字典信息")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict["city"] = " shengzhen"
print(dict)

print("\n6.2.6.计算字典的长度")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
Length  = len(dict)
print(Length)

print("\n6.2.7.清空字典所有信息")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict.clear()
print(dict)


print("\n6.2.8.创建字典")
dict = {}
dict["name"] = "lizhixin"
dict["age"] = 18
dict["city"] = "shengzhen"
print(dict)

print("\n6.3遍历字典")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for keys, values in dict.items():
    print(keys + ":" + str(values))

print("6.3.1 遍历所有的键—值对")
print("\n6.3.2 遍历字典所有键）#可用 keys表示")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for keys, values in dict.items():
    print(keys)

print("\n6.3.3 按顺序遍历字典中的所有键")
dict = {'Flice': '2', 'Deth': '9', 'Cecil': '1', "Bella": "10"}
for key in sorted(dict.keys()):  #sorted() 按照顺序排列
    key = list(dict.keys())
print(key)

print("\n6.3.4 遍历字典所有值") #可用values表示
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
keys = list(dict.keys())
values = list(dict.values())  #访回以列表形式的键和值
print(keys)
print(values)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for keys, values in dict.items():
    print(values)

print("\n6.4嵌套")
print("\n6.4.1 字典列表")
alien_0 = {"color": "red"}
alien_1 = {"color": "green"}
alien_2 = {"color": "blue"}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

print("\n#示例2：创建一个用于存储外星人的空列表")
aliens = []
#创建30个绿色的外星人
for alien_number in range(30):
   new_alien = {"color":"green", 'points':5, 'speed':'slow'}
   aliens.append(new_alien)
#显示前5个外星人
for alien in aliens[:5]:
   print(alien)
print("...")
#显示一共创建了多少个外星人
print("外星人的数量是： %d" % len(aliens))

print("\m示例3:创建一个用于存储外星人的空列表")
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {"color": "green", 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

print("\n6.4.2 在字典中存储列表")
#假设有个小店，里边卖了2种粥，但是每种粥的配料都不一样，利用一个字典记录两种粥及其配料
gruel={
    "八宝粥":["大米","桂圆","红枣","芡实","莲子","薏仁","黑豆","核桃仁"],
    "瘦肉粥":["大米","瘦肉"]
    }
for keys, values in gruel.items():
    print("\n" + keys,end=":")   #print默认是打印一行，结尾加换行。end=" "意思是末尾不换行，加空格。
    for value in values:
        print(value,end=" ")

print("\n6.4.3 在字典中存储字典")
grade={
    '赵丽颖':{
        '国籍':'中国',
        '民族':'汉',
        '出生日期':'1987年10月16日',
        '身高':'165cm',
        },
    '杨幂':{
        '国籍':'中国',
        '民族':'汉',
        '出生日期':'1986年9月12日',
        '身高':'166.5cm',
        }
    }
for name,information in grade.items():
    print(name)
    for key,value in information.items():
        print(key+':'+value)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for new_dict in dict.keys():
    print(new_dict)
for keys, values in dict.items():
    print(keys)






