print('Welcome valued customer!')
print('Thank you for stopping by')
print('Please use the codes in front of each drinks to select and pay for the kind of drink you want')
print('----------------------------------------------------------------------------------------------')
print('Coke  (d1) price = $1.25')
print('Pepsi (d2) price = $1.25')
print('Fanta (d3) price = $1.25')
print('Sprite(d4) price = $1.25')
print('Water (d5) price = $1.00')

coke = 'd1'
pepsi = 'd2'
fanta = 'd3'
sprite = 'd4'
water = 'd5'

select_choice = (input('Enter the code of your desired drink: '))

if select_choice == coke:
    print('Amount due for this product is $1.25')
    amount_paid = float(input('please pay here: '))
    if amount_paid < 1.25:
        print('-----------------ERROR---------------')
        print('Amount not enough for product')
        print('Please make sure amount is "$1.25" or more')
        print('Start purchase of drink again')
    else:
        if amount_paid >= 1.25:
            if amount_paid % .25 == 0:
                change = amount_paid - 1.25
                print('Please take your product "COKE" ')
                print('And your change due:', change)
            else:
                if amount_paid % .25 != 0:
                    print('------------------ERROR---------------------')
                    print('This machine accepts only quarters or dollar bills')
                    print('Start purchase of drink again')
                    
else:
    if select_choice == pepsi:
        print('Amount due for this product is $1.25')
        amount_paid = float(input('please pay here: '))
        if amount_paid < 1.25:
            print('-----------------ERROR---------------')
            print('Amount not enough for product')
            print('Please make sure amount is "$1.25" or more')
            print('Start purchase of drink again')
        else:
            if amount_paid >= 1.25:
                if amount_paid % .25 == 0:
                    change = amount_paid - 1.25
                    print('Please take your product "PEPSI" ')
                    print('And your change due:', change)
                else:
                    if amount_paid % .25 != 0:
                        print('------------------ERROR---------------------')
                        print('This machine accepts only quarters or dollar bills')
                        print('Start purchase of drink again')
    else:
        if select_choice == fanta:
            print('Amount due for this product is $1.25')
            amount_paid = float(input('please pay here: '))
            if amount_paid < 1.25:
                print('-----------------ERROR---------------')
                print('Amount not enough for product')
                print('Please make sure amount is "$1.25" or more')
                print('Start purchase of drink again')
            else:
                if amount_paid >= 1.25:
                    if amount_paid % .25 == 0:
                        change = amount_paid - 1.25
                        print('Please take your product "FANTA" ')
                        print('And your change due:', change)
                    else:
                        if amount_paid % .25 != 0:
                            print('------------------ERROR---------------------')
                            print('This machine accepts only quarters or dollar bills')
                            print('Start purchase of drink again')
            
        else:
            if select_choice == sprite:
                print('Amount due for this product is $1.25')
                amount_paid = float(input('please pay here: '))
                if amount_paid < 1.25:
                    print('-----------------ERROR---------------')
                    print('Amount not enough for product')
                    print('Please make sure amount is "$1.25" or more')
                    print('Start purchase of drink again')
                else:
                    if amount_paid >= 1.25:
                        if amount_paid % .25 == 0:
                            change = amount_paid - 1.25
                            print('Please take your product "SPRITE" ')
                            print('And your change due:', change)
                        else:
                            if amount_paid % .25 != 0:
                                print('------------------ERROR---------------------')
                                print('This machine accepts only quarters or dollar bills')
                                print('Start purchase of drink again')

            else:
                if select_choice == water:
                    print('Amount due for this product is $1.00')
                    amount_paid = float(input('please pay here: '))
                    if amount_paid < 1.00:
                            print('-----------------ERROR---------------')
                            print('Amount not enough for product')
                            print('Please make sure amount is "$1.00" or more')
                            print('Start purchase of drink again')
                    else:
                        if amount_paid >= 1.00:
                            if amount_paid % .25 == 0:
                                change = amount_paid - 1.00
                                print('Please take your product "WATER" ')
                                print('And your change due:', change)
                            else:
                                if amount_paid % .25 != 0:
                                    print('------------------ERROR---------------------')
                                    print('This machine accepts only quarters or dollar bills')
                                    print('Start purchase of drink again')
