import random
def randomized_quicksort(arr):
if len(arr) <= 1:
  return arr
pivot = random.choice(arr)

left = [x for x in arr if x < pivot]
equal = [x for x in arr if x == pivot]
right = [x for x in arr if x > pivot]

return randomized_quicksort(left) + equal + randomized_quicksort(right)
