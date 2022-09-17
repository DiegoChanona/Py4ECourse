largest = None
smallest = None
lista=[]

while True:
    
    num = input("Enter a number: ")
    if num == "done":
        break
    #We look only for numerical input
    try:
        fval=int(num)
    except:
        print('Enter only numbers')
        continue
   
   #we add the value to a list
    lista.append(fval)

    #print(num)

for i in lista:
    if smallest is None:
        smallest=i
    elif i<smallest:
        smallest=i
    
    elif largest is None:
        largest=i
    elif i>largest:
        largest=i



print("Maximum", largest)
print("Minimum", smallest)