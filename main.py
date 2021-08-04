cap_price = 3
esp_price = 2.25
lat_price = 2.5
ice_price = 2.5
no_take = 0
no_dine = 0
r_take = ''
r_dine = ''
total = 0
total_G = 0
drinks = 0
dlist = []
qlist = []
cap_quantity = 0
esp_quantity = 0
lat_quantity = 0
ice_quantity = 0

oper = input('operation: ')
if oper == 'New order':
    type = input('Dine in or take away: ')
    if type == 'Take away':
        no_take = no_take + 1
        r_take = 'Take away'
    elif type == 'Dine in':
        no_dine = no_dine + 1
        r_dine = 'Dine in'
    else:
        print('Error') #find way to restart
    while drinks != '':
        drinks = input('Enter drink type: ')
        if drinks == 'Cappuccino':
            cap_quantity = int(input('Enter quantity: '))
            cap_order_price = cap_quantity*cap_price
            qlist.append(cap_quantity)
            dlist.append(drinks)
        elif drinks == 'Espresso':
            esp_quantity = int(input('Enter quantity: '))
            esp_order_price = esp_quantity*esp_price
            qlist.append(esp_quantity)
            dlist.append(drinks)
        elif drinks == 'Latte':
            lat_quantity = int(input('Enter quantity: '))
            lat_order_price = lat_quantity*lat_price
            qlist.append(lat_quantity)
            dlist.append(drinks)
        elif drinks == 'Iced Coffee':
            ice_quantity = int(input('Enter quantity: '))
            ice_order_price = ice_quantity * lat_price
            qlist.append(ice_quantity)
            dlist.append(drinks)
        elif drinks != '':
            print('Error')
        else:
            num = 0
            for seq in range(len(dlist)):
                print(dlist[num] + '        ' + str(qlist[num]))
                num = num + 1
