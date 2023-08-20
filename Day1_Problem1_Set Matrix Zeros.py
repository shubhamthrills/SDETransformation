# About
Challenge: **SDE Transformation**
Day: **1**
Problem: **1**
Category: **Array**
Problem Name: **Set Matrix Zeros**
Problem URL: https://leetcode.com/problems/set-matrix-zeroes
Solution URL:https://leetcode.com/problems/set-matrix-zeroes/solutions/3935886/sde-transformation-day-1-problem-1-python-well-explained/
Owner: **Shubham Sagar**

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We will itterate through ever element of the matrix and when we encoonter "0" we will make the whole row and column as "-1000" (Any Unique Number, So that we can idenitify which "0" was from beggining and which cell needs to be modified) if that cell was not already 0.

At the end we will re itterate and make the cell "0" whose value is -1000

# Approach
<!-- Describe your approach to solving the problem. -->
Step 1: We will initalize two varaible named "RowCounter" & "ColumnCounter" which will hold the value of Row and Column

    RowCounter,ColumnCounter = len(matrix)-1,len(matrix[0])-1

Step 2: We will start itterating through every cell of the matrix with 2 for loop 

         for row in range (len(matrix)):
            for column in range ((len(matrix[0]))):

Step 3: We will check if the current cell is having value 0 or not if yes then we will run a while loop twice one to make all row element as zero
    
    while(RowCounter >= 0):
        if (matrix[RowCounter])[column] != 0:
            (matrix[RowCounter])[column] = -1000
        RowCounter -= 1
and similarly to make the Columns as 0

    while(ColumnCounter >= 0):
        if (matrix[row])[ColumnCounter] != 0:
            (matrix[row])[ColumnCounter] = -1000
        ColumnCounter -= 1

Step 4: Post making every row and column cell as 0 we will re initalize the Step 1 Counter variable

    RowCounter,ColumnCounter = len(matrix)-1,len(matrix[0])-1

Step 5: At the end we will re itterate and check if cell has value "-1000" if yws then we will make it as 0

        for row in range (len(matrix)):
            for column in range ((len(matrix[0]))):
                if (matrix[row])[column] == -1000 :
                    (matrix[row])[column] = 0    

# Complexity
- Time complexity: **O(max(RowLength,ColumnLength)*RowLength*ColumnLength)**
<!-- Add your time complexity here, e.g. $$O(n)$$ --> 


- Space complexity: **O(1)**
<!-- Add your space complexity here, e.g. $$O(n)$$ --> 

# Code
```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        RowCounter,ColumnCounter = len(matrix)-1,len(matrix[0])-1
        for row in range (len(matrix)):
            for column in range ((len(matrix[0]))):
                if (matrix[row])[column] == 0 :
                    while(RowCounter >= 0):
                        if (matrix[RowCounter])[column] != 0:
                            (matrix[RowCounter])[column] = -1000
                        RowCounter -= 1
                    while(ColumnCounter >= 0):
                        if (matrix[row])[ColumnCounter] != 0:
                            (matrix[row])[ColumnCounter] = -1000
                        ColumnCounter -= 1
                    RowCounter,ColumnCounter = len(matrix)-1,len(matrix[0])-1
                else:
                    continue
        for row in range (len(matrix)):
            for column in range ((len(matrix[0]))):
                if (matrix[row])[column] == -1000 :
                    (matrix[row])[column] = 0
        
```


# Follow and Upvote the solution

```
For any Queries or Question Please pimg me / Follow me at

Linkedin: https://www.linkedin.com/in/shubhamsagar/
Instagram: https://instagram.com/shubhamthrills

For More detailed solution and placement related resource follow

Github: https://github.com/shubhamthrills

```
