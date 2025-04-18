# Dynamic List Processing - All code in one file

# 1. Prompt for number of items and build a list
num_items = int(input("Enter the number of items in the list: "))
my_list = []
for i in range(num_items):
    value = int(input(f"Enter integer {i+1}: "))
    my_list.append(value)
print("Initial list:", my_list)

# 2. Insert 99 at position 1
my_list.insert(1, 99)
print("After inserting 99 at position 1:", my_list)

# 3. Replace 99 with 100
if 99 in my_list:
    index_99 = my_list.index(99)
    my_list[index_99] = 100
print("After replacing 99 with 100:", my_list)

# 4. Create second list and extend the first list
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
my_list.extend(second_list)
print("First list after extending:", my_list)

# 5. Remove 800 from the first list
if 800 in my_list:
    my_list.remove(800)
print("After removing 800:", my_list)

# 6. Remove the third item (index 2)
if len(my_list) > 2:
    del my_list[2]
print("After removing third item:", my_list)

# 7. List of grades
grades = ["A", "B", "C", "A", "A", "C"]

# 8. Count number of A grades
count_A = grades.count("A")
print("Number of A grades:", count_A)

# 9. Index of first B grade
if "B" in grades:
    index_B = grades.index("B")
    print("Index of first B grade:", index_B)

# 10. Check for F grade
if "F" in grades:
    print("F is in the list.")
else:
    print("F is not in the list.")

# 11. Clear the second list
second_list.clear()
print("Second list after clearing:", second_list)

# 12. Delete the second list and try to display it
del second_list
try:
    print(second_list)
except NameError:
    print("second_list no longer exists (deleted).")

# 13. Create list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14. Sort the players list
players.sort()
print("Sorted players list:", players)

# 15. Make a copy of players to players2
players2 = players.copy()
print("players2 (copy):", players2)

# 16. Reverse players2 and show both lists
players2.reverse()
print("Original players list:", players)
print("Reversed players2 list:", players2)
