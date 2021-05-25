# Creating lists
first_list=[]
second_list=[]

for i in range(10):
    if i%2 != 0 :
        # first list should contain odd values 
        first_list.append(i)
    else:
        # so the second list contains even values
        second_list.append(i)
        
# merging lists
merged_list=first_list+ second_list

# multiplying all the values with 2 in merged_list
merged_list = [element * 2 for element in merged_list]

# printing all values with their types in merged_list
for element in merged_list:
    print("{}'s type is {}".format(element,type(element)))
