def bestSelection(conferences):
    " This function finds conflict-free combination of conferences "
    " best suitable for maximum profit "

    # Check that conferences is indeed a dictionary
    assert isinstance(conferences, dict)

    # List of Name of conferences, also keys of the dictionary
    conference_keys = conferences.keys()

    # List of all conflict free conferences
    conflict_free_combination_keys = []
    for key in conference_keys:
        # Current conference under consideration
        conf = conferences[key]
        # keys of all other conferences
        other_conference_keys = conference_keys[conference_keys.index(key):]
        for next_key in other_conference_keys:
            # next conference to be compared with conference under consideration
            # for checking conflicts 
            next_conf = conferences[next_key]
            if(next_conf[0] > conf[1] or next_conf[1] < conf[0]):
                # next conference either starts later or ends early,
                # So add to list
                conflict_free_combination_keys.append((key, next_key))
    
    # The output best combination and best participation sum 
    best_combination_key = conflict_free_combination_keys[0]
    best_sum = 0
    for keys in conflict_free_combination_keys:
        # sum of participation for current conflict-free combination
        sum = 0
        for key in keys:
            sum = sum + conferences[key][2]
        
        if(sum > best_sum):
            # place in the sum of best participation number
            best_sum = sum
            best_combination_key = keys
    
    # print results
    print "Selected Conferences: ", best_combination_key
    print "Total number of participants: ", best_sum
