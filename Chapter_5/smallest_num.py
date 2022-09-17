list=[13,512,3,23,56]
smallest_so_far=None
auxlist=[]
for i in list:
    if smallest_so_far is None:
        smallest_so_far=i

    elif i<smallest_so_far:
        smallest_so_far=i


print(smallest_so_far)