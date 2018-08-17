list =[]
for i in range(100,201):
	flag = 0 #假设100-200之间全是素数
	for j in range(2,i):#验证假设
		if i%j == 0:
			flag = 1
			break
	if flag == 0:#假设成立
		list.append(i)
print(list)
sum = 0
for i in list:
	sum+=i
print("和是%d"%sum)
list.reverse()
print(list)

















