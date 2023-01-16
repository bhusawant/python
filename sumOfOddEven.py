sum=0
choice = int(input("Enter 1 for Odd 2 for Even\n"))
if(choice == 1):
    for i in range(0, 11):
        if(i%2==0):
            print(i, end=" ")
            sum+=i
    print("\nSum of odd number:", sum)


elif(choice == 2):
    for i in range(0, 11):
        if(i%2==1):
            print(i, end=" ")
            sum += i
    print("\nSum of even number:", sum)

else:
    print("Enter a valid choice\n")
