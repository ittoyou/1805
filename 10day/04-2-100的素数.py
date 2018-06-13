for i in range(2,101):
	flag = 0 #假设2-100之间全是素数
	for j in range(2,i):#验证假设
		if i%j == 0:
			flag = 1
			break
	if flag == 0:#假设成立
		print(i)
















