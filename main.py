cap_price = 3       #constant price
esp_price = float(2.25)    #constant price
lat_price = float(2.50)     #constant price
ice_price = float(2.50)     #constant price
no_take = 0
no_dine = 0
r_take = ''
r_dine = ''
total = float(0)           #Total price Ex. GST
total_G = float(0)         #Total GST
drinks = 0
dlist = []          #list of drinks for (1)
qlist = []          #list of drink quantities for (1)
plist = []
cap_quantity = 0    #quantity of each cap
esp_quantity = 0    #quantity of each esp
lat_quantity = 0    #quantity of each lat
ice_quantity = 0    #quantity of each ice
oper = ' '

while oper != '3':
    oper = input('''operations: 
New order (1) 
Daily Summary (2) 
End (3) 
   
Enter operation number: ''')
    if oper == '1':
        type = input('''Dining Options: 
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
        while drinks != '':
            drinks = input('Enter drink type: ')
            if drinks == 'Cappuccino':
                cap_quantity = int(input('Enter quantity: '))
                cop = cap_quantity*cap_price        #cop = cappuccino order price
                plist.append(cop)
                qlist.append(cap_quantity)
                dlist.append(drinks)
                drinks = ' '
            elif drinks == 'Espresso':
                esp_quantity = int(input('Enter quantity: '))
                eop = esp_quantity*esp_price        #eop = espresso order price
                plist.append(eop)
                qlist.append(esp_quantity)
                dlist.append(drinks)
                drinks = ' '
            elif drinks == 'Latte':
                lat_quantity = int(input('Enter quantity: '))
                lop = lat_quantity*lat_price        #lop = latte order price
                plist.append(lop)
                qlist.append(lat_quantity)
                dlist.append(drinks)
                drinks = ' '
            elif drinks == 'Iced Coffee':
                ice_quantity = int(input('Enter quantity: '))
                iop = ice_quantity*lat_price      #iop = iced coffee order price
                plist.append(iop)
                qlist.append(ice_quantity)
                dlist.append(drinks)
                drinks = ' '
            elif drinks != '':
                print('Error')
            else:
                num = 0
                print('Order:')
                for seq in range(len(dlist)):
                    print(dlist[num] + '   ' + 'x' + str(qlist[num]) + '    ' + '$' + str(round(plist[num], 2)))  #print price (total for sum of drink quantity)
                    total = total + plist[num]
                    num = num + 1
                print('Total Ex. GST:   $' + str(total))
                total_G = total*0.1
                print('Total GST:   $' + str(round(total_G, 2)))
                print('Total icl. GST:  $' + str(round(total_G+total, 2)))              ##make receipt look nicer


