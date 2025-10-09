class Solution {

    public int minimumTotal(List<List<Integer>> triangle) {
        int[][] dp = new int[triangle.size()+1][triangle.size()+1];

        for(int i = triangle.size() - 1;i!=-1;i--){
            for(int j = triangle.get(i).size()-1;j!=-1;j--){
                dp[i][j]  = triangle.get(i).get(j) + Math.min(
                        dp[i+1][j],
                        dp[i+1][j+1]
                );
            }
        }

        return dp[0][0];
    }
}