list = []
print("学生信息管理系统".center(50,"*"))
while True:
	print("1:添加学生信息".center(50," "))                             
	print("2:查找学生信息".center(50," "))                       
	print("3:删除学生信息".center(50," "))                             
	print("4:修改学生信息".center(50," "))
	print("5:打印学生信息".center(50," "))                             
	num = int(input("请选择功能")) 
	if  num == 1:  
		d = {}       
		#while True:  
		name = input("请输入要添加学生的名字")  
		if len(name) > 4: 
			print("名字太长，请重新输入")
			continue
		phone = input("请输入学生联系方式") 
		if len(phone) != 11 or phone.startswith("1") ==False:
			print("手机号确认有误，请重新输入")
			continue
	elif num == 2:  
		name = input("请输入要查找的学生姓名")
		flag = False
		for i in list:
			if name == i["name"]:
				print("姓名:%s\n电话:%s"%(i["name"],i["phone"]))
				flag = True
				break
	elif num == 3:
		name = input("请输入要删除的学生姓名")
		flag = False
		for position,i in enumerate(list):
			if name == i["name"]:
				flag = True
				print("1:确认删除")
				print("2:取消删除")	
				num_1 = int(input("请选择功能"))
				if num_1 == 1:
					list.pop(position)
				break
		if flag == False:
			print("查无此人")
	elif num == 4:
		name = input("请输入要改的学生姓名")
		flag = False
		for i in list:
			if name == i["name"]:
				print("1:修改名字")
				print("2:修改电话")
				num_2 = int(input("请选择功能"))
				if num_2 ==1:
					new_name = input("请输入新的名字")
					i["name"] = new_name
				elif num_2 == 2:
					new_phone =int(input("请输入新的电话"))
					i["phone"] = new_phone
				flag = True
				break
		if flag == False:
			print("查无此人")
	elif num == 5:
		print("名字\t电话")
		for i in list:
			print(" "+i["name"]+"\t "+i["phone"])				
