# Q.2 - To split and join a string

def split_and_join(string):
    return "-".join(string.split(" "))

string = input("Enter a string : ")
data = split_and_join(string)
print(data)
