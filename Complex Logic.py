frstvl = int(input())

if ((frstvl % 2) == 1) and (frstvl < 0 or frstvl>=100):
    print("yes")  
elif ((frstvl % 3) == 0) or (frstvl>=0 and frstvl < 100):
    print("maybe")
else:
    print("no")