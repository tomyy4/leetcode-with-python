from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answers = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                answers.append("FizzBuzz")
            elif i % 5 == 0:
                answers.append("Buzz")
            elif i % 3 == 0:
                answers.append("Fizz")
            else:
                answers.append(str(i))

        return answers
    
s =Solution()
print(s.fizzBuzz(n=3))
print(s.fizzBuzz(n=5))
print(s.fizzBuzz(n = 15))
