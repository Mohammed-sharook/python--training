'''
1.break statement will ends the loop before the loops end or it
looped through all items

2.continue statement will stops the loop for current iteration
and continue with next iteration.

3. pass statement is like placeholder
'''
# continue statement

list_of_items = [1, 2, "4", 5, "23", "sha"]
for i in list_of_items:
    if type(i) == str:
        continue
    print(i,end=" ")

# break statement
list_of_name = ["sharook","ayden","vijay"]
for i in list_of_name:
    if i == "ayden":
        break
    print(i)

