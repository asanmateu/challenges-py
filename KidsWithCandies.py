class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        """For each kid check if there is a way to distribute extraCandies among the kids such that he
        or she can have the greatest number of candies among them. Notice that multiple kids can have the
        greatest number of candies."""
        return (True if i + extraCandies >= max(candies) else False for i in candies)
