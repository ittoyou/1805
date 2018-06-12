'''
两个人 电脑和玩家
A>B
A<B
'''


import random
i=0
pc = random.randint(1,100)
while i < 10:
	py = int(input("请选择数字"))
	if pc>py:
			print("你的数字小了")
	elif pc<py:
			print("你的数字大了")
	elif pc==py:
		print("你猜对了")
			i=10停止循环















