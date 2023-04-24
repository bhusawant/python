#Q.1) WAP to accept first name and last name and print them in reverse with space between last nam and first name

# first_name=input("Enter first name: ")
# last_name=input("Enter last name: ")
# print(last_name+" "+first_name)


# Q.2) Divisbility by 7 and 5

for num in range(2000, 3201):
    if(num%7==0 and num%5!=0):
        print(num, end="-")

