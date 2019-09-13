# = in python means assigning a number. so when dealing with operators and you want to mean equal to alone you use double equal to signs
# e.g.
d=1
e=2
print(d==e)

# inequality operator
print(d !=e)

# comparison operators are used with conditional statements which are 'if' statements
# Logical operators
    # and - all conditions must be true
    # OR - At least one condition must be true
            # true and true - true
            # true and false - false
            # true or false - true
            # false or false - false

    # Not - It is to negate conditions
print(True and False)

print(not (True and False))

print(not (True and False or True))
            # and is treated as multiplication
            # or is treated as addition

print(not (1<3 and 2>4 or 3>3))