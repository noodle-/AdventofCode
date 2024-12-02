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


def is_safe_with_dampener(levels):
    """
    Determine if a report is safe with the Problem Dampener applied.
    A report is safe if:
    - It is already safe.
    - OR removing any single level makes it safe.
    """
    # If the report is already safe, no need for the dampener
    if is_safe_report(levels):
        return True

    # Try removing each level and check if the report becomes safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe_report(modified_levels):
            return True

    # If no single removal makes it safe, the report is unsafe
    return False


# Step 1: Read input from a text file
with open("input.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]

# Step 2: Count the number of safe reports without and with the dampener
safe_reports_count = sum(1 for report in reports if is_safe_report(report))
safe_with_dampener_count = sum(1 for report in reports if is_safe_with_dampener(report))

# Output the results
print("Number of Safe Reports (without Dampener):", safe_reports_count)
print("Number of Safe Reports (with Dampener):", safe_with_dampener_count)
