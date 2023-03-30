menu = {
    'coffe': 15000,
    'tea': 20000,
    'orange juice': 25000,
    'strawwbarry juice': 10000,
}

key = 0
while key != 3:
    print("--------------------")
    print("press 1 to print menu!")
    print("press 2 to order món")
    print("press 3 to quit")
    key = int(input('What do you want : '))
    if key == 1:
        for key, value in menu.items():
            print(f'food: {key} -- value: {value}')
    elif key == 2: 
        so_luong = int(input('Input amount: '))
        cart = []
        for i in range(0, so_luong):
            do_uong = input('Dish you want: ')
            so_luong = int(input(f'input amount {do_uong}: '))
            cart.append(do_uong)
            cart.append(so_luong)
            tong_tien = so_luong*menu[value]
            print(cart)
            print("total price: ", tong_tien)
    elif key == 3:
        print('quit')

