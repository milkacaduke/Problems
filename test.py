# inputs
weights = [1, 2, 3, 4, 5]
values = [1, 4, 4, 5, 7]
max_weight = 9

# Display helper function
def print2DArray(array):
	print("{}".format(" "*4), end="")
	print([i for i in range(len(array[0]))])
	for i in range(len(array)):
		print("[{}] {}".format(i, array[i]))




def knapsack(weights, values, max_weight):
	cache = [[0 for y in range(max_weight + 1)] for x in range(len(weights)+1)]

	for i in range(1, len(weights) + 1):
		for j in range(max_weight + 1):
			# if we couldn't choose because its over allowence
			if weights[i-1] > j:
				# copy above cell
				cache[i][j] = cache[i-1][j]
			# if we could choose to take new item
			else:
				# get the max of
					# 1. Value of dont take the new item
						# cache[i-1][j]
					# 2. Value of taking the new item
						# new weight and its value + 
						# row(j - i) from above row
				cache[i][j] = max(cache[i-1][j], values[i-1] + cache[i-1][j-i])

	print2DArray(cache)
	return cache[len(weights)][max_weight]


# driver
result = knapsack(weights, values, max_weight)
print("result: {}".format(result))
