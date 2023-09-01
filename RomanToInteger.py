class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev_value = 0
        roman_to_int_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        for char in reversed(s):
            value = roman_to_int_mapping[char]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total

p1 = Solution();
roman_numeral = "MCMXCIV"  # Example Roman numeral
integer_value = p1.romanToInt(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")
