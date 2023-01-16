a=int(input("Enter your age\n"))
if(a>=18):
    print("You can vote!\n")
elif(a>=12 and a<18):
    if(a>=12 and a<17):
        print("You are teenager.You can vote at 18!\n")
    else:
        print("Your age is 17. So, you cannot vote now\nYou can vote next year\n")
else:
    print("You cannot vote!\n")