y = int(input("Enter your year "))

if y % 4 == 0 and y % 100 != 0:
    print(y, "is a leap year")

else:
    print(y, "is not a leap year")

# if y%4 == 0 and y%100 != 0:
#     print(y, "is a leap year")
#
# if y%4 != 0 and y%100 == 0:
#     print(y, "is not a leap year")

