import json

def register(login, passwd):
	user_data = {login : passwd}
	with open('users_data.json', 'w') as f:
		json.dump(user_data, f)
		# print(user_data)

login = input('Login: ')
passwd = input('Password: ')
register(login, passwd)