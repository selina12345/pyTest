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