list = []
while True:
	print("菜单 1:乘坐 2:计算")
	menu = int(input("请选择:"))
	if menu ==1:
		month = int(input("请输入月份:"))
		if month >= 1 and month <=12:
			day = 30
		else:
			print("输入有误")
			break
		cishu = int(input("每天坐几次:"))
		km = int(input("请输入距离:"))
	elif menu == 2:
		all_money=0
		if km<=6:
			price=3
		elif km>6 and km<=12:
			price=4
		elif km>12 and km<=22:
			price=5
		elif km>22 and km<=32:
			price=6
		elif km>32 and (km-32)/20 == 0:
			price=6+(km-32)/20
		else: 
			price=6+int((km-32)/20)+1
		if all_money>100 and all_money<=150:
			price=price*0.8
		if all_money>150 and all_money<=400:
			price=price*0.5
		list.append(all_money)
		all_money=(all_money+price)*cishu*30
		print("%d月份花了:"%f元（month,all_money))
