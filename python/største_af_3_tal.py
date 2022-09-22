print('What three numbers would you like to know which is the biggest?')
print('Write a number, them enter. then write new number, and enter. Finaly write last number and enter')

no1=input()
no2=input()
no3=input()

if no1>no2 and no1>no3 :
    print('The biggest number is ' + no1)

if no2>no1 and no2>no3 :
    print('The biggest number is ' + no2)

if no3>no1 and no3>no1 :
    print('The biggest number is ' + no3)
