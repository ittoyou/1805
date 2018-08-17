list = []
print("名片管理系统".center(50,"*"))
while True:
	print("1:添加名片".center(50," "))
	print("2:查找名片".center(50," "))
	print("3:修改名片".center(50," "))
	print("4:删除名片".center(50," "))
	print("5:打印名片".center(50," "))
	num = int(input("请选择功能"))
	if num == 1:
		d = {}
		name = input ("请输入要添加的名字")
		job = input("请输入要添加的职务")
		phone = input("请输入联系方式")
		company = input("请输入公司名称")
		address = input("请输入公司地址")
		d["name"] = name
		d["job"] = job
		d["phone"] = phone
		d["company"] = company
		d["address"] = address 
		list.append(d)
		print(list)
	elif num == 2:
		name = input("请输入要查找的姓名")
		job = input("请输入要查找的职位")
		phone = input("请输入要查找的联系方式")
		company = input("请输入要查找的公司名称")
		address = input("请输入要查找的公司地址")

		for i in list:
			if name == i["name"]:
				print("%s姓名\n%s职位\n%s联系方式\n%s公司名称\n%s公司地址"%(i["name"],i["job"],i["phone"],i["company"],i["address"]))
				break


























