## Problem Statement

Given a number (target) and a list of numbers (list_of_numbers), find all unique combinations of 4 numbers from list_of_numbers where the numbers sum to target. A number can be used multiple times but combinations should be unique.

### Example

```
target = 11
list_of_numbers = [0, 5, 2, 3, 4, 1]

Output = [(5, 5, 1, 0), (5, 4, 2, 0), (5, 4, 1, 1), (5, 3, 3, 0), (5, 3, 2, 1), (5, 2, 2, 2), (4, 4, 3, 0), (4, 4, 2, 1), (4, 3, 3, 1), (4, 3, 2, 2), (3, 3, 3, 2)]

```

### Notion of solution

The solution is based on the following observations:

1. If list of numbers is sorted in descending order,then if you pick the number from 0 index and create all combinations there is no need to consider index 0 number again when next number from list is picked. i.e. from above example if you pick 5 from index 0 and create all combinations, then when you pick 4 from index 1, you don't need to consider 5 again.

2. A number can repeat itself in a combination upto target//number times. i.e. if target is 11 and number is 5, then 5 can repeat itself 2 times at most in a combination. This is because 5\*3 = 15 > 11. So 5 can repeat itself 2 times in a combination.

3. The problem can be broken down i.e., if you have a list of numbers [5, 4, 3, 2, 1, 0] and target is 11, now suppose you pick (5,5) and you have two more positions to be filled in the combination. Now the problem is reduced to finding all combinations of 2 numbers from the list [4, 3, 2, 1, 0] where the numbers sum to 1. This is a subproblem of the original problem and can be solved recursively with same logic.

4. If the factor of the target for a number is greater than 4 (positions/placeholders) and the list of numbers is sorted in descending order then in no scenario there be a combination of numbers from the list that sum to target. i.e. if target is 11 and number is 2, we are trying to fill 4 positions with 2, then factor is 11//2 = 5, so there is no way we can fill 4 positions with 2.
