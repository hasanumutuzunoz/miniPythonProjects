# Find the given number in the string

s = "3If I have 95 apples and 3401 carrots, 3how many fruits I have?"
n = str(input("Please enter a number"))

# Easy way
location = s.find(n)
if location > -1:
    print("Your number is in the string, at the %i character" %location)
else:
    print("Your number is not in the string")


# Convert string to list, and search list
listStr = list(s)
for i in range(len(listStr)):
    if listStr[i] == n:
        print("Your number is in the string at the %i character" %i)
        break

