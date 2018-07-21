print("#5.1一个简单示例")
cars = ["audi", "bnw", "subaru", "toyota"]
for car in cars:
    if car == "bnw":
        print(car.upper())
    else:
        print(car.title())

print("\n#5.2条件测试 一个值为true或false值的表达式称为条件测试")
# 5.2.1检查是否相等 最简单的的条件测试检查变量的值是否与特定值相等
car = "bmw"  # 可解读为将变量car设置为为bmw
car == "bmw"  # 使用两个==检查car的值是否为"bnw" 相等返回true 否则返回flase

car = "audi"
car = "bmw"  # 返回flase

# 5.2.2 检查是否相等时不考虑大小写 大小写不同的值会被视为不相等，返回flase
car = "Ausi"
car == "adui"

car = "Audi"
car.lower() == "audi"  # 如果大小写很重要可将变量的值转换成小写在进行比较

# 5.2.3 检查是否不相等 可用惊叹号和等号(!=),!表示不
vehicle = "heavy_vehicle"
if vehicle != "light_vehicle":
    print("it is light_vehicle!")

# 5.2.4比较数字
age = 18
print(age == 19)

answer = 17
if answer != 18:
    print(answer)

age = 10
print(age > 9)

# 5.2.5检查多个条件 (可使用and 将两个条件测试合为一个，如果每个测试都通过了，返回true),如果至少有一个没有通过，返回false) 如：
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # 检查两个变量是否都大于21，返回flase

age_0 = 22
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # 返回true

# 使用or检查多个条件，至少有一个条件满足就返回true,当所有的都不满足时才返回flase
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

print("5.2.6检查特定值是否包含在列表中 （可用关键字in")
Fruits = ["apple", "banana", "orange", "peach"]
fruit =  "apple" in Fruits
print(fruit)

Fruits = ["apple", "banana", "orange", "peach"]
print("lizi" in Fruits)

print("\n5.2.7 检查特定值是否不包含在列表中 可用关键字not in")
theList = ["a", "b", "c"]
if "d" not in theList:
    print("d" + " is not in the list.")

theList = ["a", "b", "c"]
List = "d"
if "d" not in theList:
    print(List.title() + " is not in the list.")

print("\nP70 动手试一试")
country = "china"
coutries = "china"
print(coutries + " I predict True.")

print("====================")

print("country = [""china", "chile", "india""]")
print("for countries in country:")
print("if countries == ""chile"":")
print("country.title()")
print("else:")
print("countries")

country = ["china", "chile", "india"]
for countries in country:
    if countries == "chile":
        print(countries.title())
    else:
        print(countries)

print("====================")

light = 5
light = 5
print(light == 5)

light = 5
light = 6
print(light != 5)

print("====================")

you = "Y"
you = you.lower()
print(you == "y")

number_1 = 1
number_2 = 1
print(number_1 == number_2)

number_1 = 1
number_2 = 2
print(number_1 == number_2)

print("====================")

print("number_1 = 1")
print("number_2 = 2")
print("number_1 > number_2")
number_1 = 1
number_2 = 2
print(number_1 > number_2)
print("====================")

number_1 = 1
number_2 = 2
print(number_1 < number_2)

number_1 = 2
number_2 = 10
print(number_1 >= 10 and number_2 >= 10)

number_1 = 2
number_2 = 10
print(number_1 >= 10 or number_2 >= 10)

print("====================")

print("country = [""china"",""chile"",""india""]")
print("india in country")
country = ["china", "chile", "india"]
print("india" in country)

country = ["china", "chile", "india"]
country_1 = "france"
if "france" not in country:
    print(country_1.title() + " it is flase.")

print("\n5.3 if语句")
print("5.3.1 简单的if语句")
age = 18
if age >= 18:  # 如果age的值小于18，这不会输出内容
    print("You are old enough to vote!")  # 如果条件测试的结果为true，python会继续执行if语句后面的代码，否则将忽略这些代码。

print("\n5.3.2 if-else语句 检查一个条件情况")  # 如果满足条件执行些代码，否则输出下面的代码。执行两种中的一种。
print("age = 17")
print("if age >= 18:")
print("You are old enough to vote!")
print("Have you registered to vote yet!")
print("else:")
print("Sorry,you are too young to vote.")
print("Please register to vote as soon as you turn 18!")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet!")  # 如果满足条件执行些代码，否则输出下面的代码。执行两种中的一种。
else:
    print("\nSorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("====================")
print("\n5.3.3 if-elif-else 检查超过两个条件情况")  # 依次检查每个条件的测试，直到遇到通过了条件的测试才会运行后面的代码
age = 12
if age < 4:
    print("You admission cost is $4.")
elif age < 18:
    print("You admission cost is $5.")
else:
    print("You admission cost is $4.")

# 为了使代码更简洁，可这样操作：
age = 1
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("your admission cost is $" + str(price) + ".")

print("====================")
print("\n 5.3.4 使用多个elif 代码块")  # 如前面的案例中在加一个条件，对于65岁以上的老人半价
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("your admission cost is $" + str(price) + ".")
print("====================")

print("\n5.3.5 省略else 代码块")  # python并不要求if-elif结构后面必须要有else代码块，在特定情况下使用一条elif语句来处理特定的情形更清晰。
age = 66
if age < 4:
    price = 0
elif age <= 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:  # 在超过65，价格才为5美元，这样只有每个代码块通过相应测试才会执行。
    print("your admission cost is $" + str(price) + ".")  #str()将数转化成字符格式
print("====================")

print("\n5.3.6 测试多个代码条件")  # 要检查所有条件应使用不包含elif 和 else代码块的if 语句，在可能有多个条件为true，且你需要在每个条件都为true时都采取相应措施时适合这种
# 如客户点了两种配料，就要确保在其比萨中包含这些配料：
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni")
if "extra cheese in requested_toppings":
    print("Adding extra cheese.")
print("\nFished making your pizza!")

# 总之：如只想执行一个代码块，就使用if-elif-else结构，如要运行多个代码块，就使用一系列独立的语句。
print("====================")

print("P75 动手试一试")
print("#5-3 外星人的颜色")
alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("You can get 5 points")

alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "blue":
        print("You can get 5 points")

print("\n5.4 外星人颜色2")
alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("You can get 5 points")

alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("You can get 5 points")
else:
    print("You can get 10 points")

print("\n5-5外星人颜色#3")
alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("You can get 5 points")
    elif color == "yellow":
        print("You can get 10 points")
    elif color == "red":
        print("You can get 15 points")

alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("\nYou can get 5 points")
    elif color == "yellow":
        print("You can get 10 points")
else:
    print("You can get 15 points")

print("\n5-6生的不同阶段")
age = 10
if age < 2:
    print("He is baby")
elif 2 <= age < 4:
    print("He is learning to walk.")
elif 4 <= age < 13:
    print("He is a child.")
elif 13 <= age < 20:
    print("He is a teenager.")
elif 20 <= age < 65:
    print("He is an adult.")
else:
    print("He is the elderly.")

print("\n5-7喜欢的水果")
favorite_fruits = ["banana", "orange", "peach"]
if "banana" in favorite_fruits:
    print("I really like banana.")
if "orange" in favorite_fruits:
    print("I really like orange.")
if "peach" in favorite_fruits:
    print("I really like peach.")

print("\n5.4 使用if语句处理列表")
print("5.4.1 检查特殊元素")
requested_toppings = ["mushrooms", "green pepers", "extra cheese"]
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFished making your pizza!")

print("\n如果披萨店的青椒用完了，可这样处理：")
requested_toppings = ["mushrooms", "green pepers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green pepers":
        print("Sorry，we are out of green pepers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("Fished making your pizza!")

print("\n5.4.2 确定列表不是空的")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Fished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\n5.4.3 使用多个列表")
available_toppings = ["mushrooms", "olives", "green pepers", "peperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "frehch fies", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + "")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
        print("Fished making your pizza!")

print("\np79 动手试一试")
print("5-8 以特殊方式跟管理员打招呼：")
list = ["selina", "sue", "admin", "candy", "fafa"]
for lists in list:
    if lists == "admin":
        print("Hello admin,world you like to see a staus report?")
    else:
        print("Hello," + lists + ",thank you for logging in again.")

print("5-9 处理没有用户的行为")
list = ["selina", "sue", "admin", "candy", "fafa"]
if list:
    for lists in list:
        if lists == "admin":
            print("Hello admin,world you like to see a staus report?")
        else:
            print("Hello," + lists + ",thank you for logging in again.")
else:
    print("We need to find some users!")
del list[0]
del list[1]
del list[2]
del list[-1]
print("It is clear.")

print("\n5-10 检查用户名")
current_users = ["sam", "nana", "admin", "candy", "fafa"]
new_users = ["selina", "sue", "admin", "chris", "fafa"]
for new_users in new_users:
    if new_users in current_users:
        print(new_users + " this username has already been used.")
        print("You need to enter a different username.")
    else:
        print(new_users + " this username has't already been used.")

print("\n5.11 序数")
# numbers = list(range(1,10))
# print(numbers)
for number in range(1,10):
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+ "th")

print("\n5.5设置if语句格式")

