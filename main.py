"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###


def linear_search(mylist, key):
	""" done. """
	for i, v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	# Base case: key is not present
	if left > right:
		return -1

	mid = (left + right) // 2  #Find the middle index
	mid_val = mylist[mid]  #Find the middle value from index
	if mid_val == key:  #if the middle value is the key, return the index
		return mid  #return middle value
		# Search in the left half
	elif key < mid_val:  #if key is less than mid
		return _binary_search(mylist, key, left, mid - 1)  #search the left half
	else:  #if key is greater than mid
		return _binary_search(mylist, key, mid + 1, right)  #search right half
	### TODO

	###


def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	startTime = time.time()  #establish start time
	search_fn(mylist, key)  #complete operation
	endTime = time.time()  #establish end time
	timeSpent = (endTime - startTime
	             ) * 1000  #calculate time difference then multiply by 100
	return timeSpent
	### TODO

	###


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	results = []  #created empty results array
	for size in sizes:  #loop through sizes
		n = int(size)  #convert to int
		mylist = list(range(n))  #create an array of numbers from 0 to n-1
		key = -1  #create a worst case scenario key
		binaryTime = time_search(binary_search, mylist,
		                         key)  #find time for binary search
		linearTime = time_search(linear_search, mylist,
		                         key)  #find time for linear search
		results.append((n, linearTime, binaryTime))  #append to results
	return results
	### TODO

	###


def print_results(results):
	""" done """
	print(
	    tabulate.tabulate(results,
	                      headers=['n', 'linear', 'binary'],
	                      floatfmt=".3f",
	                      tablefmt="github"))


if __name__ == "__main__":  #allows to call compare search
	print_results(compare_search())
