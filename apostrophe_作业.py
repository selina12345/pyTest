message = "one of python's strengths is its diverse comunity."
print(message)    #撇号位于两个双引号之间，python能正确读取，如使用单引号将出错

#第23页动手试一试
name= "lucy"
message = "hello," + name + "," "what do you do?"
message = message.title()
print(message)

famous_person= "What makes life dreary is the want of motive"
message = "George Eliot once said," +"'"+famous_person+".'"
print(message)

message= "\tlucy"
print(message)

message= "\nlucy"
print(message)

message= "hello:\n\tgood morning!\n\tlucy"
print(message)

name= " lucy"
message=name.lstrip()
print(message)

name= "lucy   "
message= name.rstrip()
print(message)
 
name= "  lucy  "
message= name.strip()
print(message)

print(4+4)
print(10-2)
print(8*1)
print(24/3)
