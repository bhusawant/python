# input_string = input('Enter elements separated by space: ')

# user_list = input_string.split()

# # print list
# print('list: ', user_list)

# list2 = []
# list3 = []
# for i in user_list:
#     if(i == 0):
#         list2.append(i)


"""
test_list = [5, 6, 10, 4, 7, 1, 19] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# Odd elements indices
# using loop 
res1 = [] 
res2 = [] 
for idx, ele in enumerate(test_list): 
    if ele % 2 != 0: 
        res1.append(idx) 
    if ele % 2 == 0: 
        res2.append(idx) 
          
# printing result 
print("Indices list Odd elements is : " + str(res1)) 
print("Indices list even elements is : " + str(res2)) 
"""


"""
# Q.1
list1 = []
# Input number of elemetns
n = int(input("List elements: "))

list1 = list(map(int, input("Numbers : ").strip().split()))[:n]
sum1 =0
sum2 =0

for i in list1:
    if(i%2==0):
        # print(i)
        sum1+=i
    if(i%2!=0):
        # print(i)
        sum2+=i

tuple1 = (sum1, sum2)
# print(list1)
print(tuple1)
"""





"""
input_string = input('Enter elements separated by space: ')

user_list = input_string.split()

# print list
print('list: ', user_list)
# L = [1, 2, 3, 4, 5, 6, 7]
li1 = []
li2 = []
sum=0
# sum2=0
count = 0
for i in user_list:
    if count % 2 == 1:
        li1.append(i)
        # sum+=i
    if count % 2 != 1:
        li2.append(i)
        # sum2+=i
    count += 1

print(user_list)
print(tuple(li1))
print(tuple(li2))
# print(sum)
# print(sum2)
"""



"""
# Q.2
l = ['x', 'y', 'z']
list1 = [i*j for i in l for j in range(1, 4)]
print(list1)
list2 = [i*j for i in range(1, 4) for j in l]
print(list2)
"""


"""
# Q.3
t = (4, 5, 6, 2, 3, 4, 5, 1, 2, 6, 4)
d={}
for i in t:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
"""








# Q.4
dict1 = {1:"www.yahoo.com", 2:"www.tsec.edu", 3:"www.asp.net", 4:"www.abcd.in"}
tuple1 = tuple(url.split(".")[-1] for url in dict1.values())
print(tuple1)


