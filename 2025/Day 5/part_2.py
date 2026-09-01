# --- Day 5: Cafeteria ---


# Check if ingredient is good
def check_good(fresh_id_ranges: list[tuple[int, int]], ingredient_id: int):
    for fresh_id_range in fresh_id_ranges:
        if fresh_id_range[0] <= ingredient_id <= fresh_id_range[1]:
            return True
    return False

def split_to_tuple(row_str: str) -> tuple[int, int]:
    """
    Split two numbers separated by a dash into a tuple
    :param row_str: two numbers separated by a dash, ex "3-5"
    :return: a tuple of the left and right number (low, high)
    """
    low, high = tuple(map(int, row_str.split("-")))
    return low, high

def tuple_overlap(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """
    Determine if two range tuples overlap
    :return: true if overlap, false if not
    """
    # No overlap
    if a[1] < b[0] or b[1] < a[0]:
        return False
    return True

def collapse_tuple(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """
    Combines two overlapping tuples into a single tuple
    :param a: tuple a
    :param b: tuple b
    :return: a tuple of the combined sizes
    """
    low_val = a[0] if a[0] < b[0] else b[0]
    high_val = a[1] if a[1] > b[1] else b[1]

    return low_val, high_val

def total_ids_in_range(a: tuple[int, int]) -> int:
    """
    Determine the total number of valid ID's in a range
    :param a: the tuple range
    :return: total values in the range that are valid
    """
    return a[1] - a[0] + 1


# Get the data
with open("input.txt") as file:
    rows = [line.strip() for line in file]

fresh_ranges: list[tuple[int, int]] = []
ingredients: list[int] = []

# Ingest data
split_index = rows.index("")
fresh_ranges = [split_to_tuple(row) for row in rows[0:split_index]]

# Loop over all tuples repeatedly until a full repeat done without a collapse
new_collapse_found = True
while new_collapse_found and len(fresh_ranges) > 1:
    new_collapse_found = False
    print('While loop start')

    for x, range_a in enumerate(fresh_ranges[:-1]):
        for range_b in fresh_ranges[x + 1:]:
            print(f'range_a:{range_a}, range_b:{range_b}')
            if tuple_overlap(range_a, range_b):
                print('overlap')
                new_collapse_found = True
                new_tuple = collapse_tuple(range_a, range_b)
                fresh_ranges.remove(range_a)
                fresh_ranges.remove(range_b)
                fresh_ranges.append(new_tuple)
                print(f'Made new tuple: {new_tuple}')
                break

        if new_collapse_found:
            break

print(f'Final tuples:')
for a in fresh_ranges:
    print(a)

# Sum total number of ID's in each range and to the fresh count
all_fresh_count = 0
for single_range in fresh_ranges:
    print(total_ids_in_range(single_range))
    all_fresh_count += total_ids_in_range(single_range)

print(f'All possible fresh ingredients count: {all_fresh_count}')