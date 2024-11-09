class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        output = [True if i+extraCandies >= max_candy else False for i in candies]
        return output