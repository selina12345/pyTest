#4.1遍历整个列表，对每个列表中的每个元素都执行相同的操作，可用for循环
name = ["china","chile","india"]
for name_new in name:
    print(name_new)  
#print语句是if语句的从属代码块，代表从属关系，print语句之前有4个空格。按Tab键就行，如果if语句没有任何从属的代码块就会报错expected an indented block。
#与if语句类似的，必须包含从属代码块的还有while、for、try-except等。

#4.1.2 在for循环中执行更多的操作
country = ["china","chile","india"]
for countrys in country:
    print("I am going to " + countrys.title()+ ".")
    print("I am going to " + countrys.title()+ "." + "\n" + "How about you？" + "\n")  #可使用空行使得输出内容更加清楚
print("that is great")  #print语句不缩进只会执行一次

#4.2避免缩进错误
#4.2.1忘记缩进
name = ["selina","sue","hester"]
for names in name:
    print(names)  #print没有缩进输出会在print语句t下方 提示有问题

#4.2.2忘记缩进额外的代码行
name = ["seli","su","hter"]
for names in name:
    print(names.title()+ ",I miss you.")
print("looking forward to meeting! "+ names.title() + ".\n")  #没有缩进则只执行列表最后一个元素

#4.2.3不必要的缩进
name = ["selina","sue","hester"]
print(name)  #在没使用for等其他循环语句时如果缩进在输出时会在print语句p下方提示有问题

#4.2.4循环后不必要的缩进
teacher = ["nana","yaya","haha"]
for teachers in teacher:
    print("I love teacher," + teachers.title()+ ".\n")
print("thank you everyone teacher."+ "\n")  #不小心缩进了应循环结束后执行的代码 ，这些代码会针对每个列表重复执行，但不会提示错误，因在输出时应确定是否应该缩进执行操作的代码

#p50动手试一试
pizza = ["orange","apple","peach"]
for pizzas in pizza:
    print(pizzas)
    print("I like " + pizzas+ " pizza" +"\n")
print("I really love pizza!"+"\n")

Animal = ["cat","dog","pig"]
for Animals in Animal:
    print(Animals)
print("the " + Animal[0] + " very lovely.") 
print("the " + Animal[1] + " very smart.") 
print("the " + Animal[-1] + " very instering.") 
print("the animals are beautiful.")#C7EDCC

#4.3创建数值列表
#4.3.1使用函数range() 从指定的第一个值开始数，并在你指定的倒数第二个值结束。如下语句输出到4
for value in range(1,5):
    print(value)

#4.3.2使用range(}创建数字列表 ，可使用函数list()将ranget()的结果直接转换成列表
numers = list(range(1,5))
print(numers)

even_numers = list(range(2,11,2)) #可指定步长，如从2开始，直到达到或超过(11)为止，因而输出值为[2,4,6,8,10]
print(even_numers)

#如何创建一个列表，其中包含前10个整数（即1-10）的平方，python中两个**表示乘方运算
squares = []
for value in range(1,11):
    square = value**2  #自定义一个表达式为value**2 表示计算平方值
    squares.append(square)
print(squares)

#4.3.3对数字列表执行简单的计算，可用min() max() sum()函数对列表执行简单的计算
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))

digits = [1,2,3,4,5,6,7,8,9,10]
message = min(digits)
print(message)

#4.3.4列表解析 列表解析可将for循环和创建新元素代码合并成一行 并自动附加新元素。
squars = [value**2 for value in range(1,11)]
print(squars)

#54动手试一试
counts = list(range(1,21))
print(counts)

counts = list(range(1,1000001))
print(min(counts))
print(max(counts))
print(sum(counts))

odd = list(range(1,21,2))
print(odd)

multiple= list(range(3,30,3))
print(multiple)

cubes = []
for value in range(1,10):
    cube = value**3
    cubes.append(cube)
print(cubes[0])
print(cubes[1])

cubes = [value**3 for value in range(1,10)]
print(cubes)

#4.4使用列表的一部分
#4.4.1 切片(python使用列表中的部分元素称为切片）
colours = ["red","blue","green","white","black"]
print(colours[0:3]) #可使用索引只输出列表中前三个元素的值
print(colours[1:5]) #可指定索引输出第2-5个值
print(colours[:3]) #如没指定第一个索引则默认从第一个元素开始输出
print(colours[2:]) #如指定从列表第三个元素开始到末尾结束
print(colours[-3:])#如要输出最后三个颜色

#4.4.2遍历切片 如要遍历列表中的部分元素，可在for循环中使用切片
players = ["nana","luca","tinda","ninz","sevn"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#4.4.3复制列表
my_fruits = ["apple","Banana","orange","peach"]
my_friend_fruits = my_fruits
print("My favorite food s are:")
print(my_fruits)
print("\nMy friends favorite food s are:")
print(my_friend_fruits)

my_fruits = ["apple","Banana","orange","peach"]
my_fruits.append("mango")  #将每个列表中都加入新的元素并输出
my_friend_fruits.append("plum")
print("\nMy favorite food s are:")
print(my_fruits)

print("\nMy friends favorite food s are:")
print(my_friend_fruits)

#p58动手试一试
musicians = ["amna","mama","dada","lili","huhu"]
print("\nThe first three items in the list are:")
for musician in musicians[0:3]:
    print(musician)
    
print("\nThe first three items in the list are:")   
for musician in musicians[1:4]:
    print(musician)
    
print("\nThe first three items in the list are:")       
for musician in musicians[-3:]:
    print(musician)
    
my_pizza = ["orange","apple","peach"]
my_pizza.append("pear")
friends_pizza = my_pizza
print("\nMy favorite pizza are:")
print(my_pizza)
print("\nMy friends favorite pizza are:")
print(friends_pizza)

print("\nMy favorite pizza are:")
for my_pizzas in my_pizza[:]:
    print(my_pizzas)

print("\nMy friends favorite pizza are:")
for friends_pizzas  in friends_pizza[:]:
    print(friends_pizzas)

#4.5元组 python将不能修改的值称不可变，而不可变的列表称为元组
#4.5.1定义元组 使用圆括号而不是方括号标识。这样就可以使用索引眯访问其元素
list = (0,10,20,30,40,50)
print(list[0])  #不能修改元组的值 如写成这样针出错, #list[0]=60
print(list[1])

#4.5.2 遍历元组中的所有值，像列表一样，可以使用for循环来输出元组中的值
list = (0,10,20,30,40,50)
for lists in list:
    print(lists)
    
#4.5.3修改元组变量 不能修改元组中的元素，但可以给存储元组中的变量赋值
list = (200,50)
print("\nOld list:")
for Old_list in list:
    print(Old_list)
    
list = (400,100)
print("\nNew list:")
for New_list in list:
    print(New_list)

#P60 动手试一试
food = ("Biscuits","Snacks","Crisps","Poultry","Cereals")
for foods in food:
    print(foods)

food = ("apple","Snacks","Crisps","Poultry","lizi")
print("\nNew_food:")
for new_food in food:
    print(new_food)
    
#4.6设置代码格式 详细见附录B

