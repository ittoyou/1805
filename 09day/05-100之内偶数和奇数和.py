number= int(input("请输入一个数字"))
o_sum=0
j_sum=0
i=0
for i in range(0,101):
	if i % 2 == 0:
		o_sum+=i	
	else:
		j_sum+=i
print("偶数和是:%d"%o_sum)
print("奇数和是:%d"%j_sum)












