"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    # A set lets us quickly check whether an ID has already appeared.
    # Checking and adding values are O(1) on average, making the overall solution O(n).
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
"""

class TaskQueue:
    def __init__(self):
        # A list keeps tasks in insertion order. Adding is O(1), while
        # removing from the front is O(n) because the remaining items shift.
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None
        return self.tasks.pop(0)


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.
"""

class UniqueTracker:
    def __init__(self):
        # A set automatically stores each value only once. Adding is O(1)
        # on average, and getting the count is O(1).
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)