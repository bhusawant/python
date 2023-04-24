# Q.1) Create two lists numbers and multiplier. Scan through multiplier list, take each of the 'value' and multiply the number from numbers list at the position equals to index of 'value' by it. If multiplier list exhausts before numbers, handle the exception with following message: "Program halted since multiplier list exhausted". If either of the list name is referred incorrectly, print the message "Sorry, this list does not exist". At the end print the message "Multiplication of two lists is done."

"""
# initialize the lists
numbers = [2, 5, 8, 10, 3]
multiplier = [3, 1, 0, 2]

try:
    # iterate through the multiplier list
    for index in range(len(multiplier)):
        # get the value from the multiplier list
        value = multiplier[index]
        # multiply the value with the number at the same index in the numbers list
        result = numbers[index] * value
        print(result)

    # handle the case where multiplier list is exhausted before numbers
    if index < len(numbers) - 1:
        print("Program halted since multiplier list exhausted")

except NameError:
    # handle the case where the list name is referred incorrectly
    print("Sorry, this list does not exist")

# print the final message
print("Multiplication of two lists is done.")
"""


#Q.2) Write a program to add two values 'a' and 'b'. An integer value is assigned to 'a'. However, while defining 'b', by mistake it was enclosed in quotes by programmer. Handle the exception so that 'b' can be added with integer value 'a'. (Note: b can be integer or float enclosed in quotes. Display appropriate messages. Use nested exception handling.)


a = 10 # integer value assigned to 'a'
b = "'20'" # by mistake, '20' is enclosed in quotes and assigned to 'b'

try:
    # try to convert 'b' to an integer or float
    b = int(b.strip("'"))
except ValueError:
    try:
        b = float(b.strip("'"))
    except ValueError:
        print("Sorry, the value assigned to 'b' is not a valid integer or float.")

try:
    # try to add 'a' and 'b'
    result = a + b
    print(f"The sum of {a} and {b} is {result}.")
except TypeError:
    print("Sorry, the value assigned to 'b' cannot be added to an integer.")

# print the final message
print("Program finished.")





