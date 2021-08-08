# Imports
import sys
import csv
import os

cap_price = 3  # constant price
esp_price = float(2.25)  # constant price
lat_price = float(2.50)  # constant price
ice_price = float(2.50)  # constant price
no_take = 0     # counts the amount of take away orders
no_dine = 0     # counts the amount of dine in orders
r_take = ''
r_dine = ''
oper = ' '
Income = float(0)
TGST = float(0)     # total GST
NoCups = 0          # Number of cups sold
type = 0            # dine in/take away

while oper != '3':              # Operation selection
    oper = input('''operations: 
New order (1) 
Daily Summary (2) 
End (3)
Enter operation number: ''')
    if oper == '1':
        while type == 0:
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
        plist = []  # list of prices corresponding to order
        drinks = 0
        cap_quantity = 0  # quantity of each cap
        esp_quantity = 0  # quantity of each esp
        lat_quantity = 0  # quantity of each lat
        ice_quantity = 0  # quantity of each ice
        Ftotal = 0          # total + GST
        FFtotal = 0         # ftotal + extras (Grand total
        extra = 0
        total = float(0)  # Total price Ex. GST
        total_GST = float(0)  # Total GST of an order
        while drinks != '':
            drinks = input('''
Drinks: 
Cappucino   (1)
Espresso    (2)
Latte       (3)
Iced Coffee (4)
Complete (enter)
Enter drink type: ''')
            if drinks == '1':
                cap_quantity = int(input('Enter quantity: '))
                cop = cap_quantity * cap_price  # cop = cappuccino order price
                plist.append(cop)
                qlist.append(cap_quantity)
                dlist.append('Cappuccino     ')
                drinks = ' '
            elif drinks == '2':
                esp_quantity = int(input('Enter quantity: '))
                eop = esp_quantity * esp_price  # eop = espresso order price
                plist.append(eop)
                qlist.append(esp_quantity)
                dlist.append('Espresso       ')
                drinks = ' '
            elif drinks == '3':
                lat_quantity = int(input('Enter quantity: '))
                lop = lat_quantity * lat_price  # lop = latte order price
                plist.append(lop)
                qlist.append(lat_quantity)
                dlist.append('Latte          ')
                drinks = ' '
            elif drinks == '4':
                ice_quantity = int(input('Enter quantity: '))
                iop = ice_quantity * lat_price  # iop = iced coffee order price
                plist.append(iop)
                qlist.append(ice_quantity)
                dlist.append('Iced Coffee    ')
                drinks = ' '
            elif drinks != '':
                print('Error')

            else:           # Receipt
                print('----------------Order----------------')
                num = 0
                for seq in range(len(dlist)):
                    print(
                        f'{dlist[num]}     x{str(qlist[num])}       ${str(round(plist[num], 2))}')
                    total = total + plist[num]
                    num = num + 1
                total_GST = float(total * 0.1)
                total_GST = round(total_GST, 2)
                Ftotal = total_GST + total
                print(f'Total Ex. GST:               ${str(total)}')
                print(f'Total GST:                   ${str(total_GST)}')
                if type == '2':
                    extra = float(Ftotal * 0.05)
                    extra = round(extra, 2)
                    print(f'Extras:                       ${extra}')
                else:
                    extra = 0
                    print('Extras:                      $0.00')
                FFtotal = float(Ftotal + extra)
                FFtotal = round(FFtotal, 2)
                print(f'Total icl. GST:              ${str(FFtotal)}')
                print(' ')
                tendered = 0
                while tendered < FFtotal:
                    tendered = (input('Amount tendered ($): '))
                    tendered = float(tendered)
                    if tendered < FFtotal:
                        print('More payment required')
                        print(f'Funds remaining: ${FFtotal-tendered}')
                    elif tendered >= FFtotal:
                        change = tendered - (Ftotal + extra)
                        change = round(change, 2)
                    else:
                        print('error')
                print('')
                print('------------Sales Receipt------------')
                num = 0
                for seq in range(len(dlist)):
                    print(
                        f'{dlist[num]}      x{str(qlist[num])}      ${str(round(plist[num], 2))}')
                    num = num + 1
                print(f'Total Ex. GST:               ${str(total)}')
                print(f'Total GST:                   ${str(round(total_GST, 2))}')
                print(f'Extras:                      ${extra}')
                print(f'Total icl. GST:              ${str(FFtotal)}')
                print(' ')
                print(f'Amount tendered:             ${str(tendered)}')
                print(f'Change given:                ${str(change)}')
                print('''
                ''')
                Income = Income + total + extra         # Adding total to total income
                TGST = TGST + total_GST                 # Adding the GST to total income
                for i in range(len(qlist)):             # Counts total quantity of cups
                    NoCups = qlist[i] + NoCups
                type = 0                                # Resets dine-in/takeaway
    elif oper == '2':                                   # Daily summary
        Torders = no_take + no_dine
        TGST = round(TGST, 2)
        print(f'''Number of Dine-In orders:              {no_dine}
Number of Take-Away orders:            {no_take}
Total number of orders:                {Torders}
Total number of cups of coffee:        {NoCups}
Total income:                         ${round(Income, 2)}
Total GST collected:                  ${TGST}
''')
        data = [no_take, no_dine, Torders, NoCups, Income, TGST]            # Used to save as a csv file and open ecxel
        headings = ['Take-Away', 'Dine-In', 'Total Orders', 'Number of Cups', 'Income', 'Total GST']
        with open('Dailyss.csv', 'w', encoding='UTF8', newline='') as Sum:
            writer = csv.writer(Sum)
            writer.writerow(headings)
            writer.writerow(data)
        Sum.close()
        os.system("start EXCEL.EXE Dailyss.csv")

    elif oper == '3':       # end program
        sys.exit()
    else:
        print('error')
