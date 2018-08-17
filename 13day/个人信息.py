id_card = {"name":"靳彦昆","sex":"男","age":"28","address":"河南新乡","height":"182","weight":"165"}
print(id_card)
print(type(id_card))
#新增
id_card["birthday":"1989.05.07"]
print(id_card)
'''
id_card.setdefault("hobby":188)

id_card.setdefault("xiaobuding":118)
'''
print(id_card)
#查找
print(id_card["name"])
print(id_card.get("name"))
#修改
id_card["name"] = "xiaogao"
print(id_card)
#删除
id_card.pop("name")
print(id_card)
id_card.popitem()
print(id_card)
#清空
id_card.clear()
#




