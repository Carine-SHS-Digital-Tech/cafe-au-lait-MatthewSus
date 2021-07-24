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

oper = input('operation: ')
if oper == 'New order':
    type = input('Dine in or take away: ')
    if type == 'Take away':
        no_take = no_take + 1
        r_take = "Take away"
    elif type == 'Dine in':
        no_dine = no_dine + 1
        r_dine = 'Dine in'
    else:
        print('Error') #find way to restart
