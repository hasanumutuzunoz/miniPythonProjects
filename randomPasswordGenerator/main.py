from random import *
import string
from random import *

print("\nWelcome to the random password generator\n")

# Global Variables
userAgree = ""
message = "Your password will be %i characters \nDo you agree? 'YES' 'NO'\n"
passLength = 0


def userMessage():
    globals()["userAgree"] = str(input(globals()["message"] % (globals()["passLength"])))


# Ask password length from the user and confirm (YES, NO)
# YES - end the loop
# NO - stay in the loop and ask again
while userAgree != "YES":
    passLength = int(input("Enter a number for the password length\n"))

    # Max character limit
    if passLength > 1000000:
        print("You password cannot be more than 1,000,000 characters")
        continue

    userMessage()

    # Second loop for OTHER answers to avoid asking password length
    # Keep asking until the answer is YES or NO
    while userAgree != "NO" and userAgree != "YES":
        print("Please enter 'YES' or 'NO'\n")
        userMessage()

# Add upper and lower case letters, digits, symbols in chars array
chars = string.ascii_letters + string.digits + string.punctuation

# Add password string variable random characters
password = ""
for i in range(passLength):
    password += chars[randint(0, len(chars) - 1)]

print("Your password is: ", password)