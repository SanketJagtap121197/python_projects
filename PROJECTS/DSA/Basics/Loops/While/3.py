num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skip 3
    print(num)

# Output:
# 1
# 2
# 4
# 5
# The continue statement is used to skip a certain iteration of the loop.
# The loop will continue to run, but the iteration that contains the continue statement will be skipped.
# The output will be 1, 2, 4, 5.
