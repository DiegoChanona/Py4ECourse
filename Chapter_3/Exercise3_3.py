score = input("Enter Score: ")

scr=float(score)


if scr<0:
    print("Value not in range(0-1)")
    quit()

elif scr <0.6:
    print("F")
    
elif scr <0.7:
    print("D")
    
elif scr<0.8:
    print("C")

elif scr<0.9:
    print("B")
    
elif scr >=0.9:
    print("A")
    
elif scr>1:
    print("Value not in range(0-1)")
    quit()
  