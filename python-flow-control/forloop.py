# for loop and nested for loop
# for loop is used for iterating through a sequence
l1 = []
l2 = []
user_input = [x for x in range(1,11)]
for i in user_input:
    if i%2 ==0:
        l1.append(i)
    else:
        l2.append(i)

print("Even numbers",l1)
print("Odd numbers",l2)
