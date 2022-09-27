import datetime

print("Enter your year of birth: " )
yearOfBirth = int(input())
today = datetime.date.today()
currYear = today.year
currAge = currYear - yearOfBirth
print("Your age is {}".format(currAge))
