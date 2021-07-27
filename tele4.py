import random
num = input('login ')
pas = ''
for x in range(4): #Количество символов (4)
    pas = pas + random.choice(list('1234567890')) #Символы, из которых будет составлен пароль
print('Hello, ', num, 'your password is: ', pas)

