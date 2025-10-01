# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent_optimized(numbers):
    # Handle empty list case
    if not numbers:
        return None

    counts = {}
    most_freq_element = numbers[0]  # Initialize with the first element
    max_count = 0

    # Single pass to count frequencies AND track the maximum count
    for num in numbers:
        # Update the frequency count (O(1) average)
        counts[num] = counts.get(num, 0) + 1
        current_count = counts[num]
        
        # Check if the current element is now the most frequent
        # We use '>=' to handle ties and keep the element seen latest if a tie occurs.
        if current_count > max_count:
            max_count = current_count
            most_freq_element = num
            
    # Comment explaining the optimization:
    # Optimization: Reduced the solution from a two-pass approach (O(N) + O(K)) to a single-pass approach (O(N)).
    # We now track the 'max_count' and 'most_freq_element' *while* building the 'counts' dictionary.
    # Performance Comparison:
    # - Original: O(N) to build map + O(K) to find max (where K <= N unique elements). Total O(N).
    # - Optimized: O(N) to build map and find max simultaneously. Total O(N).
    # Space Usage Comparison: Both are O(K) space complexity.
    # The time complexity remains O(N), but the constant factor is slightly better as we avoid iterating over the 'counts' map entirely.

    return most_freq_element

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) (One pass to count, one pass to find max)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(k) or O(n) (To store the counts dictionary, where k is unique elements)
- Why this approach? Uses a hash map for O(1) average time lookups/updates, leading to an optimal O(n) solution.
- Could it be optimized? Time complexity is already optimal at O(n) because all elements must be examined.
"""
# Example:
print("P1 Output:", most_frequent_optimized([1, 3, 2, 3, 4, 1, 3])) # Output: 3

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):

    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) (To store the 'seen' set and the 'result' list)
- Why this approach? Using a set for lookups allows checking if an element has been seen in average O(1) time, ensuring an overall O(n) time complexity while iterating to preserve order.
- Could it be optimized? Time complexity is already optimal at O(n).
"""
# Example:
print("P2 Output:", remove_duplicates([4, 5, 4, 6, 5, 7])) # Output: [4, 5, 6, 7]

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):

    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            # Found a pair. Store it as a sorted tuple to ensure uniqueness.
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        
        seen.add(num)

    return list(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) (To store 'seen' elements and 'pairs')
- Why this approach? Hash sets allow for O(1) average time lookups for the complement, resulting in a single-pass O(n) solution.
- Could it be optimized? The O(n) time complexity is the best possible.
"""
# Example:
print("P3 Output:", find_pairs([1, 2, 3, 4], target=5)) # Output: [(1, 4), (2, 3)]

# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n, initial_capacity=2):

    current_items = []
    capacity = initial_capacity
    
    print(f"\n--- Simulating List Resizing for {n} items ---")
    print(f"Initial Capacity: {capacity}")

    for i in range(n):
        new_item = i + 1

        # Check for resize condition
        if len(current_items) == capacity:
            print(f"--> RESIZING: Capacity {capacity} full. Doubling to {capacity * 2} (O({capacity}) copy cost)")
            
            # Simulate doubling by creating a new list and copying
            new_capacity = capacity * 2
            
            # The actual copy operation (O(capacity) time)
            new_list = current_items[:] 
            
            current_items = new_list # Reference the new, larger list conceptually
            capacity = new_capacity
        
        # Simulate O(1) append
        current_items.append(new_item) 
        print(f"Appended {new_item}. Size: {len(current_items)}, Capacity: {capacity}")

    return current_items

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size equals capacity (e.g., after the 2nd, 4th, 8th, 16th, ... element).
- What is the worst-case for a single append? O(n). This happens during a resize, requiring a copy of all 'n' existing elements.
- What is the amortized time per append overall? O(1). The total cost for N appends is O(2N), as the copying cost (N-1) is paid back over the subsequent O(N) operations.
- Space complexity: O(n).
- Why does doubling reduce the cost overall? Doubling ensures that the $O(n)$ cost of a resize is amortized over the $n$ subsequent $O(1)$ appends, preventing a worst-case $O(n^2)$ total time that would occur with constant-amount increases (e.g., +10).
"""
# Example:
add_n_items(6)

# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):

    result = []
    current_sum = 0
    
    for num in nums:
        current_sum += num
        result.append(current_sum)
        
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) (For the new list storing the running totals)
- Why this approach? It uses a single pass, maintaining a running sum, which is the most time-efficient (optimal O(n)) solution.
- Could it be optimized? Time complexity is already optimal at O(n).
"""
# Example:
print("P5 Output:", running_total([1, 2, 3, 4])) # Output: [1, 3, 6, 10]