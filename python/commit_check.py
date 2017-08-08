#!/usr/bin/python3
message_list=[]
with open("message.log","r") as f:
	for line in f.readlines:
		message_list.append(line)
print(message_list)
if message_list[0] == "\n":
	print("Subject shouldn't be blank")
if message_list[1] == "\n":
	print("Second Line check pass"):
else:
	print("Second Line check Failed")
if message_list[len(message_list)-1].startswith("ChangeID:"):
	print("Last Line check pass")
