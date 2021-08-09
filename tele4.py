import random
num = input('login ')
mun = input('pas')
pas = ''
passSumbols = ''
length = input('длина пароля?'+ "\n")
length = int(length)
for x in range(length): #Количество символов (length)
    passSumbols = '1234567890abcdefghijklmnopqrstuvwxyz' #Символы, из которых будет составлен пароль
print('Hello, ', num, 'your password is: ', mun)
print('passSumbols, ',pas, 'your passSumbols is: ', mun)
passSumbols = (mun)

