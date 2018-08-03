#2018/5/4
a= "what fuck"
print(a.upper())   #upper() 将字符串转全部转换成小写

b= "what fuck" 
print(b.title())   #title() 将首字母转换成大写    

c= "WHAT FUCK"
print(c.lower())   #lower（）字母全部转换成小写

frist_name= "jiang"
last_name= "jing jing"
all= frist_name + " " + last_name
all_name = "hello,"  + all + ",how are you " + "?"
print(all_name.title())   #使用 + 拼接字符串

print("\tpython") #空行可用字符组合\t

print("\npython\nthis\nis") #换行符可用字符组合\n

print("all:\n\tpython\n\tthis\n\tis") #可使用”\n\t“让python换到下一行，并在下一行开头空两格

2018/5/6
like_it= "'python  '"
like_it=like_it.replace(' ','')   #replace(' ','')替换所有空格
print(like_it)

like_it= ' python '
like_it.rstrip()
like_it.lstrip()
like_it.strip()
print(like_it)   # strip()去掉首尾空格 lstrip()去掉左边空格 rstrip()去掉右边空格

message = "one of python's strengths is its diverse comunity."
print(message)  # 撇号位于两个双引号之间，python能正确读取，如使用单引号将出错

#第23页动手试一试
name = "lucy"
message = "hello," + name + "," "what do you do?"
message = message.title()
print(message)

famous_person = "What makes life dreary is the want of motive"
message = "George Eliot once said," + "'" + famous_person + ".'"
print(message)

message = "\tlucy"
print(message)

message = "\nlucy"
print(message)

message = "hello:\n\tgood morning!\n\tlucy"
print(message)

name = " lucy"
message = name.lstrip()
print(message)

name = "lucy   "
message = name.rstrip()
print(message)

name = "  lucy  "
message = name.strip()
print(message)

# 2018/5/6 数字
count = 3 / 2  # 可对数字进行+ - * /运算
print(count)

count = 2 ** 3  # 使用两个**表示乘方运算
print(count)

count = (2 + 3) * 2  # 可使用括号改变运算顺序
print(count)

count = 0.1 + 0.1
print(count)  # python将带小数点的数字都称为浮点数

age = 24
message = "lucy," + str(age) + "," + "happy brithday!"
print(message)  # 函数str()让pythony将非字符串转换字符串
print(4 + 4)
print(10 - 2)
print(8 * 1)
print(24 / 3)

print("7.2.2  让用户选择何时退出")
#可使用while循环让程序在用户愿意时不断地运行，如下面的程序，我们在其中定义了一个退出值，
#只要用户输入的不是这个值，程序就接着运行：
#prompt = '\nTell me something, and I will repeat it back to you: '
#prompt += "\nEnter 'quit' to end the program. "
#message = "" #将变量message的初始值设置为空字符串""，让Python首次执行while代码时有可供检查的东西。
#while message != 'quit':  # Python重新检查while语句中的条件。只要用户输入的不是单词'quit'，Python就会再次显示提示消息并
    #message = input(prompt)   # 等待用户输入。等到用户终于输入'quit'后，Python停止执行while循环，而整个程序也到此结束。
    #print(message)

#可不将单词"quit"打印出来，可使用if来判断：
#prompt = '\nTell me something, and I will repeat it back to you: '
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
    #message = input(prompt)
#if message != "quit":
    #print(message)
#这个程序与上面程序的区别是，这个程序在打印的时候进行了一次判断，判断在什么样的条件下才允许打印，什么样的情况下不允许打印。

print("\n7.2.3 使用标志")
#在要求很多条件都满足才能继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。整个变量被称为标志，可让程序
#在标志为True时继续运行,并在任何事件导致标志的值为False时让程序停止运行。这样在while语句中就只需检查标志的当前值是否为True，
#prompt = "\nTell me something and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to end the program. "
#active = True
#while active:
    #message = input(prompt)
    #if message == 'quit':
        #active = False
    #else:
        #print(message)
#我们将变量active设置成了True，让程序最初处于活动状态。这样做简化了while语句，因为不需要在其中做任何比较相关的逻辑，
#由程序的其他部分处理。只要变量active为True，循环就将继续运行。
#在while循环中，我们在用户输入后使用一条if语句来检查变量message的值。如果用户输入的是'quit', 我们就将变量active设置为False，
# 这将导致while循环不在执行。如果用户输入的不是'quit', 我们就将输入作为一条消息打印出来。

#在前一个示例中，我们将条件测试直接放在了while语句中，而在这个程序中，我们使用了一个标志来指出程序是否处于
#活动状态，这样如果要添加测试(如elif语句）以检查是否发生了其他导致active变为False的事件，将很容易。
print("\n7-4 动手试一试")
prompt = "\nPlease enter your choice of pizza ingredients: "
prompt += "\nEnter 'quit' to end the program."
message = " "
while message != "quit":
    message = input(prompt)
if message != "quit":
    print(message)


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
