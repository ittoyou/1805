def cul_num(num):
	if num >= 1:
		result = num*cul_num(num-1)
	else:
		result = 1
	return result
res = cul_num(5)
print(res)














