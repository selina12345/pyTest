print("9.1  创建和使用类")
# 使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类Dog——它表示的不是特定的小狗，而是任何小狗。对于大多数宠物狗，
# 我们都知道些什么呢？它们都有自己的名字和年龄；我们还知道，大多数小狗还会蹲下和打滚。由于大多数小狗都具备上述两项信息（名字和年龄）和两种行为（蹲下和打滚），
# 我们的Dog类将包含它们。这个类让Python知道如何创建表示小狗的对象，编写这个类后，我们将使用它来创建表示特定小狗的实例。
# 类就是把一类具有共同属性的事物封装到一起，不用重复编写这些程序，编写好类后，需要的时候只需调用相应的类即可。

print("9.1.1  创建Dog类")


# 根据Dog类创建的每个实例都将存储名字和年龄。我们赋予了每条小狗蹲下（sit())和打滚(roll_over())的能力：
class Dog():
    """一次模拟小狗的简单尝试"""
    """方法__init__()是一个
特殊的方法，每当我们根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免
Python默认方法与普通方法发生名称冲突。"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        """以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量。selfname =
name 获取存储在形参name中的值，并将其存储到变量name中， 然后该变量被关联到当前创建的实例。selfage = age的作用与此类似。像这样可通过实例访
问的变量称为属性。"""
        self.name = name
        self.age = age

    def sit(self):
        """拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


class Dog():
    """一次模拟小狗的简单尝试"""
    """方法__init__()是一个
# 特殊的方法，每当我们根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免
# Python默认方法与普通方法发生名称冲突。"""


print("\n9.1.2  根据类创建实例")


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog("xiaobai", 6)  # my_dog 是结象
my_dog.sit()
my_dog.roll_over()
print("My dog's name is " + my_dog.name.title() + ".")  # (2)
print("My dog is " + str(my_dog.age) + ' years old.')  # (3)
"""我们将这个实例存储在变量
my_dog中。在这里，命名约定很有用：我们通常可以认为首字母大写的名称(如Dog)指的是类，
而小写的名称(如my_dog)指的是根据类创建的实例。"""

"""1.访问属性"""
# 要访问实例的属性，可使用句点表示法。在(2)处，我们编写了如下代码来访问my_dog的属性name的值：my_dog.name
# 句点表示法在Python中很常用，这种语法演示了Python如何获悉属性的值。在这里，Python先找到实例my_dog，再查找与这个实例相关联的属性name.
# 在Dog类中引用这个属性时，使用的是self.name。在(3)处，我们使用同样的方法来获取属性age的值。在前面的第一条print语句中，
# my_dog.name.title()将my_dog的属性name的值'willie'改为首字母大写的；在第2条print语句中，str(my_dog.age)将my_dog的属性age的值6转换为字符串。
# 输出的是有关my_dog的摘要：
#  My dog's name is Willie.
#  My dog is 6 years old.

"""2.调用方法"""
#  根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。下面来让小狗蹲下和打滚：
# my_dog = Dog('willie',6)
# my_dog.sit()
# my_dog.roll_over()
"""要调用方法，可指定实例的名称(这里是my_dog)和要调用的方法，并用句点分隔它们。遇到代码my_dog.sit()时，
Python在类Dog中查找方法sit()并运行其代码。Python以同样的方式解读代码my_dog.roll_over()。"""
#     Willie按我们的命令做了：
#     Willie is now sitting.
# 　　Willie rolled over!
"""这种语法很有用。如果给属性和方法指定了合适的描述性名称，如name、age、sit()和roll_over()，即便是从未见过的代码块，
# 我们也能够轻松地推断 出它是做什么的。"""

print("\n3.创建多个实例")


# 可按需求根据类创建任意数量的实例。下面再创建一个名为your_dog的实例：
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog("xiaobai", 6)  # my_dog 是对象
you_dog = Dog("xiaohuang", 10)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()

print("\nYou dog's name is " + you_dog.name.title() + ".")
print("You dog is " + str(you_dog.age) + ' years old.')
you_dog.sit()
you_dog.roll_over()

print("\n动手试一试")

# 9-1 餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type.创建一个名为describe_restaurant()
# 的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is open for business.")

my_restanrant = Restaurant("Xiao_LI_Restaurant", "west_food")
print("The restaurant's name is " + my_restanrant.restaurant_name.title() + ".")
print("The restaurant is good at " + my_restanrant.cuisine_type + ".")

my_restanrant.describe_restaurant()
my_restanrant.open_restaurant()


print("====")
#  9-3 用户：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
# 在User中定义一个名为describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
#  创建多个表示不同用户的实例，并对每个实例都调用上述方法。
class User():
    def __init__(self,first_name, last_name, age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.age)
        print(self.country.title())

    def greet_user(self):
        print("Hello, Nice to meet you " )

user_1 = User("li ","zhi_xin",18,"china")
user_2 = User("yang ","zhi_xin",22,"india")

user_1.describe_user()
user_2.greet_user()

print("\nMy name is " + user_1.first_name.title() + user_1.last_name.title() + " I am " + str(user_1.age) + ", I come from "  + user_1.country.title())
print("My name is " + user_2.first_name.title() + user_2.last_name.title() + " I am " + str(user_2.age) + ", I come from "  + user_2.country.title())





