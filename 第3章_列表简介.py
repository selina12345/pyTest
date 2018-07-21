# 2018/5/8
Fruits = [1, 2, 3, 4]
print(Fruits)  # 创建一个列表，列表可以包含多个元素，并用【】表示列表，用逗号分隔,其中元素可以用数字，元素也可以是文本，数字

Fruits = ["apple", "banana", "orange", "peach"]
print(Fruits)

# 访问列表元素
Fruits = ["apple", "Banana", "orange", "peach"]
print(Fruits[0].title())
print(Fruits[1].lower())
print(Fruits[2].upper())
print(Fruits[3])
print(Fruits[-1])
# 获取列表元素只返回该元素，而不包括【】和引号，可在输出时将该元素的索引加上，第一个元素的索引从0开始，最后一个元素的索引可写成-1同时还可以结合字符串转换大小或者去掉空格等

# 使用列表中的各个值
Fruits = ["apple", "Banana", "Orange", "peach"]
message = "My favourite fruit" + " " + Fruits[1].lower() + " " + "and" + " " + Fruits[
    0].lower() + "," + "what about you" + "?"
print(message)  # 可使用拼接根据列表中的值来创建消息

# 动手试一试(p33)
names = ["selina", "sue", "candy", "fafa", "hester"]
print(names)

names = ["selina", "sue", "candy", ]
message = names[0] + ",good morning" + "!"
print(message)

message = names[1] + ",good morning" + "!"
print(message)

message = names[2] + ",good morning" + "!"
print(message)

transportation = ["aeroplane", "bicycle", "truck", "taxi"]
message = "I usually choose to take a " + transportation[3] + " home" + "."
print(message)

# 修改、添加和删除元素
Fruits = ["apple", "banana", "orange", "peach"]
print(Fruits)
Fruits[0] = "lemon"
Fruits[1] = "pear"
Fruits[2] = "mango"
Fruits[3] = "plum"
print(Fruits)  # 可以修改列表中任何一个元素

Fruits = []
Fruits.append('apple')
Fruits.append("banana")
Fruits.append("orange")
Fruits.append("peach")
print(Fruits)  # 在列表中添加元素 用append()来添加元素

Fruits = ["apple", "banana", "orange", "peach"]
Fruits.insert(0, "cherry")  # 在索引0处添加cherry，即在apple前面插入
Fruits.insert(2, "cherry")  # 同理在索引2处添加
print(Fruits)  # 在列表是插入元素，可用insert()在列表中任意位置添加元素

# 2018/5/9
Fruits = ["apple", "banana", "orange", "peach"]
print(Fruits)
del Fruits[0]
print(Fruits[1])  # 从列表中删除元素可使用del语句，同时要知道其元素的位置，即索引，可在输出加上索引去掉相应的括号和引号（del语句不删除元素后，元素不能继续使用）

Fruits = ["apple", "banana", "orange", "peach"]
print(Fruits)  # 先打印列表中所有的值
popped_Fruits = Fruits.pop()  # 将列表中末尾的值储存到新新的变量popped_Fruits中，使用pop()删除列表中任何位置的元素，只需在括号中指定要删除的元素索引即可
print(Fruits)  # 验证是否删除了末尾的值
print(popped_Fruits)  # pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

Fruits = ["apple", "banana", "orange", "peach"]
Fruits.remove("banana")
print(Fruits)  # 删除列表中的元素但并不知道其位置可用remove()

Fruits = ["apple", "banana", "orange", "peach"]
new_Fruits = "banana"
Fruits.remove(new_Fruits)
print(new_Fruits)  # 删除的元素可继续使用该删除的元素，并可打印一条消息说明其原因
print("i don not like" + " " + new_Fruits.title() + ".")

# P38动手试一试
dinner = ["selina", "sue", "candy", "fafa"]
message = "I want to have dinner with " + dinner[0] + " and " + dinner[1] + " and " + dinner[2] + " and " + dinner[
    3] + "."
print(message)

dinner = ["selina", "sue", "candy", "fafa"]
no_dinner = "fafa"
dinner.remove(no_dinner)
no_dinner = no_dinner.replace("fafa", "selina")
print(no_dinner + " can not come over for dinner" + ".")

dinner = ["selina", "sue", "candy", "fafa"]
dinner[-1] = "hester"
print(dinner)

dinner = ["selina", "sue", "candy", "fafa"]
dinner[-1] = "hester"
message = "I want to have dinner with " + dinner[0]
message1 = "I want to have dinner with " + dinner[1]
message2 = "I want to have dinner with " + dinner[2]
message3 = "I want to have dinner with " + dinner[-1]
print(message + "\n" + message1 + "\n" + message2 + "\n" + message3)

dinner = ["selina", "sue", "fafa"]
dinner.insert(0, "nana")
dinner.insert(2, "frank")
dinner.append("sam")
message = "I want to have dinner with " + dinner[0] + " and " + dinner[1] + " and " + dinner[2] + " and " + dinner[
    3] + " and " + dinner[4] + " and " + dinner[5] + "."
message1 = "as soon as I heard the news" + "," + "I could only invite two dinner to dinner" + "," + dinner[
    1] + " and " + dinner[2] + "."
print(message1)
pop1_dinner = dinner.pop(0)
pop2_dinner = dinner.pop(4)
pop3_dinner = dinner.pop(3)
message2 = "sorry," + pop1_dinner + ",I can not have dinner with you."
message3 = "sorry," + pop2_dinner + ",I can not have dinner with you."
message4 = "sorry," + pop3_dinner + ",I can not have dinner with you."
print(message2 + "\n" + message3 + "\n" + message4)
message5 = dinner[1] + ",You are on the invitation list."
message6 = dinner[2] + ",You are on the invitation list."
print(message5 + "\n" + message6)
print(dinner)
del dinner[2]
print(dinner)

# 3.3组织列表
# 3.3.1sort()对列表进行永永久性排序
names = ["selina", "sue", "candy", "fafa", "hester"]
names.sort()
print(names)
# sort(revenrse=True)可按字母相反顺序排列列表元素
names = ["selina", "sue", "candy", "fafa", "hester"]
names.sort(reverse=True)
print(names)

# 3.3.2使用函数sorted()对列表进行临时排序,按字母顺序排序(首字母，从a到Z顺序）
names = ["s", "ea", "c", "f", "h"]
print(sorted(names))

# 3.3.3反转列表元素排列顺序可用reverse()，可随时恢复到原来的顺序只需要对列表再次调用reverse()即可，注这不是指按与字母顺序相反的顺序排列
names = ["selina", "sue", "candy", "fafa", "hester"]
names.reverse()
names.reverse()
print(names)

# 3.3.4确定列表长度可用leb()函数，从1开始计算列表元素长度
names = ["selina", "sue", "candy", "fafa", "hester"]
print(len(names))

# p41动手试一试
where = ["KR", "JP", "US", "AU", "MX"]
print(where)

where = ["KR", "JP", "US", "AU", "MX"]
where.sort()
print(where)

where = ["UA", "BR", "CA", "DZ", "EG"]
print(sorted(where))

where = ["UA", "BR", "CA", "DZ", "EG"]
print(where)

where = ["UA", "BR", "CA", "DZ", "EG"]
where.sort(reverse=True)
print(where)

where = ["KR", "JP", "US", "AU", "MX"]
where.reverse()
print(where)

where = ["KR", "JP", "US", "AU", "MX"]
where.reverse()
where.reverse()
print(where)

where = ["KR", "JP", "US", "AU", "MX"]
where.reverse()
where.reverse()
where.sort()
where.sort(reverse=True)
print(where)

dinner = ["selina", "sue", "candy", "fafa"]
print(len(dinner))
