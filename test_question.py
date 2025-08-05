from local_dsa import question, solve_problem, test_problem

#> Set Question
question.name = "Sum Of "
## Problem found here: [ID: 1] Sum of Two Numbers

question.id = 1
## Attempting problem: Sum of Two Numbers
## Given two integers, return their sum.

class SumTwoNumbers:
    def solve(self, a, b):
        return a

solve_problem(question, SumTwoNumbers)
