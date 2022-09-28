import math
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break



length =  len(numbers) %2
numbers = sorted(numbers)



if length == 0:
    print((numbers[math.floor(len(numbers)/2)] + numbers[math.floor(len(numbers)/2)-1] )/2)
    
    

else:
    
    print(numbers[math.floor(len(numbers)/2)])
