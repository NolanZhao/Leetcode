class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        digits = list(reversed(digits))
        digits[0] += 1
        i, carry = 0, 0
        while i < len(digits):
            next_carry = (digits[i] + carry) / 10
            digits[i] = (digits[i] + carry) % 10
            i, carry = i + 1, next_carry
        if carry > 0:
            digits.append(carry)
        
        return list(reversed(digits))


a = Solution()
print a.plusOne([1, 2, 9, 9])