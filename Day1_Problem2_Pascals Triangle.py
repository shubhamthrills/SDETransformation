# About
Challenge: **SDE Transformation**
Day: **1**
Problem: **2**
Category: **Array**
Problem Name: **Pascals Triangle**
Problem URL: https://leetcode.com/problems/pascals-triangle/
Solution URL:https://leetcode.com/problems/pascals-triangle/solutions/3961543/sde-transformation-pascals-triangle-day-1-problem-2-python-well-explained/
Owner: **Shubham Sagar**

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We will try to break the traiangle to normal pattern problem and try to develop a generic logic that satisfies the condition for Pascals Triangle

Pattern:
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1

If we carefully observe then First and Last element of every Row is 1 and the rest elements i.e., elements between 0 and len(Row) is basically a sun of its upper and upper left emenet

Example (arr[4])[2]) is 6 == (arr[3])[1]) + (arr[3])[2])

o in genric the logic is  arr[i-1][j-1] + arr[i-1][j]
# Approach
<!-- Describe your approach to solving the problem. -->
Step 1: We will create an structure of full pattern having all zeros
      
    Pascal = [[0 for j in range(i)] for i in range(1, numRows+1)]

    Pascal will contains [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

    Simpler View in Pattern:
    0
    0 0
    0 0 0 
    0 0 0 0 
    0 0 0 0 0 

Step 2: We will start itterating through each row of the structure we formed and make that entire row with "1" and in that row we would form nested for loop in whichh the elemnet between start and last elemnet will be calculated based on logic we formed above

         for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = Pascal[i-1][j-1] + Pascal[i-1][j]

Step 3: At last we will assign the calculate value to Pascal list/array that we formed
    
    Pascal[i] = row
    

# Complexity
- Time complexity: **O(N^2)**
<!-- Add your time complexity here, e.g. $$O(n)$$ --> 


- Space complexity: **O(NumberOfElement) == O(N)**
<!-- Add your space complexity here, e.g. $$O(n)$$ --> 

# Code
```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Pascal = [[0 for j in range(i)] for i in range(1, numRows+1)]
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = Pascal[i-1][j-1] + Pascal[i-1][j]
            Pascal[i] = row
        return Pascal        
```


# Follow and Upvote the solution

```
For any Queries or Question Please ping me / Follow me at

Linkedin: https://www.linkedin.com/in/shubhamsagar/
Instagram: https://instagram.com/shubhamthrills

For More detailed solution and placement related resource follow

Github: https://github.com/shubhamthrills

```
