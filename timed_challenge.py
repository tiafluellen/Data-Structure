# Timed Challenge #7: First Repeated Value
#
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3


def first_repeated_value(values):
    seen = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

    return None


# Test cases
print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))
print(first_repeated_value([1, 2, 3, 4, 5]))
print(first_repeated_value([]))
print(first_repeated_value([7, 7, 2, 3]))
print(first_repeated_value(["apple", "banana", "apple", "orange"]))



"""
Reflection:

For this timed challenge, I chose to use a set because the problem asks me to find the first value that appears more than once. A set is useful because it allows me to quickly check whether a value has already been seen. As I loop through the collection, I check each value against the set. If the value is already there, I return it immediately. If it is not there, I add it to the set and continue. The average runtime is O(n), while the space complexity is O(n) because the set can store each value.

The 30-minute time limit affected my decision because I wanted to choose a solution that was simple, efficient, and easy to explain. Instead of trying to create a more complicated structure, I focused on a data structure I already understand and knew would work well for fast lookups. The set also allowed me to avoid checking every possible pair of values, which would have taken O(n²) time.

One trade-off I made was using additional memory for the set. A solution that uses less extra space might be possible in some situations, but it could take longer to run. Under time pressure, I prioritized a clear and efficient solution that I could test quickly. I also tested normal input, no duplicates, an empty list, an immediate duplicate, and string values to make sure the function handled different situations correctly.
"""