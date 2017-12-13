def almostIncreasingSequence(sequence):
    """
       MISSING DESCRIPTION
    """
    if len(sequence) == 0:
        return False
    if len(sequence) == 1:
        return False
    elif len(sequence) == 2:
        if sequence[1] < sequence[0]:
            return False
    elif len(sequence) == 3:
        if len(set(sequence)) < 3:
            return False
        if sequence[0] > sequence[1] and sequence[1] > sequence[2]:
            return False
    elif len(sequence) == 4:
        errorCount = 0
        if len(set(sequence)) <= 2:
            return False
        if sequence[0] > sequence[1]:
            errorCount += 1
        if sequence[1] > sequence[2]:
            errorCount += 1
        if sequence[2] > sequence[3]:
            errorCount += 1
        if errorCount > 1:
            return False
    if len(sequence) > 4:
        i = 0
        mod_seq = sequence[:]
        hasRemoved = False

        while True:
            try:
                    
                first = mod_seq[i]
                second = mod_seq[i+1]
                third = mod_seq[i+2]
                fourth = mod_seq[i+3]
                
                if len(set([first, second, third, fourth])) <= 2:
                    return False
                
                if first == second:
                    if hasRemoved:
                        return False
                    hasRemoved = True
                    del mod_seq[i]

                if third == second:
                    if hasRemoved:
                        return False
                    hasRemoved = True
                    del mod_seq[i+1]

                if fourth == third:
                    if hasRemoved:
                        return False
                    hasRemoved = True
                    del mod_seq[i+2]
                
                if len(sequence)-i == 5:
                    if fourth < third and hasRemoved:
                        return False

                if first > second and second < third:
                    ## remove first
                    if hasRemoved:
                        return False
                    hasRemoved = True
                    del mod_seq[i]

                    if i + 4 >= len(mod_seq):
                        new_first = mod_seq[i+1]
                        new_second = mod_seq[i+2]
                        new_third = mod_seq[i+3]
                        if new_third < new_second or new_second < new_first:
                            return False
                    
                if third < second and second < fourth:
                    ## Remove third
                    if hasRemoved:
                        return False
                    hasRemoved = True
                    del mod_seq[i+2]
                if third < second and not (second < fourth):
                    if first >= third:
                        return False
                    ## remove second
                    if hasRemoved:
                        return False
                    hasRemoved = True
                    del mod_seq[i+1]
                    
                if fourth <= third:
                    if fourth <= second:
                        ## Remove fourth
                        if hasRemoved:
                            return False
                        hasRemoved = True
                        del mod_seq[i+3]
                        if i + 4 >= len(mod_seq):
                            new_first = mod_seq[i+1]
                            new_second = mod_seq[i+2]
                            new_third = mod_seq[i+3]
                            if new_third < new_second or new_second < new_first:
                                return False
                    else:
                        ## Trap!!
                        if hasRemoved:
                            return False
                        hasRemoved = True
                        del mod_seq[i+2]
                        if i + 4 >= len(mod_seq):
                            new_first = mod_seq[i+1]
                            new_second = mod_seq[i+2]
                            new_third = mod_seq[i+3]
                            if new_third <= new_second or new_second <= new_first:
                                return False
                i += 1
            except IndexError:
                break
    return True
