def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: 3,4. for number in [1,2,3], if number > 1 means the condition applies to 2 and 3. return value + 1 means return 3 and 4.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: add_one(2) returns 3 because the function adds 1 to the input value. return sends the calculated value back to the code that called the function, whereas print() displays that value on the screen. In the loop, print() displays the values returned by add_one(). 
