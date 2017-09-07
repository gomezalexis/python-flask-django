# task 1
words = "It's thanksgiving day. It's my birthday,too!"

print "The first index of day is", words.find('day')

new_words = words.replace('day', 'month', 1)
print new_words
# task 2
x = [2,54,-2,7,12,98]
minimum = min(x)
maximum = max(x)
print "The minimum is {} and the maximum is {}.".format(minimum, maximum)

x_list = ["hello",2,54,-2,7,12,98,"world"]
first_one = x_list[0]
last_one = x_list[len(x_list)-1]
print "The first value is:", first_one
print "The last value of the list is:", last_one

new_list = []
new_list.append(first_one)
new_list.append(last_one)

last_list = [19,2,54,-2,7,12,98,32,10,-3,6]
print "This is before sort:", last_list
last_list.sort()
print "This is after sort function:", last_list

# shorter_list = last_list.pop(0:len(last_list)/2)
# insert(0,'white')
shorter_list = last_list[0:len(last_list)/2]
# print shorter_list
# last_list.pop(shorter_list)
last_list.insert(0,shorter_list)
print last_list
