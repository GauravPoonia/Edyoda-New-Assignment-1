# Q.4 - score of runner up




n = int(input("Enter number of students : "))
score_list = []
for i in range(n):
    ele = float(input("Enter the scores : "))
    score_list.append(ele)
arr = sorted(score_list)
print(arr)
print(arr[n-2])