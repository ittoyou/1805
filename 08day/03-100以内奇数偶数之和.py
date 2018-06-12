


count = int(input("请输入一个数字"))
o_sum =0 
j_sum =0
i = 0
while i < count:
	print("当前数字:%d"%i)
	i+=1
	if i%2 ==0:#这是偶数
		o_sum = o_sum + i
	elif i %2 !=0:
		j_sum = j_sum + i
print("偶数和为:%d"%o_sum)
print("奇数和为:%d"%j_sum)









