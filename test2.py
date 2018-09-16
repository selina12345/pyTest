#9-10导入Restaurant类
from lei import Restaurant
my_restanrant = Restaurant("Xiao_LI_Restaurant", "west_food")
my_restanrant.describe_restaurant()

#9-11导入Admin类
from lei import User,Privilegs,Admin
my_user = User("LI", "ZHI", 18, "china")
my_user.describe_user()
my_user.greet_user()

my_admin = Admin("Yes i do")
my_admin.show_privilegs2()

#9-12多个模块
from lei import User

class User():
    def __init__(self, first_name, last_name, age):
        self_first_name1 = first_name
        self_last_name1 = last_name
        self_age1 = age

    def describe_user(self):
        print("my name is" + self.first_name1 + self.last_name1 + " I am" + str(self.age))

    def greet_user(self):
            print("Nice to meet you !" + self.first_name1 + self.last_name1)

    user = User("li", "zhixin",18)
    user.describe_user()
    user.greet_user()








