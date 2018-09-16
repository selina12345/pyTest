# 2018/5/8 草稿复习
from 第5章_if语句 import price

all = ["you", "me", "he"]
message = "hello," + "i love " + all[0] + " and " + all[1] + " and " + all[2] + "!"
message_new = message.title()
print(message_new)

ALL = [1, 2, 3, 4]
ALL_NEW = ALL.pop()
print(ALL_NEW)

# 第四章 列表综合复习 2018.6.11
Country = ["cn", "ma", "th", "us"]
message1 = "I want to go to " + Country[1].title() + " and " + Country[-1].title() + "."
Country[1] = "za"
Country.append("br")
print(message1)
print(Country)
print(Country[0].title())
print(Country[1].title())
print(Country[2].title())
print(Country[3].title())
print(Country[4].title())
Country.insert(0, "kr")
print(Country)
Country_new = Country.pop()
message2 = "\nI don not go to " + Country_new.title() + "."
Country.remove("us")
print(message2)
print(Country)
Country.sort()
print(Country)
Country.sort(reverse=True)
print(Country)
message3 = sorted(Country)
print(message3)
Country.reverse()
print(Country)
message4 = len(Country)
print(message4)

# 操作列表复习 2018.6.23
colours = ["red", "blue", "green"]
for colour in colours:
    print(colour)
    print("my love colour is " + colour + "\n")
print("the " + colours[0] + " festive.")

for numbers in range(1, 6):
    print(numbers)
numbers = list(range(1, 6))
print(numbers)

numbers = list(range(3, 10, 3))
print(numbers)

squares = []
for numbers in range(1, 5):
    square = numbers ** 2
    squares.append(square)
    print(square)
squares = [numbers ** 2 for numbers in range(1, 5)]
print(squares)

count = list(range(1, 100))
print(max(count))
print(min(count))
print(sum(count))

theList = ["a", "b", "c"]
ll = "d" not in theList
print(ll)

print("--")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print("=-")
current_number = 0
while current_number < 10:
    if current_number == 5:
        current_number += 1
        continue
    print(current_number)
    current_number += 1

# 0-100偶数求和
i = 0
r = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        r += i
print(r)
print("0-100偶数求和 = %d " % r)


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name+self.last_name)
    def greet_user(self):
        print("hey,tony.")

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post","can ban user"]

    def show_privileges(self):
        for privileges2 in self.privileges:
            print("If you are an administrator account, you can have the following permissions: ")
            print("—" + privileges2)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

user = Admin('Tony','Stark')

user.privileges.show_privileges()

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name1 = first_name
        self.last_name1 = last_name
        self.age1 = age

    def describe_user(self):
        print("my name is" + self.first_name1+ self.last_name1 + " I am" + str(self.age1))

    def greet_user(self):
            print("Nice to meet you !" + self.first_name1 + self.last_name1)

user = User("li", "zhixin",18)
user.describe_user()
user.greet_user()

print("=======")
class User():
    def __init__(self, first_name, last_name, age,privielges):
        self.first_name1 = first_name
        self.last_name1 = last_name
        self.age1 = age
        self.privielges1 = privielges


    def describe_user(self):
        print("my name is" + self.first_name1 + self.last_name1 + " I am" + str(self.age1))

    def greet_user(self):
        print("Nice to meet you !" + self.first_name1 + self.last_name1)

class Admin(User):
        def __init__(self, first_name, last_name, age, privielges):
            super().__init__(first_name, last_name, age, privielges)
            privielges = ["can add post", "can delete post", "can ban user"]
            self.privielges1 = privielges

        def show_privileges(self):
            for privielges2 in self.privielges1:
                print("If you are an administrator account, you can have the following permissions: ")
                print("_" + privielges2)

admin = Admin("jiang", "jingjing",10, 111)
admin.show_privileges()

print("===================")
class Privileges():
    def __init__(self, privileges):
        self.privileges1 = privileges
        privielges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privielges2 in self.privileges1:
            print("you can have the following permissions: ")
            print("_" + privielges2)

class Admin():
    def __init__(self, privileges1):
        self.privielges1 = Privileges()

Admin1 = Admin("LI")
Privileges1 = Privileges("ZHI")
Admin1.privielges1.show_privileges()
Privileges1.show_privileges()


