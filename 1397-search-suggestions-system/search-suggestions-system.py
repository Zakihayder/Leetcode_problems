from bisect import bisect_left

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        ans = []
        left = 0

        prefix = ""
        for c in searchWord:
            prefix += c
            left = bisect_left(products, prefix, left)

            suggestions = []
            for i in range(left, min(left + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            ans.append(suggestions)

        return ans