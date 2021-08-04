import sys
cap_price = 3  # constant price
esp_price = float(2.25)  # constant price
lat_price = float(2.50)  # constant price
ice_price = float(2.50)  # constant price
no_take = 0
no_dine = 0
r_take = ''
r_dine = ''
oper = ' '
Income = float(0)
TGST = float(0)
NoCups = 0

while oper != '3':
    oper = input('''
operations: 
New order (1) 
Daily Summary (2) 
End (3)
Enter operation number: ''')
    if oper == '1':
        while type = 0:
            type = input('''
Dining Options: 
Dine-in (1) 
Take-away (2) 
Enter dining option: ''')
            if type == '2':
                no_take = no_take + 1
                r_take = 'Take away'
            elif type == '1':
                no_dine = no_dine + 1
                r_dine = 'Dine in'
            else:
                print('Error')
                type = 0
        dlist = []  # list of drinks for (1)
        qlist = []  # list of drink quantities for (1)
        plist = []
        drinks = 0
        cap_quantity = 0  # quantity of each cap
        esp_quantity = 0  # quantity of each esp
        lat_quantity = 0  # quantity of each lat
        ice_quantity = 0  # quantity of each ice
        Ftotal = 0
        FFtotal = 0
        extra = 0
        total = float(0)  # Total price Ex. GST
        total_GST = float(0)  # Total GST
        while drinks != '':
            drinks = input('''
Drinks: 
Cappucino   (1)
Espresso    (2)
Latte       (3)
Iced Coffee (4)
Enter drink type:''')
            if drinks == '1':
                cap_quantity = int(input('Enter quantity: '))
                cop = cap_quantity * cap_price  # cop = cappuccino order price
                plist.append(cop)
                qlist.append(cap_quantity)
                dlist.append('Cappuccino')
                drinks = ' '
            elif drinks == '2':
                esp_quantity = int(input('Enter quantity: '))
                eop = esp_quantity * esp_price  # eop = espresso order price
                plist.append(eop)
                qlist.append(esp_quantity)
                dlist.append('Espresso')
                drinks = ' '
            elif drinks == '3':
                lat_quantity = int(input('Enter quantity: '))
                lop = lat_quantity * lat_price  # lop = latte order price
                plist.append(lop)
                qlist.append(lat_quantity)
                dlist.append('Latte')
                drinks = ' '
            elif drinks == '4':
                ice_quantity = int(input('Enter quantity: '))
                iop = ice_quantity * lat_price  # iop = iced coffee order price
                plist.append(iop)
                qlist.append(ice_quantity)
                dlist.append('Iced Coffee')
                drinks = ' '
            elif drinks != '':
                print('Error')

            else:
                print('------------Order------------')
                num = 0
                for seq in range(len(dlist)):
                    print(
                        f'{dlist[num]}        x{str(qlist[num])}      ${str(round(plist[num], 2))}')  # print price (total for sum of drink quantity)
                    total = total + plist[num]
                    num = num + 1
                total_GST = float(total * 0.1)
                total_GST = round(total_GST, 2)
                Ftotal = total_GST + total
                print(f'Total Ex. GST:   ${str(total)}')
                print(f'Total GST:   ${str(total_GST)}')
                if type == '2':
                    extra = float(Ftotal * 0.05)
                    extra = round(extra, 2)
                    print(f'Extras:  ${extra}')
                else:
                    extra = 0
                    print('Extras: $0.00')
                FFtotal = float(Ftotal + extra)
                FFtotal = round(FFtotal, 2)
                print(f'Total icl. GST:  ${str(FFtotal)}')  ##make receipt look nicer
                print(' ')                                  ##change drinks to numbers
                tendered = int(input('Amount tendered ($): '))  ##Daily summary
                change = tendered - (Ftotal+extra)
                change = round(change, 2)
                round(change, 2)
                print('')
                print('------------Sales Receipt------------')
                num = 0
                for seq in range(len(dlist)):
                    print(
                        f'{dlist[num]}        x{str(qlist[num])}      ${str(round(plist[num], 2))}')
                    num = num + 1
                print(f'Total Ex. GST:   ${str(total)}')
                print(f'Total GST:   ${str(round(total_GST, 2))}')
                print(f'Extras:  ${extra}')
                print(f'Total icl. GST:  ${str(FFtotal)}')
                print(' ')
                print(f'Amount tendered: ${str(tendered)}')
                print(f'Change given: ${str(change)}')
                print('''
                ''')
                Income = Income + total + extra
                TGST = TGST + total_GST
                for i in range(len(qlist)):
                    NoCups = qlist[i] + NoCups
    elif oper == 3:
        sys.exit()
    elif oper == 2:
        Torders = no_take + no_dine
        print(f'''Number of Dine-In orders: {no_dine}
Number of Take-Away orders: {no_take}
Total number of orders: {Torders}
Total number of cups of coffee: {NoCups}
Total income:  ${Income}
Total GST collected:  ${TGST}
''')

        data = [no_take, no_dine, Torders, NoCups, Income, TGST]
        headings = ['Take-Away', 'Dine-In', 'Total Orders', 'Number of Cups', 'Income', 'Total GST']

        import csv

        with open ('DailySummary.csv', 'w', encoding='UTF8', newline='') as Sum:
            writer = csv.writer(Sum)
            writer.writerow(headings)
            writer.writerow(data)
    else:
        print('error')
