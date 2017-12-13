## -*- coding: utf-8 -*-
#"""
#Created on Sat Aug 12 22:09:13 2017
#
#@author: jayto_000
#"""
#
#def almostIncreasingSequence(sequence):
#    """
#       MISSING DESCRIPTION
#    """
#    remove_FLAG = False
#    skip_FLAG = False
#    for i in xrange(len(sequence)):
#        print 'seq:', sequence[i]
#        if skip_FLAG:
#            print "skip"
#            skip_FLAG = False
#            continue
#        print 'here'
#        try:
#            statement = sequence[i] < sequence[i+1]
#        except:
#            print "EOF"
#            return True
#        if not statement:
#            print "FALSE"
#            if remove_FLAG:
#                print 'fail twice'
#                return False
##            remove_FLAG = True
#            if i == 0:
#                print 'fail at beginning'
#                if not (sequence[i] < sequence[i+2]):
#                    return False
#                else:
#                    skip_FLAG = True
#            else:
#                print 'not fail at beginning'
#                skip_FLAG = True
#            if i == len(sequence):
#                return True
#        else:
#            pass
#            
#
##sequence = [1, 3, 2, 1]
##sequence = [2, 1, 3, 4, 5, 6]
##sequence = [1, 3, 2, 3, 4, 5]
##sequence = [1, 3, 2, 4, 8, 15]
##sequence = [1, 3, 0, 3, 4, 5]
##print almostIncreasingSequence(sequence)
#
#
#
#
#
#def proCategorization(pros, preferences):
#    answer = {}
#    for i in range(len(preferences)):
#        pref = preferences[i]
#        for j in xrange(len(pref)):
#            try:
#                answer[pref[j]].append(pros[i])
#            except KeyError:
#                answer[pref[j]] = [pros[i]]
#    keys = sorted(answer.keys())
#    final = []
#    for key in keys:
#        temp = [key]
#        final.append([temp, sorted(answer[key])])
#    return final
#
#
#
#
#preferences = [["Computer repair", "Handyman", "House cleaning"],
#               ["Computer lessons", "Computer repair", "Data recovery service"],
#               ["Computer lessons", "House cleaning"]]
#pros = ["Jack", "Leon", "Maria"]
#
#
##print proCategorization(pros, preferences)
#
#def spamClusterization(requests, ids, threshold):
#    import string
#    sets = []
#    for request in requests:
#        copy = request.split(' ')
#        words = []
#        allowed = string.ascii_letters
#        for word in copy:
#            temp = ''
#            for c in word:
#                if c in allowed:
#                    temp += c.lower()
#            words.append(temp)
#        sets.append(set(words))
#    matrix = []
#    for num in range(len(sets)):
#        matrix.append([None] * len(sets))
#    for i in range(len(sets)):
#        for j in range(len(sets)):
#            if i == j:
#                matrix[i][j] = None
#            else:
#                intersection = sets[i].intersection(sets[j])
#                union = sets[i].union(sets[j])
#                matrix[i][j] = len(intersection)/len(union)
#    print matrix
##    intersection / union
#
#
#
#
#requests = ["I need a new window.",
#            "I really, really want to replace my window!",
#            "Replace my window.",
#            "I want a new window.",
#            "I want a new carpet, I want a new carpet, I want a new carpet.",
#            "Replace my carpet"]
#
#ids = [374, 2845, 83, 1848, 1837, 1500]
#threshold = 0.5
#
#print spamClusterization(requests, ids, threshold)
#
#
#
#
#
#
#
#
#def ratingThreshold(threshold, ratings):
#    indexes = []
#    for pro_i in xrange(len(ratings)):
#        total = len(ratings[pro_i])
#        rates = 0
#        for r in ratings[pro_i]:
#            rates += r
#        if rates/total > threshold:
#            indexes.append(pro_i)
#    return indexes
#    
#    
##threshold= 3.5
##ratings= [[3,4], 
## [3,3,3,4], 
## [4]]
# 
##print ratingThreshold(threshold, ratings)

#    
#    
#s1 = [1,3,2]        # True
#s2 = [1,3,2,1]      # false
#s3 = [1,3,2,4,5]    # true
#s4 = [1,8,2,3,4,5,6,7,8,9,10,11,12]#true
#s5 = [1,8,2,3,4,5,6,7,8,9,10,22,12]#false
#s6 = [1,8,2,3,4,8,2]#false
#s7 = [0,1,2,3,4,8,6]#true
#s8 = [9,2,3,4,8,5]  # false
#s9 = [1, 2, 18, 4, 4]    # true
#s10 = [2,2,3,4,3]
#s11 = [1,2,5,3,5]
#
#
##almostIncreasingSequence(s1)
##print almostIncreasingSequence(s2)
##print almostIncreasingSequence(s3)
#print almostIncreasingSequence(s9)
#print "============="
#
#
#def almostIncreasingSequence(sequence):
#    """
#       MISSING DESCRIPTION
#    """
#    print "sequence", sequence
#    if len(sequence) == 0:
#        return False
#    if len(sequence) == 1:
#        return False
#    elif len(sequence) == 2:
#        if sequence[1] < sequence[0]:
#            return False
#    elif len(sequence) == 3:
#        if sequence[0] > sequence[1] and sequence[1] > sequence[2]:
#            return False
#    elif len(sequence) == 4:
#        errorCount = 0
#        if len(set(sequence)) <= 2:
#            return False
#        if sequence[0] > sequence[1]:
#            errorCount += 1
#        if sequence[1] > sequence[2]:
#            errorCount += 1
#        if sequence[2] > sequence[3]:
#            errorCount += 1
#        if errorCount > 1:
#            return False
#    if len(sequence) > 4:
#        i = 0
#        mod_seq = sequence[:]
#        hasRemoved = False
#
#        while True:
#            try:
#                    
#                first = mod_seq[i]
#                second = mod_seq[i+1]
#                third = mod_seq[i+2]
#                fourth = mod_seq[i+3]
#
#                print "\nFirst: ", first
#                print "Second:", second
#                print "Third: ", third
#                print "Fourth:", fourth
#                
#                if len(set([first, second, third, fourth])) <= 2:
#                    return False
#                
#                if first == second:
#                    if hasRemoved:
#                        return False
#                    hasRemoved = True
#                    del mod_seq[i]
#
#                if third == second:
#                    if hasRemoved:
#                        return False
#                    hasRemoved = True
#                    del mod_seq[i+1]
#
#                if fourth == third:
#                    if hasRemoved:
#                        return False
#                    hasRemoved = True
#                    del mod_seq[i+2]
#                
#                if len(sequence)-i == 5:
#                    if fourth < third and hasRemoved:
#                        return False
#
#                if first > second and second < third:
#                    ## remove first
#                    if hasRemoved:
#                        return False
#                    hasRemoved = True
#                    del mod_seq[i]
#                if third < second and second < fourth:
#                    ## Remove third
#                    if hasRemoved:
#                        return False
#                    hasRemoved = True
#                    del mod_seq[i+2]
#                if third < second and not (second < fourth):
#                    if first >= third:
#                        return False
#                    ## remove second
#                    if hasRemoved:
#                        return False
#                    hasRemoved = True
#                    del mod_seq[i+1]
#                    
#                if fourth <= third:
#                    if fourth <= second:
#                        print "remove fourth"
#                        ## Remove fourth
#                        if hasRemoved:
#                            return False
#                        hasRemoved = True
#                        del mod_seq[i+3]
#                        if i + 4 >= len(mod_seq):
#                            new_first = mod_seq[i+1]
#                            new_second = mod_seq[i+2]
#                            new_third = mod_seq[i+3]
#                            if new_third < new_second or new_second < new_first:
#                                return False
#                    else:
#                        ## Trap!!
#                        print "trap"
#                        if hasRemoved:
#                            return False
#                        hasRemoved = True
#                        del mod_seq[i+2]
#                        if i + 4 >= len(mod_seq):
#                            new_first = mod_seq[i+1]
#                            new_second = mod_seq[i+2]
#                            new_third = mod_seq[i+3]
#                            if new_third <= new_second or new_second <= new_first:
#                                return False
#                        
#                i += 1
#            except IndexError:
#                first = mod_seq[i]
#                second = mod_seq[i+1]
#                third = mod_seq[i+2]
#
#                print "\nFirst: ", first
#                print "Second:", second
#                print "Third: ", third
#                break
#    return True      


#def matrixElementsSum(matrix):
#    """
#       MISSING DESCRIPTION
#    """
#    rows = len(matrix)
#    columns = len(matrix[0])
#    haunted = [0 for i in range(columns)]
#    total = 0
#    for row in xrange(rows):
#        print matrix[row]
#    for row in xrange(rows):
#        for room in xrange(columns):
#            if haunted[room] != 0:
#                continue
#            if matrix[row][room] == 0:
#                haunted[room] = 1
#                continue
#            total += matrix[row][room]
#    return total
#
#m1 = [[0,1,1,2], 
# [0,5,0,0], 
# [2,0,3,3]]
#print matrixElementsSum(m1)


#def allLongestStrings(inputArray):
#    """
#       MISSING DESCRIPTION
#    """
#    answer = [inputArray[0]]
#    longest = len(inputArray[0])
#    for entry in xrange(1,len(inputArray)):
#        if len(inputArray[entry]) > longest:
#            answer = [inputArray[entry]]
#            longest = len(inputArray[entry])
#            continue
#        elif len(inputArray[entry]) == longest:
#            answer.append(inputArray[entry])
#    return answer
#
#a1 = ["aba", 
# "aa", 
# "ad", 
# "vcd", 
# "aba"]
#
#allLongestStrings(a1)
#
#print allLongestStrings(a1)

def commonCharacterCount(s1, s2):
    """
       Itterate through the shortest string, and check each if element is contatined in the larger string
    """
    answer = 0
    n1 = sorted(s1)
    n2 = sorted(s2)
    if len(n1) >= len(n2):
        shortest = len(n2)
        for i in xrange(shortest):
            if n2[i] in n1:
                n1.remove(n2[i])
                answer += 1
    else:
        shortest = len(n1)
        for i in xrange(shortest):
            if n1[i] in n2:
                n2.remove(n1[i])
                answer += 1


    return answer
    
s1 = "aabcc"
s2 = "adcaa"

print commonCharacterCount(s1, s2)