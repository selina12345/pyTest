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
ll="d" not in theList
print(ll)