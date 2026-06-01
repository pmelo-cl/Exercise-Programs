/*
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8

Explanation: There are 8 negatives number in the matrix.
*/

int countNegatives(int** grid, int gridSize, int* gridColSize) {

    int negs = 0;
    int cols = *gridColSize;

    for (int i = 0; i < gridSize; i++){
        for(int j = 0; j < cols; j++){
            if (grid[i][j] < 0){
                negs += cols- j;
                break;
            }
        }
    }
    return negs;
}