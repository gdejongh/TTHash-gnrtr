import numpy as np

from operator import add

from click._compat import raw_input
import git

# repo = git.Repo()
# o = repo.remotes.origin
# o.pull()

g = git.Git()
g.pull('origin','master')

def toTTH(nums):
    # convert nums into numpy array then into matrix
    nums = np.asarray(nums)
    nums = np.reshape(nums, (4, 4))
    # perform calculation
    running = np.sum(nums, axis=0) % 26
    nums = nums.flatten().tolist()
    idx = [3, 0, 1, 2, 6, 7, 4, 5, 9, 10, 11, 8, 15, 14, 13, 12]
    # shift things around
    values_by_index = dict(zip(idx, nums))
    nums = [values_by_index[index] for index in range(len(idx))]
    nums = np.asarray(nums)
    nums = np.reshape(nums, (4, 4))
    # perform calculation again
    temp = np.sum(nums, axis=0) % 26

    return sumElements(running, temp)

def sumElements(list1, list2):
    list3 = [(list1[0] + list2[0]) % 26, (list1[1] + list2[1]) % 26, (list1[2] + list2[2]) % 26, (list1[3] + list2[3]) % 26]
    return list3

# take user input

input1 = raw_input("Enter String: \n").upper().replace(" ", "")

#convert String to list
parts = list(input1)
digits = []
# Convert String to numbers: a:0 b:1 c:2...
for ch in parts:
    val = ord(ch) - 65
    digits.append(val)

#init lists
theList = [0,0,0,0]
inloop = []

# go through digits, every 16 elements update hash code
for i in range(len(digits)):
    inloop.append(digits[i])
    if (i + 1) % 16 == 0:
        theList = sumElements(theList, toTTH(inloop))
        inloop = []

# if the user input was not divisible by 16 fill the last matrix
if len(inloop) != 0:
    while len(inloop) != 16:
        inloop.append(0)
    theList = sumElements(theList, toTTH(inloop))


# get the hash code and print
str = ""
for c in theList:
    str += chr(c+97)


print str.upper()
