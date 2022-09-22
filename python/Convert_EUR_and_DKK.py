print('Hello and welcome to Gold Bank')
print('Do you want to convert EUR to DKK, or DKK to EUR?  (yes og no)')

response=input()

if response == 'yes':
    print('Nice, is it EUR to DKK, or DKK to EUR')
    print('For EUR to DKK press 1')
    print('For DKK to EUR press 2')

    EURtoDKK = input()

    if EURtoDKK == '1':
        print('Good choice. Note that at Gold bank we have 2% commition and you have to convert at least 25 eur')
        print('The exchange rate for EUR to DKK is 7,44')
        print('How many EUR would you like to convert')
        EUR=input()
        EUR=float(EUR)
        if EUR >= 25:
            print('You will revice ' + str(EUR*7.44*0.98) + ' DKK at Gold Bank')
        if EUR < 25:
            print('This is not enough')
    
    if EURtoDKK == '2':
        print('Good choice. Note that at Gold bank we have 2% commition and you have to convert at least 186 DKK')
        print('The exchange rate for DKK to EUR is 0,13')
        print('How many DKK would you like to convert')
        DKK=input()
        DKK=float(DKK)
        if DKK >= 186:
            print('You will revice ' + str(DKK*0.13*0.98) + ' EUR at Gold Bank')
        if DKK < 186:
            print('This is not enough')
    


if response != 'yes':
    print('Sorry, this program cant help you')
