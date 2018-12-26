def solve(n, coins, k):
  # print("n: %d, k: %d" % (n, k))
    if k < 0 or n < 0:
        return 0

    if n == 0:  # Change for 0 is only empty one.
        return 1
          # print("  n: %d, k: %d" % (n, k - 1))
    # print("  n: %d, k: %d" % (n - coins[k], k))

    # solve(n, coins, k - 1) -> Count of money without coins[k]
    # solve(n - coins[k], coins, k) -> Count of (money - coins[k]) with coins[k]
    count = solve(n, coins, k - 1) + solve(n - coins[k], coins, k)

    # print("Count: %d" % count)
    return count


def count_change(money, coins):
    return solve(money, coins, len(coins) - 1)
