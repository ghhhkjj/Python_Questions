## Exercise 1. Calculate the cube of all numbers from 1 to a given number
number = int(input("Enter the number here : "))
n = 1
for i in range(1,number+1):
    i = i**3
    n += 1 
    print(f"Current number is: {n} and the cube of {n} is: {i}")

 ##Exercise 2. Display numbers from a list using a loop
    #Given a list of numbers, iterate through it and print numbers that satisfy these conditions:
        numbers = [12, 75, 150, 180, 145, 525, 50]
    # 1.The number must be divisible by five.
    # 2.If the number is greater than 150, skip it and move to the next.
    # 3.If the number is greater than 500, stop the loop entirely.
    numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    # To check the number is greater than 500 to break the loop.
    if i > 500:
        break
    # To check the number is greater than 150 to skip it and move to next move.
    if i > 150:
        continue
    # To check the number is divisible by five.
    if i%5 == 0:
        print(i)
    
