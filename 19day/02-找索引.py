list = [1,100,49,10,56,3,2,37]
#第一种方法
i = 0
while i < len(list):
	if list(i) == 3:
		print("索引是%d"%i)
		break
	i+=1
#第二种方法
position = list.index(3)	
print("索引是%d"%position)
#第三种方法
for p,i in enumerate(list):
	if i == 3:
		print("索引是%d"%p)
		break
#第四种方法
num = 3
min = 0
max = len(list)-1
center = int((min+max)/2)
if num in list:
	while True:
		if list[center]>num:
			center = center-1
		elif list[center]<num:
			center = center+1
		elif list[center] == num:
			print("索引是%d"%center) 
			break
















