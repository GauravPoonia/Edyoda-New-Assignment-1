# Q.9 - nested list

lst = []
n = int(input("Enter no of students : "))
for i in range(n):
    names = input("Enter the names : ")
    scores = float(input("Enter the scores : "))
    lst.append([names,scores])

lst.sort(key=lambda lst:lst[1])

second_lowest = []
for i in range(len(lst)):
    if lst[i][1] != lst[0][1]:
        second_lowest.append(lst[i][0])
        for j in range(i+1,len(lst)):
            if lst[j][1] == lst[i][1]:
                second_lowest.append(lst[j][0])
            else:
                break
        break
    else:
        continue

second_lowest.sort()
for i in second_lowest:
    print(i)