#ExerciseRandom from : https://www.youtube.com/watch?v=XKu_SEDAykw

'''
Input: list of values
Output: true/false of pairings adding up to a designated value

Example:
Input | Criteria | Output
[1,2,3,9], Sum = 8, False
[1,2,4,4], Sum = 8, True
'''

def functsum(listed , desval):
	for i in range(len(listed)):
		if (desval - listed[i]) in listed:
			return true
	else:
		return False


def functsum2(listed , desval):
	for i in listed:
        for j in listed:
            if (i+j) == desval:
                return True
    return False


#restrictions: cannot repeat added index
def functsum3(listed , desval):
	for i in range(len(listed)):
        for j in range(i+1, len(listed)):
            if (listed[i]+listed[j]) == desval:
                return True
    return False
