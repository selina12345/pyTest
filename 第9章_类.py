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
my_dog中。在这里，命名约定很有用：我们通常可以认为首字母大写的名称(如Dog)指的是类，而小写的名称(如my_dog)指的是根据类创建的实例。"""

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


# 可按需求根据类创建任意数量的实例。下面再创建一个名为you_dog的实例：
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
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print("Hello," + self.first_name.title() + self.last_name.title() + " ,")

    def greet_user(self):
        print("Nice to meet you! ")


user_1 = User("li ", "zhi_xin", 18, "china")
user_2 = User("yang ", "zhi_xin", 22, "india")

user_1.describe_user()
user_1.greet_user()
print("My name is " + user_2.first_name.title() + user_1.last_name.title() + " I am " + str(
    user_1.age) + ", I come from " + user_1.country.title())
print("\n")

user_2.describe_user()
user_2.greet_user()
print("My name is " + user_1.first_name.title() + user_2.last_name.title() + " I am " + str(
    user_2.age) + ", I come from " + user_2.country.title())

print("\n9.2 使用类和实例")
# 们可以使用类来模拟现实世界中很多情景。类编写好后，我们的大部分时间都将花在使用根据类创建的实例上。
# 我们需要执行的一个重要任务就是修改实例的属性。我们可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
print("9.2.1 Car类")


# 下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法：
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def et_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.et_descriptive_name())

print("\n9.2.2 给属性指定默认值")


# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，
# 在方法__init__()内指定这种初始值是可行的；如果我们对某个属性这样做了，就无需包含为它提供初始值的形参。
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 现在，当Python调用方法__init__()来创建新实例时，将像前一个示例一样以属性的方式存储制造商、型号和生产年份。接下来，Python将创建一个名为
# odometer_reading的属性，并将其初始值设置为0.我们还定义了一个名为read_odometer()的方法，它让我们能够轻松地获悉汽车的里程。

print("\n9.2.3 修改属性的值")
print("1.直接修改属性的值")  # 要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为23：


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23  # 使用句点表示法来直接访问并设置汽车的属性odometer_reading。
my_new_car.read_odometer()

print("2.通过方法修改属性的值")


# 如果有替我们更新属性的方法，将大有裨益。这样，我们就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
# 下面的示例演示了一个名为update_odometer()的方法：
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):  # (1)
        self.odometer_reading = mileage

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)  # (2)
my_new_car.read_odometer()

# 对Car类所做的唯一修改是在（1）处添加了方法update_odometer()。这个方法接受一个里程值，并将其存储到self.odometer_reading中。
# 在（2）处，我们调用了update_odometer()，并向它提供了实参23（该实例对应于方法定义中的形参mileage)。它将里程表读数设置为23；
print("=====")


# 可对方法update_odometer()进行扩展，使其在修改里程表读数时做些额外的工作。下面来添加一些逻辑，禁止任何人将里程表的读数往回调：
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 40

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值
        # 禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 运行结果如下：
# 2016 Audi A4
# You can't roll back on odometer!
# This car has 40 miles on it.
# 现在，update_odometer()在修改属性前检查指定的读数是否合理。如果新指定的里程(mileage)大于或等于原来的里程(self.odometer_reading)，
# 就将里程表读数改为新指定的里程；否则就发出警告，指出不能往里程表往回调。

print("\n3.通过方法对属性的值进行递增")


# 有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记前增加了100英里的里程，
# 下面的方法让我们能够传递这个增量，并相应地增加里程表读数：
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """更新汽车里程表"""
        self.odometer_reading = mileage

    def increment_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_used_car = Car("subaru", 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# 我们可以轻松地修改这个方法，以禁止增量为负值，从而防止有人利用它来回拨里程表。

print("\n9.3  继承")
# 编写类时，并非总是要从空白开始。如果我们要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，它将自动获得另一个类的所
# 有属性和方法；原有的类称为父类，而新类称为子类。子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。
print("9.3.1  子类的方法__init__()")


#  创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法__init__()需要父类施以援手。
# 例如，下面来模拟电动汽车，电动汽车是一种特殊的汽车，因此我们可以在前面创建的Car类的基础上创建新类ElectricCar，
# 这样我们就只需为电动汽车特有的属性和行为编写代码。
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 40

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


class ElectricCar(Car):
    # 定义子类时，必须在括号内指定父类的名称。
    """电动汽车的独特之处"""

    def _init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息。
        super().__init__(make, model, year)  # """初始化父类的属性"""
        # super()是一个特殊函数，帮助Python将父类和子类关联起来，这行代码让Python调用ElectricCar的父类的方法__init__()，# 让ElectricCar实例包含父类的所有属性。

    def y(self):
        print(self.make + self.model + str(self.year))


my_tesla = ElectricCar("tesla", "models", 2016)
name = my_tesla.get_descriptive_name()
print(name)

print("\n9.3.4 重写父类的方法")


# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，
# 即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
# 假设Car类有一个名为fill_gas_tank()的方法，它对全电动汽车来说毫无意义，因此我们可能想重写它。下面演示了一种重写的方式：
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 40

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def fill_gas_tank(self):
        print("As")

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


class ElectricCar(Car):  # 定义子类时，必须在括号内指定父类的名称。
    """电动汽车的独特之处"""

    def _init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息。
        super().__init__(make, model, year)  # """初始化父类的属性"""
        self.battery = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery) + "-kwh battery.")

    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas.")


my_tesla = ElectricCar("tesla", "models", 2016)
name = my_tesla.get_descriptive_name()
print(name)
my_tesla.get_descriptive_name()
my_tesla.fill_gas_tank()
# 现在，如果有人对电动汽车调用方法fill_gas_tank()，Python将忽略Car类中的方法fill_gas_tank()，转而运行上述代码。
# 使用继承时，可让子类保留从父类哪里继承而来的精华，并剔除不需要的糟粕。

print("\n9.3.5  将实例用作属性")


# 使用代码模拟实物时，我们可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，
# 可能需要将类的一部分作为一个独立的类提取出来。我们可以将大型类拆分成多个协同工作的小类。
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 40

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值
        # 禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


class Battery():  # 定义了一个名为Battery的新类，它没有继承任何类。
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):  # 方法__init__()除self外，还有另一个形参battery_size。这个形参是可选的：
        # 如果没有给它提供值，电瓶容量将被设置为70.方法describe_battery()也移到了这个类中。
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):  # 方法describe_battery()也移到了这个类中。
        print("This car has a " + str(self.battery_size) + '-kwh battery.')


class ElectricCar(Car):  # 在ElectricCar类中，我们添加了一个名为self.battery的属性，让Python创建一个新的Battery实例(由于没有指定尺寸，因此默认值是70),
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化电动车的属性"""
        super().__init__(make, model, year)  # 将该实例存储在属性self.battery中。每当方法__init__()被调用时，
        self.battery = Battery()  # 都将执行该操作；因此现在每个ElectricCar实例都包含一个自动创建的Battery实例。


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  # 我们创建一辆电动汽车，并将其存储在变量my_tesla中。要描述电瓶时，需要使用电动汽车的属性battery：

print("\n下面再给Battery类添加一个方法，它根据电瓶容量报告汽车的续航里程:")


class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 40

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值
        # 禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + '-kwh battery.')

    def get_range(self):
        if self.battery_size == 70:  # 新增的方法get_range()做了一些简单分析：如果电瓶的容量为70kwh,它就将续航里程设置为240英里；
            range = 240
        elif self.battery_size == 85:  # 如果容量为85kwh，就将续航里程设置270英里，然后报个这个值。
            range = 270
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
            print(message)


class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self, make, model, year):
        '''初始化电动车的属性'''
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.battery_size = 85
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 输出了汽车的续航里程(这取决于电瓶的容量):
# 2016 Tesla Model S
# This car has a 85-kwh battery.
# This car can go approximately 270 miles on a full charge.

print("\n动手试一试")


#  9-6  冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。
# 添加一个名为flavors的属性，用于存储一个有各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例。并调用这个方法。
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is open for business.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        flavors = ['vanilla', 'coffee', 'blueberry', 'chocolates', 'green tea']
        self.flavors = flavors

    def describe_icecream(self):
        print("The icecream tastes: ")
        for flavor in self.flavors:
            print(" --" + flavor)

my_restanrant = IceCreamStand("Xiao_LI_Restaurant", "west_food", )
print("The restaurant's name is " + my_restanrant.restaurant_name.title() + ".")
print("The restaurant is good at " + my_restanrant.cuisine_type + ".")

my_restanrant.describe_restaurant()
my_restanrant.open_restaurant()
my_restanrant.describe_icecream()

print("\n9.7 管理员")
class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name2 = first_name
        self.last_name2 = last_name
        self.age2 = age
        self.country2 = country

    def describe_user(self):
        print("Hello," + self.first_name2.title() + self.last_name2.title() + " ,")

    def greet_user(self):
        print("Nice to meet you! ")

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        privilegs = ["can add post", "can delete post", "can be user"]
        self.privilegs2 = privilegs

    def show_privilegs(self):
        print("If you are an administrator account, you can have the following permissions: ")
        for privileg in self.privilegs2:
            print("—" + privileg)

all_users = Admin("li", "zhixin", 18, "china")
all_users.describe_user()
all_users.greet_user()
all_users.show_privilegs()

print("\n9.8 权限")
# # 编写一个名为 Privileges 的类，它只有一个属性——privileges，其中
# # 存储了练习 9-7 所说的字符串列表。将方法 show_privileges()移到这个类中。在 Admin
# # 类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法
# # show_privileges()来显示其权限。
class Privilegs():
    def __init__(self):
        self.privilegs2 = ["can add post", "can delete post", "can ban user"]

    def show_privilegs(self):
        print("If you are an administrator account, you can have the following permissions: ")
        for privileg in self.privilegs2:
            print(privileg)

class Admin():
    def __init__(self, privilegs):
        self.privilegs2 = Privilegs()

privilegs = Admin("2324")
privilegs.privilegs2.show_privilegs()





