list = []
def register(account,pwd):
	user ={}
	if len(account) == 11 and account.startswith("1") and len(pwd) > 6:
		print("注册成功")
		user["account"] = account
		user["pwd"] = pwd
		list.append(user)
	else:
		print("注册失败")
def login(account,pwd):
	for i in list:
		if account == i["account"] and pwd == i["pwd"]:
			print("登录成功")
		else:
			print("登录失败")
acc = input("请选择一个账号")
pwd = input("请设置一个密码")
register(acc,pwd)
if list:
	acc = input("请输入账号")
	pwd = input("请输入密码")
	login(acc,pwd)











