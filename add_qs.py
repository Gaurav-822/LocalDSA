from local-dsa import insert_problem, insert_test_case

# Insert a problem
problem_id = insert_problem(
    "Sum of Two Numbers",
    "Given two integers, return their sum."
)

# Insert test cases
insert_test_case(problem_id, "1 2", "3")
insert_test_case(problem_id, "-1 5", "4")
insert_test_case(problem_id, "10 20", "30")
