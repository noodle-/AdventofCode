# Step 1: Read input from a text file
with open("input.txt", "r") as file:
    left_list = []
    right_list = []
    for line in file:
        # Split each line into two numbers and append them to respective lists
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

# Step 2: Sort both lists in ascending order
left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

# Step 3: Calculate the total distance by pairing and summing the differences
total_distance = sum(abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted))

# Output the result
print("Total Distance:", total_distance)
