list = []
def sushu():
	for i in range(2,201):
		flag = 1
		for j in range(2,i):
			if i%j == 0:
				flag = 0
				break
		if flag == 1:
			list.append(i)
	return list	
sushu()
print(list)			

















