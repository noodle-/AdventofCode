from collections import Counter

# Step 1: Read input from a text file
with open("input.txt", "r") as file:
    left_list = []
    right_list = []
    for line in file:
        # Split each line into two numbers and append them to respective lists
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

# --- Part 1: Calculate Total Distance ---
# Sort both lists in ascending order
left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

# Calculate the total distance by pairing and summing the differences
total_distance = sum(abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted))

# --- Part 2: Calculate Similarity Score ---
# Count occurrences of each number in the right list
right_counts = Counter(right_list)

# Calculate the similarity score
similarity_score = sum(num * right_counts[num] for num in left_list)

# Output the results
print("Total Distance:", total_distance)
print("Similarity Score:", similarity_score)
