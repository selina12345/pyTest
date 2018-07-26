print("8.1定义函数") #用def 定义函数或方法
# 如:下面是一个打印问候语的简单函数，名为greet_user():
def greet_user():
    print("Hello!")
greet_user()

print("\n8.1.1 向函数体传递信息")
#只要稍作修改，就可以让函数greet_user()不仅向用户显示Hello！，还将用户的名字用作抬头。为此，可在函数定义def greet_user()
#的括号内添加username。通过在这里添加username，就可让函数接受我们给username制定的任何值。现在，这个函数要求我们调用
#它给username指定一个值。调用greet_user()时，可将一个名字传递给它，如下所示：
def greet_user(username):
    print("Hello, " + username)
greet_user("Selina.") #调用函数greet_user("Selina."),并向它提供执行print语句所需的信息。这个函数接受我们传递给它的名字，
                      #并向这个人发出问候：Hello, Selina.,我们可以根据需要调用函数greet_user()任意次.

print("\n8.1.2 实参和形参")
#前面定义函数greet_user()时，要求给变量username指定一个值。调用这个函数并提供这种信息(人名)时，它将打印相应的问候语。
#实参是调用函数时传递给函数的信息。我们调用函数时，将要让函数使用的信息放在括号内。在greet_user('jesse')中，
#将实参'jesse'传递给了函数,greet_user(),这个值被存储在形参username中。

print("\n8.2 传递实参")
#鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多，可能用位置实参，这要求实参的顺序与形参的顺序
#相同；也可使用关键字实参，其实每个实参都有变量名和值组成；还可使用列表和字典。

print("\n8.2.1 位置实参")
#我们调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种方式被称为位置实参。
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')
#这个函数的定义表明，它需要一种动物类型和一个名字。调用describe_pet()时，需要按顺序提供一种动物类型和一个名字。例如，
# 在前面的函数调用中，实参'hamster'存储在形参animal_type中，而实参'harry'存储在形参pet_name中。在函数体内，
# 使用了这两个形参来显示宠物的信息。输出描述了一只名为Harry的仓鼠：
# I have a hamster.
# My hamster's name is Harry.

#1、调用函数多次。如要再描述一个宠物，只需再次调用describe_pet()即可：
def describe_pet(animal_type,pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')
describe_pet("dog","willie")
#每当需要描述新宠物时，都可调用这个函数,只需使用一行调用函数的代码，就可描述一个新宠物。
#在函数中，可根据需要使用任意数量的位置实参，Python将按 顺序 将函数调用中的实参关联到函数定义中相应的形参。

#2、位置实参的顺序很重要。使用位置实参来调动函数时，如果实参的顺序不正确，结果可能出乎意料：
def describe_pet(animal_type,pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('harry','hamster') #由于实参'harry'在前，这个值将存储到animal_type中，因而结果跟上面的相反

print("\n8.2.2 ")
#关键字实参是传递给函数的名称-值对。我们直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆(不会得到名为
#Hamster的Harry这样的结果).关键字实参让我们无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中的各个值的用途。如：
def describe_pets(animal_type,pet_name):  #使用关键字实参来调用describe_pet():
    print("\nI have a " + animal_type.title() + ".")
    print("My pet " + animal_type.title() + "'s name is " + pet_name.title() +".")
describe_pets(pet_name = 'harry',animal_type = 'hamster')  #无需考虑实参顺序，使用关键字对应

print("\n8.2.3 默认值")
#编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用制定的实参值；否则，将使用形参的默认值。
# 因此,给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
#例如，如果我们发现调用describe_pet()时，描述的大都是小狗，就可将形参animal_type的默认值设置为'dog'。这样，
# 调用describe_pet()来描述小狗时，就可不提供这种信息：只提供名字pet_name实参
def describe_pet(pet_name,animal_type = 'dog'):
    print('\nI have a ' + animal_type.title() + '.')
    print("My " + animal_type + "'s name is " + pet_name + ".")
describe_pet("Harry")  #省略animal_type默认的实参dog

print("\n如果要描述的动物不是小狗，可使用类似于下面的函数说明：")
def describe_pet(pet_name,animal_type = 'dog'):
    print('\nI have a ' + animal_type.title() + '.')
    print("My " + animal_type + "'s name is " + pet_name + ".")
describe_pet(animal_type="haster",pet_name="Harry")
describe_pet(pet_name="Harry",animal_type="Haster")
#注意 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。

print("\n8.2.4 等效的函数调用")
# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。请看下面的函数describe_pet()的定义，其中给一个形参提供了默认
#值：def describe_pet(pet_name,anmila_type = 'dog')
#基于这种定义，在任何情况下都必须给pet_name提供实参；指定该实参时可以使用位置方式也可以使用关键字方式。如果要描述的动物不是小狗，
#还必须在函数调用中给animal_type提供实参；同样，制定该实参可以使用位置方式，也可以使用关键字方式。

print("\n8.2.5 避免实参错误")

print("\n动手试一试")
print("8-3 T恤")
def make_shirt(Size,Typeface):
    print("\nI need a " + Size + " T-shirt.")
    print("The word " + Typeface + " is printed on this T-shirt.")
make_shirt("S","Just do it")

print("8-4 大号T恤")
#修改函数make_shirt()，使其在默认情况下制作印有字样'I love Python'的大号T恤。
#调用这个函数来制作如下T恤:一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤(尺码无关紧要)。
def make_shirt(Size,Typeface = "love Python"):
    print("\nI need a " + Size + " T-shirt.")
    print("The word " + Typeface + " is printed on this T-shirt.")
make_shirt("")
make_shirt("L")
make_shirt("M")
make_shirt(Size="M",Typeface="I am happy")
make_shirt(Typeface="I am happy",Size="M")

print("\n8-5 城市")
#编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，如
# Reykjavik is in Iceland.给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家
def scribe_city(city,country = "china"):
    print(city + " is in " + country.title() + ".")
scribe_city("Beijing")
scribe_city(city="shenzheng")
scribe_city(city="yongzhou")
scribe_city("Mumbai","Idia")

print("\n8.3 返回值")
#函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值称为返回值。在函数中，
#可使用return语句将值返回到调用函数的代码行。返回值让我们能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

print("\n8.3.1 返回简单值")
#这一个函数，它接受名和姓并返回整洁的姓名：
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
#调用返回值的函数时，需要提供一个变量，用于存储返回的值。这里将返回值存储在了变量musician中。输出为整洁的姓名：Jimi Hendrix

print("\n8.3.2 让实参编程可选的")
#有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。
#例如，假设我们要扩展函数get_formatted_name()，使其处理中间名，为此，可将其修改成类似与下面这样：
def get_formatted_name(first_name,last_name,middle_name = ""):
    if middle_name:   #使用if进行判断，middle_name是否有参数传进来
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name("Geng","xue","chang")
print(musician)
#在函数体中，我们检查是否提供了中间名。Python将非空字符串解读为True，因此如果函数调用中间提供了中间名，if middle_name将为True。如果提供
#了中间名，就将名、中间名和姓合并为姓名，然后将其修改为首字母大写格式，并返回到函数调用行。在函数调用行，将返回的值存储在变量musician中；然后
#将这个变量的值打印出来。如果没有提供中间名，middle_name将为空字符串，导致if测试未通过，进而执行else代码块；只是用名和姓来生成姓名，并将设置
#好格式的姓名返回给函数调用行。在函数调用行，将返回的值存储在变量musician章；然后将这个变量的值打印出来。

print("\n8.3.3 返回字典")
#函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个表示人的字典：
def build_person(first_name,last_name):
    person = {"first":first_name,"last":last_name}   #返回一个字典，其中包含有关一个人的信息
    return person
musician = build_person("jimi",'hendrix')
print(musician)

#我们可以轻松地扩展这个函数，使其接受可选值，如中间名、年龄、职业或我们要存储的其他信息。例如，修改让我们还能存储年龄：
def build_person(first_name,last_name,age=""):
    person = {"first":"first_name","last":"last_name"}
    if age:
        person["age"] = age
    return person
musician = build_person("jimi","hendrix","18")
print(musician)  #我们新增了一个可选形参age，其默认值设置为空字符串。如果函数调用中包含这形参的值，这个值将存储到字典中。

print("\n8.3.4 结合使用函数和while循环")
#可将函数同本书前面介绍的任何Python结构结合起来使用。例如，下面将结合使用函数get_formatted_name()和while循环，
#以更正规的方式问候用户，下面尝试使用名和姓跟用户打招呼：
#def get_formatted_name(first_name,last_name):
   # full_name  = first_name + " " + last_name
    #return full_name.title()

#while True:
    #print("\nPlease tell me your name: ")
    #print("Enter 'q' at any time to quit")

    #f_name = input("First name: ")
    #if f_name == 'q':
        #break

    #l_name = input("Last name: ")
    #if l_name == 'q':
        #break

    #formatted_name = get_formatted_name(f_name,l_name)
    #print("\nHello, " + formatted_name)

print("\n动手试一试")
#8-6 城市名： 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
def city_country (city,country):
    print(city.title() + "," + country.title())
city_country("shenzheng","china")
city_country("Mumbai","Idia")

print("\n8-7 专辑：编写一个名为make_album()的函数，创建一个描述音乐专辑的字典。这个函数应接受歌手名字和专辑名，并返回一个包含")
#这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回值，以核实字典正确地存储了专辑的信息。")
def make_album(singer_name,album_name,songs=0):

    Music_album = {"singer_name":singer_name,"album_name":album_name}
    if songs > 0:
        Music_album["songs"] = songs
    return Music_album

new_album = make_album("zhaolei","chengdou",1)
print(new_album)

new_album = make_album("zhangjie","you are big")
print(new_album)
#如果使用return，则必须有接收变量，因为return是把函数运行的结果返回给调用行，必须有一个指定的变量能够接收这个返回值，
#否则，就必须输出这个函数。

print("\n8.4 传递列表")
#我们经常会发现，向函数传递列表很有用，这种列表包含的可能是名字，数字或更复杂的对象(如字典)。将列表传递给函数后，
#函数就能直接访问其内容。下面使用函数来提高处理列表的效率。
#假设有一个用户列表，我们要问候其中的每位用户。下面的示例将一个名字列表传递给一个名为greet_users()的函数，这个函数问候列表中的每个人：
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['zengmingzhu','gengchangxue','linzhiling','zhaobenshan']
greet_users(usernames)

print("\n8.4.1 在函数中修改列表") #？？
#将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让我们能够高效地处理大量的数据。
#来看一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列表中，打印后移到另一个列表中。
#下面是在不使用函数的情况下模拟这个过程的代码：

print("\n8.4.2 禁止函数修改列表")  #？？
print("\8.5 传递任意数量的实参")   #Python允许函数从调用语句中收集任意数量的实参。
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

print("\n我们可以将这条print语句替换为一个循环，对配料列表进行遍历，并对顾客点的比萨进行描述：")
def make_pizza(*toppings):  #形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元祖中
    print("\nMaking a pizza with the following toppings：")
    for topping in toppings:
        print(topping)
make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

print("\n8.5.1 结合使用位置实参和任意数量实参")
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，
# 再将余下的实参都收集到最后一个形参中。
#例如，如果前面的函数还需要一个表示比萨的尺寸的实参，必须将该形参放在形参*toppings的前面：
def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + " inch pizza with the following toppings：")
    for topping in toppings:
        print(topping)
make_pizza("5inch","pepperoni")
make_pizza(7,"mushrooms","green peppers","extra cheese")
#ython将收到的第一个值存储在形参size中，并将其他的所有值都存储在元组toppings中。在函数调用中，首先指定表示比萨的尺寸的实参，然后根据需要制定任意数量的配料：

print("\n8.5.2  使用任意数量的关键字实参")
#需接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键-值对——
#调用语句提供了多少就接受多少。一个这样的示例是创建用户简介：我们知道我们将收到有关用户的信息，但不确定会是什么样的信息。
#在下面的示例中，函数build_profile()接受姓和名，同时还接受任意数量的关键字实参：
def build_profile(first,last,**user_info):
    profile = {}     #创建一个字典，其中包含我们知道的有关用户的一切
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value  #遍历字典user_info中的键-值对，并将每个键-值对都加入到字典profile中
    return profile            #我们将字典profile返回给函数调用行。
user_profile = build_profile("albert","einstein",location = "princeton",field = "physics")
#调用build_profile(),向它传递名'albert'、姓('einstein')和两个键-值对(location = 'princeton'和field = 'physics').并将返回profile存储在变量user_profile中，再打印这个变量：
print(user_profile)
#其实就是函数参数的方法，*代表的以元组的形式进行输入的情况，而**代表的是以字典输入的情况，并且字典要以键-值对的方式进行输出才行，
# **代表创建一个空的字典，把用户输入的参数传给这个空的字典。return是返回到调用函数的位置，返回生成的结果到函数调用的位置。

print("\n动手试一试")
print("8-12  三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息")
# 对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def make_sandwich(*toppings):
    print("\nMaking sandwich with the following toppings: ")
    for topping in toppings:
        print(topping)
make_sandwich("rice")
make_sandwich("wirte",'milk','pepperoni')

def car(manufacturer,model,**other_message):
    all_car = {}
    all_car["manufacturer"] = manufacturer
    all_car["model"] = model
    for key, value in other_message.items():
        all_car[key] = value
    return all_car
new_car = car("china","big",city= "biejing",much= 100)
print(new_car)

