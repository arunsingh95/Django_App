#1#2 digit (i,j)
X = '5,3'

print(X.split(','))
# for i in range(int(X.split(',')[0])):
# 	print ([i*j for j in range(int(X.split(',')[-1]))])
X = [[i*j for j in range(int(X.split(',')[-1]))] for i in range(int(X.split(',')[0]))]
# print(X)

######################################################################################
#2# reverse comma separated sentence and sort then alphabetically

var = 'without,hello,bag,world'

print (sorted(var.split(',')))

######################################################################################
#3#
"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
val=9
for i in range(val+1):
	print(val)
	# for j in range(i):
	# 	print (val)