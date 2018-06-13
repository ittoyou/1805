import random
number = random.randint(1,100)
for i in range(1,11):
	user = int(input("请输入一个数字"))
	if user > number:
		print("猜大了")
	elif user < number:
		print("猜小了")
	else:
		print("猜对了")
		break


















