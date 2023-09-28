year = int(input("Which year do you want to check? "))

#Write your code below this line

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is not a leap year.")
    else:
        print(str(year) + " is  a leap year.")
else:
    print(str(year) + " is not a leap year.")            