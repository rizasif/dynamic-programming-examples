from route import bestRoute
from conference import bestSelection
from combinations import possibleCombinations

# This file provides an example for running the given algorithms

print("\n-----------------------Best Route--------------------------")

# Best route from top of mountain
mountain = [[1], [1, 2], [3, 5, 4], [2, 6, 7, 4]]
bestRoute(mountain)

print("\n---------------------Best Selection------------------------")

# Best conflict-free conference combination with max profit
conferences =  {"Conference    1":    [1300,    1559,    300],
                "Conference    2":    [1100,    1359,    500],         
                "Conference    3":    [1600,    1759,    200]}
bestSelection(conferences) 

print("\n------------------Possible Combinations---------------------")

# All possible solutions which sum up to a number
possibleCombinations(4)

print("------------------------------------------------------------")