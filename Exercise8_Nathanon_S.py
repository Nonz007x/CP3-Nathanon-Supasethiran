fries = 15
burger = 25
soda  = 10

while True:
    usernameInput = input('Username :')
    passwordInput = input('Password :')
    if usernameInput == 'admin' and passwordInput == '1111':
        print('-----Fast Food Store-----')
        print('1. Fries           ', fries, '฿')
        print('2. Hamburger       ', burger, '฿')
        print('3. Soda            ', soda, '฿')
        break
    else:
        print("\nTry Again")

userSelected = int(input('Your Order :'))
if userSelected == 1:
        amount = int(input('Amount :'))
        price = fries*amount
elif userSelected == 2:
        amount = int(input('Amount :'))
        price = burger*amount
elif userSelected == 3:
        amount = int(input('Amount :'))
        price = soda*amount
else:
    print('Try Again')

print('Total =', price, '฿' )








