# Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.

# Otherwise, it should return false.

# Sample Input
# [1, 1, 2, 3, 1]
# [1, 1, 2, 4, 3]

# Expected Output
# True
# False



#lex_auth_0127135869481369601150

def list123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
    return False

nums=[1,2,3,4,5]
print(list123(nums))
