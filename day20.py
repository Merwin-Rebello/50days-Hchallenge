# climbing stairs 
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=one+two
            one=two
            two=temp
        return two


class solution{
    public int climbStairs(int n ){
        int[] dp = new int[n+1];
        dp[0]=1; # first two are already determined
        dp[1]=1;
        for(int i=2; i<=n;i++){
            dp[i] = dp[i-1] + dp[i-2];# only option that can be taken is 2 steps noot more than that
        }
        return dp[n]
    }
}        