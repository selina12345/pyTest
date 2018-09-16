print("10.1.1读取整个文件")
# 要读取文件，需要一个包含几行文本的文件。下面首先来创建一个文件，它包含精确到小数点后30位的圆周率值，且在小数点后每10处换行：
# 下面的程序打开并读取这个文件，再将其内容显示到屏幕上：
with open("pi_digits.txt") as file_obiect:
    contents = file_obiect.read()
    print(contents)

# 函数open()接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。
# 函数open()返回一个表示文件的对象.在这里，open('pi_digits.txt'),返回一个表示文件pi_digits.txt的对象；
# Python将这个对象存储在我们将在后面使用的变量中。这里储存在contents变量中

print("\n10.1.2 文件路径")
# 要让Python打开不与程序文件在同一个目录中的文件，需要提供文件路径，它让Python到系统的特定位置去查找。
# 由于文件夹text_files位于文件夹python_work中，因此可使用相对文件路径来打开该文件夹中的文件。相对文件路径让Python到指定的位置去查找，
# 而该位置是相对于当前运行程序所在目录的。在Linux和OS X中，我们可以这样编写代码：
# with open('text_files/filename.txt') as file_object:
# 我们还可以将文件在计算机中的准确位置告诉Python，这样就不用关心当前运行的程序存储在什么地方了。这称为绝对文件路径。

# 注意： Windows系统有时候能够正确地解读文件路径中的斜杠。如果你使用的是Windows系统，且结果不符合预期，请确保在文件路径中
# 使用的是反斜杠。另外，由于反斜杠在Python中被视为转义标记，为在Windows中确保万无一失，应以原始字符串的方式指定路径，即在开头的单引号前加上r.

# f = open(r'‪E:\pi_digits.txt')
#
# with f as file_object:
#     cotents = file_object.read()
#     print(cotents.rstrip())   ？？？？？

print("\n10.1.3 逐行读取")
# 读取文件时，常常需要检查其中的每一行：我们可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。
# 如我们可能要遍历一个包含天气数据的文件，并使用天气描述中包含字样sunny的行.在新闻报道中,我们可能会查找包含标签 headline的行，
# 并按特定的格式设置它。要以每次一行的方式检查文件，可对文件对象使用for循环：
filename = "pi_digits.txt"
"""将读取的文件存储在变量filename中"""
with open(filename) as file_obiect:
    """调用open()后，将一个表示文件及其内容的对象存储到了变量file_object中.7这里也使用了关键字with,让Python负责妥善地打开和关闭文件."""
    for line in file_obiect:
        """为查看文件的内容，我们通过对文件对象执行for循环来遍历文件中的每一行。"""
        print(line.rstrip())   #打印时发现每一行多了空白行，可用rstrip()删除多余的空白行

print("\n10.1.4创建一个包含文件各行内容的列表")
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块访问文件的内容，可在with代码块内将文件的
# 各行存储在一个列表中，并在with代码块外使用该列表：我们可用立即处理文件的各个部分，也可推迟到程序后面再处理。
# 下面的示例在with代码块中将文件pi_digits的各行存储在一个列表中，再在with代码块外打印它们：
filename = "pi_digits.txt"
with open(filename) as file_obiect:
    lines = file_obiect.readlines()
    """readlines()方法是指读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素,比较占内存,这里将文件存储在lines中"""
for line in lines:
    print(line.rstrip())
    """由于列表lines的每个元素都对应于文件中的一行，因此输出与文件内容完全一致："""

print("\n10.1.5 使用文件的内容")
#将文件读取到内存中后，就可以以任何方式使用这些数据了。下面以简单的方式使用圆周率的值。首先，我们创建一个字符串，
# 含文件中存储的所有数字，且没有任何空格：
filename = "pi_digits.txt"
with open(filename) as file_obiect:
    lines = file_obiect.readlines()

pi_string = ""  #创建一个变量pi_string,用于存储圆周率。
for line in lines:
    pi_string = pi_string + line.rstrip()  #使用一个循环将各行都加入pi_string,并删除每行末尾的换行符。
print(pi_string)   #打印这个字符串
print(len(pi_string))   #打印这个字符串长度

#在变量pi_string存储的字符串中，包含原来位于每行左边的空格，为删除这些空格，可使用strip()而不是rstrip():
filename = "pi_digits.txt"
with open(filename) as file_obiect:
    lines = file_obiect.readlines()
pi_string = ""
for line in lines:
    pi_string = pi_string + line.strip()
print(pi_string)
print(len(pi_string))
# 3.141592653589793238462643383279
# 32

# 注意：读取文本文件时，Python将其中的所有文本都解读为字符串。如果我们读取的是数字，并要将其作为数值使用，
# 就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数

print("\n10.1.6包含一百万的大型文件")
# 前面我们分析的都是一个只有三行的文本文件，但这些代码示例也可以处理大得多的文件。如果我们有一个文本文件，其中包含精确到
# 小数点后1000000位而不是30位的圆周率值，也可创建一个包含这些数字的字符串。为此，我们无需对前面的程序做任何修改，只需将这个
# 文件传递给它即可。在这里，我们只打印到小数点后50位，以免终端会显示全部1000000位而不断地翻滚：
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ""
# for line in lines:
# pi_string += line.strip()
# print(pi_string[:52] + "......")
# print(len(pi_string))
#对于我们可处理的数据量，Python没有任何限制；只要系统的内存足够多，我们想处理多少数据都可以。

print("\n10.1.7 圆周率值中包含你的生日吗")
# 我一想知道自己的生日是否包含在圆周率中。下面来扩展刚才编写的程序，以确定某个人的生日是否包含在圆周率值的前1000000位中。
# 生日表示为一个由数字组成的字符串，再检查这个字符串是否包含在pi_string中：
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()
#
# birthday = input("Enter your birthday,in the form mmddyy: ")  #提示用户输入生日
# if birthday in pi_string:  #检查是否包含在pi_string中
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appears in the first million digits of pi!")

print("\nP169 动手试一试")
print("10-1 python学习笔记")
with open("learning_python.txt") as learning_object:
    notes = learning_object.read()
    print(notes)

print("\n逐行读取")
notes = "learning_python.txt"
with open(notes) as learning_object:
    for line in learning_object:
        print(line.rstrip())

print("\n存储在新的列表中")
notes = "learning_python.txt"
with open(notes) as learning_object:
    lines = learning_object.readlines()

new_notes = " "
for line in lines:
    new_notes = new_notes + line
print(new_notes)