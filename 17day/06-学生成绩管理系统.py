#coding=utf-8 
  
#保存学生信息 
studentList=[] 
  
def addInfo(name,addr): 
 tempInfo={} 
 tempInfo['name']=name 
 tempInfo['addr']=addr 
 studentList.append(tempInfo) 
 print(studentList) 
  
def delInfo(number): 
 if number<len(studentList) and number>=0 : 
  del studentList[number] 
  
 else: 
  print("您输入的序号有误:") 
  
def changeInfon(modifNum,name,addr): 
 if modifNum<len(studentList) and modifNum>=0 : 
  tempInfo={} 
  tempInfo['name']=name 
  tempInfo['addr']=addr 
  studentList[modifNum]=tempInfo 
  
 else: 
  print("您输入的序号有误:") 
   
def findInfo(findName): 
  i=0
  for info in studentList: 
  if findName ==info['name']: 
   print("您要查找的信息为%i %s %s"%(i,info['name'],info['addr'])) 
  
  
while True: 
 print("-"*30) 
 print("请输入您的选项") 
 print("1.新增学生信息") 
 print("2.删除学生信息") 
 print("3.修改学生信息") 
 print("4.查询学生信息") 
 print("-"*30) 
  
  
#等待用户输入选项 
 choose=int(raw_input("请输入您的选项:")) 
  
  
 if 1==choose: 
  name=raw_input("请输入学生的姓名:") 
  addr=raw_input("请输入学生的籍贯:") 
  addInfo(name,addr) 
  
 elif 2==choose: 
  if 0==len(studentList): 
   print("当前系统没用任何学生信息") 
   continue
  i=0
  for info in studentList: 
   print("%i  %s  %s"%(i,info['name'],info['addr'])) 
   i+=1
  number=int(raw_input("请输入要删除的序号:")) 
  delInfo(number) 
  print("删除之后的信息为：%s"%studentList) 
  
 elif 3==choose: 
  i=0
  for info in studentList: 
   print("%i  %s  %s"%(i,info['name'],info['addr'])) 
   i+=1
  modifNum=int(raw_input("请输入要修改的序号:")) 
  name=raw_input("请输入学生的姓名:") 
  addr=raw_input("请输入学生的籍贯:") 
  
  changeInfon(modifNum,name,addr) 
  print("修改之后的信息为：%s"%studentList[modifNum]) 
  
 elif 4==choose: 
  findName=raw_input("请输入要查找的学生的姓名:") 
  findInfo(findName) 
  
 else : 
  print("您输入的有误,请重新输入") 
  continue

