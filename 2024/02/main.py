def is_safe_report(levels):
    """
    Determine if a report is safe.
    A report is safe if:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check if all differences are positive (increasing) or all negative (decreasing)
    all_increasing = all(0 < diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff < 0 for diff in differences)

    # A report is safe if it satisfies one of the above conditions
    return all_increasing or all_decreasing


# Step 1: Read input from a text file
with open("input.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]

# Step 2: Count the number of safe reports
safe_reports_count = sum(1 for report in reports if is_safe_report(report))

# Output the result
print("Number of Safe Reports:", safe_reports_count)
