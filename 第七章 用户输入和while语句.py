print("7用户输入和while循环")
print("7.1函数input()的工作原理")
#函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便我们使用。
#提示输入，输入对象为string格式，返回值为string格式。
#例如，下面的程序让用户输入一些文本，再将这些文本呈现给用户：

#message = input("Tell me something, and I'll repeat it back to you: ")
#print(message)

#函数input()接受一个参数：既要向用户显示的提示或说明，让用户知道该如何做。在这个示例中，Python运行第一行代码时，用户将看到提示Tell me
#something, and I will repeat it back to you:。程序等待用户输入，并在用户按回车键后继续运行。用户输入存储在变量message中，就下来的print(
#message)将输入呈现给用户：
#Tell me something, and I'll repeat it back to you: Hello everyone
#Hello everyone

print("\n7.1.1  编写清晰的程序")
#每当我们使用函数input()时，都应指定清晰而易于明白的指示，准确地指出我们希望用户提供什么样的信息——指出用户该输入任何信息的提示都行，如：

#name = input("Please inter your name: ")
#print("Hello," + name.title()+ "!")

#prompt = "If you tell us who you are,we can personalize the massages you see."
#prompt += "\nwhat is your first name? "   # += 表示把左边的数加上右边的数的和赋值给左边的数的意思。如：a+=b等效于 a=a+b
#name = input(prompt)
#print('\nHello, ' + name.title())

#print("7.1.2 使用int()来获取数值输入") #函数input()输入的都是字符串格式。
#age = input("How old are you?")
#print(age)
#age = int(age)  #函数int()将数字的字符串表示转换为数值
#if age >= 1:
    #print("you are a child")
#else:
    #print("you are a adult")

print("\n7.1.3　求模运算符")
#处理数值信息时，求模运算符(%)是一个很有用的工具，它将两个数 相除 并返回 余数：
#求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。
number = 5
number_0 = 3
print(number % number_0)

#如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0.我们可以利用这一点来判断一个数是奇数还是偶数：
#number = input("Enter a number, and I will tell you if it's even or odd: ")
#number_0 = int(number)
#if number_0 % 2 == 0:  #偶数都能被2 整除,因此对一个数(number)和2执行求模运算的结果为零，即number % 2 == 0,那么这个数就是偶数；否则就是奇数。
    #print("\nThe number " + number + ' is even.')
#else:
    #print("\nThe number " + number + " is odd.")

print("\n7-1 汽车租赁:") #编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息
#rent_car = input("What kind of car do you need to rent? ")
#print("Let me see if I can find you a " + rent_car.title() + ".")

print("\n7-2 餐馆订位:")  #编写一个程序,询问用户有多少人用餐.如果超过8个人,就打印一条消息,指出没有空桌;否则指出有空桌。
#Dining = input("How many people are dining today?")
#print(Dining)
#Dining = int(Dining)  #input()返回的数据类型是str类型，不能直接和整数进行比较，必须先把str转换成整型，使用int()方法
#if Dining >= 8:
    #print("There is no empty table to eat now, wait 20 minutes.")
#else:
    #print("There are empty tables available for dining now.")

print("\n7-3 10的整数倍")  #让用户输入一个数字，并指出这个数字是否是10的整数倍。
#digital = input("Please enter a number:")
#digital = int(digital)
#if digital %10 == 0:
    #print("This number is an integer multiple of 10." + str(digital))
#else:
    #print("This number is not an integer multiple of 10." + str(digital))

print("\n7.2 while循环简介")
#for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止。
#我们可以使用while循环来数数，例如，下面的while循环从1数到5：
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#在第1行，我们将current_number设置为1，从而指定从1开始数。接下来的while循环被设置成这样：只要current_number小于或等于5，
#就接着运行这个循环。循环中的代码打印current_number的值，再使用代码current_number += 1将其值加1.
#只要满足条件current_number <= 5 ,Python就接着运行这个循环。由于1小于5，因此Python打印1，并将current_number加1，使其为2,；由于2小于5,
#因此Python打印2，并将current_number加1，使其为3，一次类推。一旦current_number大于5，循环将停止，整个程序也将到此结束：

print("\n7.2.2 让用户选择何时退出")
print("\n7.2.4  使用break退出循环")
#要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。break语句用于控制程序流程，
#可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按我们的要求执行要执行的代码。
#例如，来看一个让用户指出他到过哪些地方的程序。在这个程序中，我们可以在用户输入'quit'后使用break语句立即退出while循环：
#prompt = '\nPlease enter the name of a city you have visited: '
#prompt += "\nEnter 'quit' when you are finished. "
#while True:
    #cities = input(prompt)
    #if cities == 'quit':
        #break
    #else:
        #print("I'd love to go to " + cities.title() + ".")

print("\n7.2.5  在循环中使用continue")
#要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像break语句那样不再执行余下的代码
# 并退出整个循环。例如来看一个从1数到10，但只打印其中奇数的循环：
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
print(current_number)
#们首先将current_number设置成了0，由于它小于10，Python进入while循环。进入循环后，我们以步长1的方式往上数，因此current_number为1，接下
#来，if语句检查current_number与2的求模运算结果。如果结果为0(意味着current_number可能被2整除),就执行continue语句，让Python忽略余下的代码，
# 并返回到循环的开头。如果当前的数字不能被2整除，就执行循环中余下的代码，Python将这个数字打印出来。

print("\7.2.6 避免无限循环")
#每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。例如，下面的循环从1数到5：x = 1
x = 1
while x <= 5:
    print(x)
    x += 1   #但如果我们像下面不小心遗漏了代码x += 1，这个循环将没完没了地运行：
#但如果我们像下面不小心遗漏了代码x += 1，这个循环将没完没了地运行：这个循环将没完没了地运行！

print("\n7.3 使用while循环来处理列表和字典")
#到目前为止，我们每次都值处理了一项用户信息：获取用户输入，再将输入打印出来或作出应答；循环再次运行时，我们获悉了
#另一个输入值并作出响应。然而，要记录大量的用户和信息，需要在while循环中使用列表和字典。
#for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，
#可使用while循环。通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。

print("\n7.3.1  在列表之间移动元素")
#假设有一个列表，其中包含新注册但还为验证的网站用户；验证这些用户后如何将它们移到另一个已验证用户列表中呢？
# 一种办法是使用while循环，在验证用户的同时将其从未验证用户列表中提取出来，再将其加入到另一个已验证用户列表中：

unconfirmed_users = ['alice','brian','candace']  #首先，创建一个待验证用户列表
confirmed_users = []   #和一个用于存储已验证用户的空列表
while unconfirmed_users:   #验证每个用户，直到没有为验证用户为止,
    current_user = unconfirmed_users.pop()  #将每个经过验证的列表都移到已验证用户列表中
    confirmed_users.insert(1,current_user)
    print("Verifying user: " + current_user)
    confirmed_users.insert(1, current_user)
print("\nThe following users have been confirmed: ")  #显示所有已验证的用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#我们首先创建了一个未验证的用户列表，其中包含用户Alice、Brian和Candace，还创建了一个空列表，用户存储已验证的用户。while循环将不断地运行，
#直到列表unconfirmed_users变成空的，在这个循环中，函数pop()以每次一个的方式从列表unconfirmed_users末尾删除为验证的用户。由于Candance位于列
#表unconfirmed_users末尾，因此其名字将首先被删除、存储到变量current_user中并加入到列表confirmed_users中。接下来是Brian，然后是Alice。
#为模拟用户验证过程，我们打印一条验证消息并将用户加入到已验证用户列表中。未验证用户列表越来越短，而已验证用户列表越来越长。未验证用户列表
#为空后结束循环，再打印已验证用户列表：

print("\n7.3.2 删除包含特定值的所有列表元素") #可用remove()来操作
#假设我们有一个宠物列表，其中包含多个值为'cat'的元素。要删除所有这些元素，可不断运行一个while循环，直到列表中不在包含值'cat'，如下：
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

print("\n7.3.3 使用用户输入来填充字典")
