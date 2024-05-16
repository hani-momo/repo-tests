import json

'''user_data = {'login' : 'passwd'}
with open('user_data.json', 'w') as f:
       json.dump(user_data, f)''' #открыть один раз

def register(login, passwd):
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
         

    if login not in user_data:
        user_data[login] = passwd
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)
    else:
        print('Login already exists. Try another one')


login = input('Login: ')
passwd = input('Password: ')
register(login, passwd)
