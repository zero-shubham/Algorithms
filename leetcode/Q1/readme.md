### Problem
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

### Notion of solution
1. Since array is sorted, when number is picked to be worked on we know once it's found twice we are free to replace any other occurence of that number after that.
2. use `i` pointer as marker for where to replace the number
3. use `j` pointer to sweep through the array
4. once the count for current number has reached 2, stop moving `i` as next replacement will be adjacent to this
5. after count of 2 is reached for current number, replace for next new number and reset the count