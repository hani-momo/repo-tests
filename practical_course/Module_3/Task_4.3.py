import json

'''user_data = {'login' : 'passwd'}
with open('user_data.json', 'w') as f:
       json.dump(user_data, f)'''

user_data = {}

def register(login, passwd):
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
        

    if login not in user_data:
        user_data[login] = passwd
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)

            print('You\'ve signed up')
    else:
        print('Login already exists. Try another one')


'''Напишите функцию для входа пользователей в систему. 
Функция должна проверять правильность логина и пароля, 
которые записаны в json файл'''

def login_function(login, passwd):
     with open('user_data.json', 'r') as f:
            user_data = json.load(f)
            if login in user_data and user_data[login] == passwd:
                print('Welcome')
            else:
                print('Check your input data and try again. Or sign up')
	#check login and passwd is correct

while True:
    q1 = input('Log in or Sign up? ')
    if q1.lower() == 'sign up':
        login = input('Login: ')
        passwd = input('Password: ')

        register(login, passwd)
    elif q1.lower() == 'log in':
        login = input('Login: ')
        passwd = input('Password: ')

        login_function(login, passwd)
    else:
        print('Error. Log in or Sign up?')