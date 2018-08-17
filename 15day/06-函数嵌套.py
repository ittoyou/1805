import time
def player():
	i = 0
	while True:
		i+=1
		if i%2 ==0:		
			time.sleep(1)
			print("我喜欢玩游戏")
		elif i%2 != 0:
			time.sleep(1)
			print("我喜欢写代码")
player()






















