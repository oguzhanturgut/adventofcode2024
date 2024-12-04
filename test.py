def max_subarray_sum(nums, k):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i - k + 1]
    return max_sum

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == '__main__':
    print(max_subarray_sum([100, 2, 3, 4, 5, 6 , 7 , 8, 1000], 2))
    print(longest_common_subsequence("abcde", "ace"))
