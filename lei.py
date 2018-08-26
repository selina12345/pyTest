# class Restaurant():
# #     def __init__(self, restaurant_name, cuisine_type):
# #         self.restaurant_name = restaurant_name
# #         self.cuisine_type = cuisine_type
# #
# #     def describe_restaurant(self):
# #         print(self.restaurant_name.title())
# #         print(self.cuisine_type)
# #
# #     def open_restaurant(self):
# #         print("This restaurant is open for business.")

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

    def show_privilegs2(self):
        print("If you are an administrator account, you can have the following permissions: ")

class Admin2():
    def __init__(self, privilegs):
       self.privilegs = Privilegs()

privilegs2 = Admin2("can add post")
privilegs2.privilegs.show_privilegs()

privilegs = Admin("2324")
privilegs.privilegs2.show_privilegs()
