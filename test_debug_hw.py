"""
test_debug_hw.py homework for csci141.
"""

#######################################################################
## problem 1 of 2.
#######################################################################
# There is a problem with the is_reverse_of function below.
# Assignment 1:
# 1.1. Develop a suite of tests to properly test the function.
# 1.2. Debug this faulty function to locate and correct the problem.

def is_reverse_of( st1, st2 ):
    """
    is_reverse_of : String String -> Boolean
    is_reverse_of tells if one string is the reverse of another.
    preconditions: st1 and st2 are character strings.
    """
    if len( st1 ) != len( st2 ):
        return False
    i = 0
    j = len( st2 ) - 1
    while j > 0:
        if st1[i] != st2[j]:
            return False
        i += 1
        j -= 1

    return True

def test_is_reverse_of():
    """
    a suite of pass/fail test cases to validate that is_reverse_of works.
    """
    case1 = "a"
    case2 = "aa"
    case3 = "2"
    case4 = "232"
    case5 = "22"
    case6 = "a!a"
    case7 = "321"
    case8 = "abcdefghijklmnopqrstuvwxyz"
    case9 = "ab cd"
    case10 = "dc ba"

    result1 = is_reverse_of(case1, case1)
    print("Testing " + case1 + " and " + case1 + ": " + str(result1))
    if result1 == False:
        return False
    result2 = is_reverse_of(case1, case2)
    print("Testing " + case1 + " and " + case2 + ": " + str(result2))
    if result2 == True:
        return False
    result3 = is_reverse_of(case2, case1)
    print("Testing " + case2 + " and " + case1 + ": " + str(result3))
    if result3 == True:
        return False
    result4 = is_reverse_of(case3, case3)
    print("Testing " + case3 + " and " + case3 + ": " + str(result4))
    if result4 == False:
        return False
    result5 = is_reverse_of(case4, case5)
    print("Testing " + case4 + " and " + case5 + ": " + str(result5))
    if result5 == True:
        return False
    result6 = is_reverse_of(case6, case6)
    print("Testing " + case6 + " and " + case6 + ": " + str(result6))
    if result6 == False:
        return False
    result7 = is_reverse_of(case7, case7)
    print("Testing " + case7 + " and " + case7 + ": " + str(result7))
    if result7 == True:
        return False
    result8 = is_reverse_of(case8, case8)
    print("Testing " + case8 + " and " + case8 + ": " + str(result8))
    if result8 == True:
        return False
    result9 = is_reverse_of(case9, case10)
    print("Testing " + case9 + " and " + case10 + ": " + str(result9))
    if result9 == True:
        return False

    print("Tests Passed!")
    return True

# DO NOT CALL YOUR TEST FUNCTIONS HERE. See end of this file for directions.

#######################################################################
## problem 2 of 2.
#######################################################################
# There is a problem with the str_search function below.
# Assignment 2:
# 2.1. Develop a suite of tests to properly test this function.
# 2.2. Debug this faulty function to find and fix the problems.
#      The function is called indirectly by main_search.
#      You can use your test suite and/or main_search for debugging.
#      Initial Hints: search for J, L, or C.
# 2.3. Document your debugging results trying to fix the str_search code.

def str_search( data, target, start, end ):
    """
    str_search : String String NatNum NatNum -> NatNum or NoneType
    Description:
    Search for a target value in a sorted data string.
    The search happens between the start and end indices inclusively.
    This starts searching in the middle. If it finds the target, it is done.
    Otherwise it decides whether to search the first half or the second half.
    preconditions: the data string is in ascending alphanumeric order.
    Parameters:
        data - a string
        target - the target value to find is a single character string e.g. 'Q'
        start - the starting index into the data
        end - the ending index into the data
    Returns:
        index of target in data, if present; otherwise None.
    """

    if start == end:
        return None

    mid_index = ( start + end ) // 2
    mid_value = data[mid_index]

    # debug statement prints the data.
    #print( "Searching for", target, ":", data[start:mid_index],
    #    "*" + str( mid_value ) + "*", data[mid_index+1:end+1] )

    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return str_search( data, target, start, mid_index )
    else:
        return str_search( data, target, mid_index, end )

def find_target( data, target ):
    """
    find_target : String String -> NatNum or NoneType
    find_target returns the index of target in data or None if not found.
    Parameters:
        data - a string
        target - the target value to find
    Returns:
        The index of the target element in data, if present, or None.
    """

    return str_search( data, target, 0, len( data ) - 1 )

def makeString():
    """
    makeString : () -> String
    makeString returns a String
    """
    data = ""
    # append characters to make the string
    for num in range( 36, 108, 2 ):
        data += chr( num )
    return data

def main_search():
    """
    main_search : Void -> NoneType
    """

    data = makeString()
    print( "Number of elements: ", len( data ) )

    while True:
        print( "\nData: ", data )
        target = input( "Enter a character to find: " )

        if target == "":
            break
        else:
            index = find_target( data, target )
            print()
            if index != None:
                print( target, "found at index", index )
            else:
                print( target, "not found" )
    # end while

def test_str_search():
    """
    a suite of pass/fail test cases to validate that str_search works.
    """
    data = makeString()
    print( "Number of elements: ", len( data ) )
    print( "\nData: ", data )

    targets = ["$", "2", "j", "H"]
    for target in targets:
        index = find_target( data, target )
        if index != None:
            print( target, "found at index", index )
        else:
            print( target, "not found" )
            return False

    targets2 = ["G"]
    for target in targets2:
        index = find_target( data, target )
        if index == None:
            print( target, "not found" )
        else:
            print( target, "found at index", index )
            return False

    print("All tests passed!")
    return True

#######################################################################
# 2.3. Document your debugging results trying to fix the str_search code.
# Enter answers to the questions below inside the triple-quoted string.
"""
	Were you able to completely fix str_search?
	If not, explain in detail the cases that still fail.
	What tool(s) did you use?
	What went well?
	What problems did you have?

	No.
	My mind's ability to logic.
	Reading the code went well.
	I can't seem to figure out why j doesn't work.
	    It's the last character.

	The code logic was flawed.
	If we want to find the midpoint of the section of the string up to
	mid_value, our search needs to be inclusive.
	Therefore, we need to make the final argument mid_index,
	rather than mid_index - 1
"""
#######################################################################

if __name__ == "__main__":
    #
    # Run the test functions for problem 1 and problem 2.
    #
    test_is_reverse_of()
    test_str_search()
    #
    main_search()

# After finishing the problems, submit this file to the mycourses dropbox.
