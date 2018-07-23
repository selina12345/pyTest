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

33344



