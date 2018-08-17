def register(account,pwd):
	result = isPhone(account)
	if result:
		print("好好好")
def login(account,pwd):
	result = isPhone(account)
	if result:
		print("会很好")
def isPhone(account):
	if len(account) == 11 and account.startswith("1"):
		return True
	else:
		return False


























