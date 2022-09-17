#create variables 
hin=0
rin=0
out=0

#Function to calculate payment depending the working hours
def computepay (h,r):
    if h<40:
        res=h*r
    #The extra hours are payd 1.5 times more the normal rate
    elif h>40:
        res=(40*r)+((h-40)*r*1.5)
    return(res)

hrs=input("Enter hours:")
rate=input("Enter rate:")
hin=float(hrs)
rin=float(rate)

out=computepay(hin,rin)

print("pay",out)


