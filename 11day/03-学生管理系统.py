student = []
while True:
	fun = int(input("1---添加，2---删除，3---修改，4---查找"))
	if fun == 1:
		name = input("请输入名字") 
		student.append(name)
	elif fun == 2:
		name = input("请输入要删除的名字")
		if name in student:
			student.remove(name)
		else:
			print("查无此人")
	elif fun == 3:
		name = input("请输入要修改的名字")
		name.index(student)
		
















