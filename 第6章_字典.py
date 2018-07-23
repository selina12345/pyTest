print("6.1 一个简单的字典")  # 字典中储存了外星人的颜色和点数，使用两条print语句来访问并打印这些信息
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

print("\n6.2 使用字典")
# 字典是一系列键-值对，每个键对应一个值，说键相关联的值可以是数字、字符串、列表、乃至字典，键和值之间用冒号隔开。

print("\n6.2.1 访问字典中的值")
# 要获取与键相关的值，可依次指定字典名和放在方括号内的键，如：
alien_0 = {"color": "green"}
print(alien_0["color"])

# 字典中可包含任意数量的键-值对，如：
alien_0 = {"color": "green", "points": 5}

# 你可以访问外星人alien_0的颜色和点数，如果玩家同时射杀了这个外星人，你可以用下面的代码来确定该玩家应获得多少个点，如：
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print("You just earned" + str(new_points) + " points!")

print("\n6.2.2 添加键—值对")  # 如在字典alien_0中添加两项信息：外星人的x轴坐标和Y轴坐标 ,如设置x=0 ，y=25：
ailen_0 = {"color": "green", "points": 5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

print("\n6.2.3 创建一个空字典")
alien_0 = {}
alien_0["color"] = "green"
alien_0["point"] = 5
print(alien_0)

print("\n6.2.4 修改字典中的值")  # 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值，如：
alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + " .")
alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + " .")
print(alien_0)

print("\n6.2.5 删除键值对")  # 对于字典中不要的信息可使用del语句将相应的值彻底删除
alien_0 = {"color": "green", "points": 5}
del alien_0["points"]
print(alien_0)

print("\n由类似对象组成的字典")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("Sarah's favorite language is " + favorite_languages["sarah"].title() + " .")

print("\np87 动手试一试")
print("6-1人")
name = {"last_name": "LI", "first_name": "zhi_xin", "age": 18, "city": "shengzhen"}
print(name["last_name"])
print(name["first_name"])
print(name["age"])
print(name["city"])

print("\n6-2 喜欢的数字")
favorite_digital = {"selina": 5, "candy": 6, "sue": 8, "hester": 1, "blue": 9}
for name, digital in favorite_digital.items():
    print("\nname: " + name)
    print("digital: " + str(digital))
    print(name.title() + " faviorite digital is " + str(digital) + " .")

print("\n6-3 词汇表")
Programming = {"Data_Structures": "基本数据结构",
               "array": "阵列",
               "background": "背景",
               "breakpoint": "断点",
               "class": "类别",
               }
for vocabulary, meaning in Programming.items():
    print("\nvocabulary: " + vocabulary)
    print("meaning: " + meaning)

print("\n6.3 遍历字典")
print("6.3.1 遍历所有的键-值对")  # 可使用for循环来遍历整个字典 如：
user_0 = {"username": "efermi",
          "first": "enrico",
          "last": "fermi",
          }
for key, value in user_0.items():  # key和value可根据字典信息自己定义 以方便理解。
    print("\nkey: " + key)
    print("value: " + value)

print("6.3.2 遍历字典中的所有键")  # 可使用keys()方法
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name)

# 可使用keys()确定某个人是否接受了调查
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n6.3.3 按顺序遍历字典中的所有键")  # 可使用sorted()获得按特定顺序排列的键
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in sorted(favorite_languages):
    print(name.title() + ", thank you for taking the poll.")

print("\n6.3.4 遍历字典中的所有值")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for languages in favorite_languages.values():  # 可使用values()方法,没有考虑重复项
    print(["value"])

# 当值有多个重复项时，可集合set(),但每个元素必须是独一无二的：
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for languages in set(favorite_languages.values()):
    print(languages.title())

print("p92 动手试一试")
print("6-4 词汇表")
Programming = {"Data_Structures": "基本数据结构",
               "array": "阵列",
               "background": "背景",
               "breakpoint": "断点",
               "class": "类别",
               }
for keys, values in Programming.items():
    print(keys.title() + ":" + values)

print("6-5 河流")
river = {"nile": "egypt",
         "donau_donav": "germany",
         "volga": "russia",
         }
for name, country in river.items():
    print("The " + name.title() + " runs through " + country.title() + ".")
    for name in river.keys():
        print(name)
        for country in river.values():
            print(country)

print("\n6-6 调查")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
member_list = ["selina", "lizhixin", "jen"]

flag = ""
for meb in member_list:
    for name in favorite_languages.keys():
        if name == meb:
            flag = name
            print(name.title() + ", Thank you for participating")

    if flag != meb:
        print(meb + " ，yes")

print("方法2")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
member_list = ["selina", "lizhixin", "jen"]
for name in favorite_languages.keys():
    print(name.title())

    if name in member_list:
        print(name.title() + ", Thank you for participating")
    if "selina" not in favorite_languages.keys():
        print("selina" + ", I want to invite you to participate in the survey.")
    if "lizhixin" not in favorite_languages.keys():
        print("lizhixin" + ", I want to invite you to participate in the survey.")

print("\n6.4 嵌套") #将字典存储在列表/将列表储存在字典
print("6.4.1 字典列表")
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#外星人不止三个，且每个外星人都是使用代码自动生成，我们可以用range()自动创建30个外星人
#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色的外星人：
for alien_number in range(30):
    new_alien =  {"color": "green", "points": 5,"speed": "slow"}
    aliens.append(new_alien)

#显示前5个外星人：
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人：
print("Total number of aliens: " + str(len(aliens)))

print("\n6.4.2 在字典中存储列表")
#存储所点披萨的信息
pizza = {"crust": "thick",
         "toppings": ["mushrooms","extra cheese"],
         }
#概述所点披萨的信息
print("You ordered a " + pizza["crust"] + "-crust pizza " + "with tha following toppings:")
for toppings in pizza["toppings"]:
    print("\t" + toppings)

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
    print("\n" + name)
    for key,value in information.items():
        print(key+': '+value)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for new_dict in dict.keys():
    print(new_dict)
for keys, values in dict.items():
    print(keys)

print("\nP99 动手试一试")
print("6.7 人")
name_0 = {"last_name": "li", "first_name": "zhi_xin", "age": 18, "city": "shengzhen"}
name_1 = {"last_name": "jiang", "first_name": "jing_jing", "age": 19, "city": "zhuhai"}
name_2 = {"last_name": "wu", "first_name": "yu_hua", "age": 20, "city": "huizhou"}
people = [name_0,name_1,name_2]
for peoples in people:
    print(peoples)

print("\n6.8 宠物")
cat = {"the_host": "lzx","type": "mammal"}
fish = {"the_host": "jjj","type": "fishes"}
chicken = {"the_host": "wyh","type": "bird"}
pets = [cat,fish,chicken]
for pet in pets:
    print(pet)

print("\n6-9 喜欢的地方")
favorite_places = {"jjj": ["china","india"],
    "lzx": ["japan","gereny","china"],
    "mtx": ["mexico","south_africa","korea"]
}
friend = ["osf","ylq","bl"]
for name, country in favorite_places.items():
    print(friend[0].title() + " said " + name + " is favorite place is " )
    for countryes in country:
        print("\t" + countryes)

print("\n6-10 喜欢的数字")
favorite_digital = {"selina": [5,9,0],
                    "candy": [6,3,],
                    "sue": [8,9,1,5],
                    "hester": [1,2,3,4,5],
                    "blue": [2.9],
}
for name, digital in favorite_digital.items():
    print("\nname: " + name)
    print("digital: " + str(digital))
    print(name.title() + " faviorite digital is " + str(digital) + " .")

print("6-11 城市")
cities ={
    "广州": {
        "country":"china",
        "population": "10000",
       "fact": "it is beautiful.",
         },
    "东京": {
        "country": "japan",
        "population": "500",
        "fact": "It is very developed here.",
        },
    "纽约": {
        "country": "united_states",
        "population": "20000",
        "fact": "The food is very rich here.",
        },
    }
for country, information in cities.items():
    print("\n" + country.title())
    for key, value in  information.items():
        print(key.title() + ": " + value.title())
