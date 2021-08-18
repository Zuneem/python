print ('lets calculate compound interest')

p = float( input( "enter the principle amount: "))
r = float (input("enter the interest rate: "))
t = float (input ("enter time in years: "))

compoundinterest = p * (pow((1 + r / 100), t)) 


print  (compoundinterest)

