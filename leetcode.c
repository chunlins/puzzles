/***********************************************************
** 2018-01-17
** Liu Chunlin / chunlins@outlook.com
** Solution for problem on leetcode.com.
** License on MIT
**
** FORMATER
** No. $problem_number | $problem_title | $difficulty
** $description
** $solution_one
** $code_one
** ...
** $testcase
**
** CONTENTS
**  * Problems
**  * Collections
**  * Solutions
************************************************************/


/***********************************************************
** Problems
** NO. 001 | Two Sum | Easy
************************************************************/

/***********************************************************
** TOP INTERVIEW QUESTIONS **
** https://leetcode.com/explore/interview/card/top-interview-questions-easy/
** 
************************************************************/

/*
** No. 001 | Two Sum | Easy
** Given an array of integers, return indices of the two numbers such that 
** they add up to a specific target.
** You may assume that each input would have exactly one solution, and you
** may not use the same element twice.
**
** Example:
**  Given nums = [2, 7, 11, 15], target = 9,
**  Because nums[0] + nums[1] = 2 + 7 = 9,
**  return [0, 1].
*/

// Note: The returned array must be malloced, assume caller calls free().
int* twoSum(int* nums, int numsSize, int target) {
    int i, j;
        int indices[] = {0, 0};
        for (i = 0; i < (numsSize - 1); i++)
            for (j = i + 1; j < numsSize; j++)
                if ( nums[i] + nums[j] == target)
                {
                    indices[0] = i;
                    indices[1] = j;
                    return indices;
                }
        return indices;
}


/*
** No. XXX | Rotate Array |
** Rotate an array of n elements to the right by k steps.
** For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is 
** rotated to [5,6,7,1,2,3,4].
**
** Note:
** Try to come up as many solutions as you can, there are at least 
** 3 different ways to 
** solve this problem.
** 
** Hint:
** Could you do it in-place with O(1) extra space?
** Related problem: Reverse Words in a String II
** 
** Credits:
** Special thanks to @Freezen for adding this problem and creating all test cases.
*/

void rotate(int* nums, int numsSize, int k) {
    int temps[numsSize];
    int i;
    for (i = 0; i < numsSize; i += 1)
        temps[(i + k) % numsSize] = nums[i];
    for (i = 0; i < numsSize; i += 1)
        nums[i] = temps[i];
}




/* 
** No. 136 | Single Number | Easy
** Given an array of integers, every element appears twice except for one.
** Find that single one.
**
** Note:
** Your algorithm should have a linear runtime complexity. 
** Could you implement it without using extra memory? 
*/

/* NORMAL SOLUTION */
int 
singleNumberSelf(int* nums, int numsSize) {
    int i, j, k;
    for (i = 0, j = numsSize-1; i <= numsSize / 2; i ++, j--)
        for (k = j; k > i; k--)
            if (nums[k] == nums[j])
            {
                // exchange nums[j] and nums[k]
                nums[k] = nums[k] + nums[j];
                nums[j] = nums[k] - nums[j];
                nums[k] = nums[k] - nums[j];
            }
    return nums[numsSize / 2];
}

/* USE XOR OPERATION */
int
singleNumberXOR(int* nums, int numsSize) {
    int i, result;
    for (i = 0; i < numsSize; i++)
        result ^= nums[numsSize];
    return result;
}

void rotate(int** matrix, int matrixRowSize) {
    int next = 0;
    int length, next, row, col;
    for (length = matrixRowSize; length > 1; length -= 2) {
        row = 0; col = 0;
        for (itera = row; itera < length - 1; itera++) {
            // matrix[row][col + itera]
            // matrix[col + itera][length - 1]
            // matrix[lenght - 1][lenght - 1 - col - itera]
            // matrix[col + itera][col]
            next = matrix[col + itera][length - 1];
            matrix[col + itera][length - 1] = matrix[row][col + itera];
            next = matrix[lenght - 1][lenght - 1 - col - itera];
            matrix[lenght - 1][lenght - 1 - col - itera] = matrix[col + itera][length - 1];
            next = matrix[col + itera][col]
            matrix[col + itera][col] = matrix[lenght - 1][lenght - 1 - col - itera];
            next = matrix[row][col + itera];
            matrix[row][col + itera] = matrix[col + itera][col];
        }
        row++; col++;
    }
}

void main(void) {
    int matrix[2][2] = {{1, 2}, {3, 4}};
    rotate(matrix, 2);
    for (int i = 0; i < 2; i++) { 
        for (int j = 0; j < 2; j++) 
            printf("%3d,");
        printf("\n");
    }
}
