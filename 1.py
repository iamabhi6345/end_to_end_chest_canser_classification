# def lastElement(input1, input2):
#     if input1 == 1:
#         return 1
    
#     dp = [[0] * (input1 + 1) for _ in range(input1 + 1)]
    
#     for i in range(1, input1 + 1):
#         dp[i][i] = 1
    
#     for i in range(2, input1 + 1):
#         for j in range(1, i + 1):
#             dp[i][j] = dp[i - 1][j]
#             if j > 1:
#                 dp[i][j] += dp[i - 1][j - 1]
    
#     return dp[input1][input2]

# N = 5
# K = 1
# print(lastElement(N, K))  

# import sympy as sp

# # Define the variable
# a = sp.Symbol('a')

# # Define the equation
# eq = a**3 + 3*a**2 + 2*a - 50616

# # Solve the equation
# solutions = sp.solve(eq, a)

# # Print the solutions
# print(solutions)


# from sympy import symbols, Eq, solve

# # Define the variables
# x, y = symbols('x y')

# # Define the equations
# eq1 = Eq(50*y + x, 120000)
# eq2 = Eq(10*y + x, 60000)

# # Solve the equations
# solution = solve((eq1, eq2), (x, y))

# # Print the solution
# print(solution)


