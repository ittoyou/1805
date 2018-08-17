def jisuanqi(a,b,c):
	if c == "+":
		z = a+b
		print("%d+%d=%d"%(a,b,z))
	elif c == "-":
		z = a-b
		print("%d-%d=%d"%(a,b,z))
	elif c == "*":
		z = a*b
		print("%d*%d=%d"%(a,b,z))
	elif c == "/":
		if b != 0:
			z = a/b
			print("%d/%d=%.02f"%(a,b,z))
		else:
			print("输入有误")
a = int(input("请输入a的值"))
b = int(input("请输入b的值"))
c = input("请输入+-*/")
jisuanqi(a,b,z)


























