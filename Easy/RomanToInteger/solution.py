"""
This is the Roman to Integer Solution that I created for the purposes of solving the problem on Leetcode.
"""

def romanToInt(s):
        conversion = {
                        "I":1,
                        "V":5,
                        "X":10,
                        "L":50,
                        "C":100,
                        "D":500,
                        "M":1000
                    }
        # combinations = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        combinations = ["IV", "IX", "XL", "XC", "CD", "CM"]
        answer = 0
        index = 0
        while index != len(s):
            if index == len(s) - 1:
                answer += conversion[s[index]]
                index += 1
            else:
                combo = s[index] + s[index + 1]
                if combo in combinations:
                    # answer += combinations[combo]
                    answer += conversion[s[index + 1]] - conversion[s[index]]
                    index += 2
                else:
                    answer += conversion[s[index]]
                    index += 1

        return answer