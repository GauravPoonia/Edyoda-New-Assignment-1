# Q.3 - Use of intersection :- 

english = int(input("Enter the no of students who read english newspaper : "))
e_roll_no_list = []
for i in range(english):
    e_roll_no = int(input("Enter the roll no : "))
    e_roll_no_list.append(e_roll_no)
e_roll_no_set = set(e_roll_no_list)
# print(e_roll_no_set)

french = int(input("Enter the no of students who read french newspaper : "))
f_roll_no_list = []
for i in range(french):
    f_roll_no = int(input("Enter the roll no : "))
    f_roll_no_list.append(f_roll_no)
f_roll_no_set = set(f_roll_no_list)
# print(f_roll_no_set)

intersection_of_two = e_roll_no_set.intersection(f_roll_no_set)
print(len(intersection_of_two))