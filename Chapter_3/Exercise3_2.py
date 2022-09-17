# declaramos variables iniciales
h=0
r=0
pay=0

#Input de numero de horas y precio por hora
hrs=input("Enter hours:")
rate=input("Enter rate:")

try:
    h=int(hrs)
    r=int(rate)
except:
    print("Error, please enter only numbers")
    quit()

print(h,r)

#evaluamos si las horas son mayores a 40 
if h>40:
    pay=(40*r)+((h-40)*r*1.5)
else:
    pay=h*r

print(pay)