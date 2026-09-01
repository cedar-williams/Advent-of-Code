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

# Get the data
with open("input.txt") as file:
    rows = [line.strip() for line in file]

fresh_ranges: list[tuple[int, int]] = []
ingredients: list[int] = []

# Ingest data

split_index = rows.index("")

fresh_ranges = [split_to_tuple(row) for row in rows[0:split_index]]
ingredients = [int(row) for row in rows[split_index + 1:]]

fresh_ingredient_count = 0
for ingredient in ingredients:
    if check_good(fresh_ranges, ingredient):
        fresh_ingredient_count += 1


print(f'Fresh ingredient ID count: {fresh_ingredient_count}')