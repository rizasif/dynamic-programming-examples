
def bestRoute(mountain):
    "This function finds the maximum value while travelling top to down from a mountain."
    "For example mountain=[[1], [1, 2], [3, 5, 4], [2, 6, 7, 4]]"

    # Check if mountain is indeed list
    assert isinstance(mountain, list)

    # Current index and value of step in mountain under consideration
    current_index = 0
    current_value = mountain[0][current_index]

    # The output path and score value
    path = []
    score = current_value

    # Iterating the mounting level by level,
    # Except for the first level since it contains only one element
    iterMountain = iter(mountain)
    next(iterMountain)
    for level in iterMountain:
        # Getting the pair of numbers the current value can move to
        next_pair = [level[current_index], level[current_index+1]]

        # Index of the largest value from the pair
        new_index = current_index

        # Find the largest value from the pair and store in new_index
        if(next_pair[0] < next_pair[1]):
            new_index = new_index + 1
            current_value = next_pair[1]
        else:
            current_value = next_pair[0]
        
        # Append the transition from current to new index and update score
        path.append((current_index, new_index))
        score += current_value

        # Update the index
        current_index = new_index
    
    # Printing Results
    print "Route: ", path
    print "Score: ", score