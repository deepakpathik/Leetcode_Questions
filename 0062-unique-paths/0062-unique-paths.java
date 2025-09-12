class Solution{
    public int helper(int currentRow, int currentCol, int m, int n, int[][] memo){

        if(currentRow>=m || currentCol>=n) return 0;
        if(currentRow == m-1  && currentCol == n-1) return 1;
        if(memo[currentRow][currentCol] != -1) return memo[currentRow][currentCol];

        int ans = helper(currentRow+1,currentCol,m,n,memo) + helper(currentRow, currentCol+1,m,n,memo);
        memo[currentRow][currentCol] = ans;
        return ans;
        
    }
    public int uniquePaths(int m, int n) {
        int[][] memo = new int[m][n];
        for(int i = 0;i<m;i++){
            for(int j = 0;j<n;j++){
                memo[i][j] = -1;
            }
        }
        return helper(0,0,m,n,memo);
    }
}