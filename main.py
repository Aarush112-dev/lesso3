list = [56,43,83,62,75,24,64,26,44,37]
list2 = ["aa","cb","gd","gc","f","zl","l","n","m"]

for i in range(len(list2)):
    key = list2[i]
    j = i-1
    while key < list2[j] and j >= 0:
        list2[j+1] = list2[j]
        j-=1
        print(list2)
    list2[j+1] = key
