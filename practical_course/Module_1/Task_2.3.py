'''
3. Пусть пользователь придумывает пароль и вводит его с клавиатуры. 
Допустимым считается пароль, который состоит более чем из 8 символов и включает как прописные, так и заглавные буквы. 
Используя цикл while дождитесь, пока пользователь введет допустимый пароль. Длину строки можно считать с помощью функции len0).
'''

while True:
   password = input('Enter your password: ')
   if len(password) <= 8 or not (any(symbol.isupper() for symbol in password) or (any(symbol.islower()) for symbol in password)):
       print('Your password must have more than 8 symbols and include both uppercase and uppercase letters. \nPlease check your password and try again.')
   else:
       print('Your password is valid. Thank you!')
       break
