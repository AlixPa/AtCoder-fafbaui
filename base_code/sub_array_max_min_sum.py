def maxSubArraySum(a,size):
  max_so_far =a[0]
  curr_max = a[0]
  index = 0
  for i in range(1,size):
    curr_max = max(a[i], curr_max + a[i])
    if curr_max > max_so_far:
      index = i
      max_so_far = curr_max 
  return index, max_so_far

def minSubArraySum(a,size):
  min_so_far =a[0]
  curr_min = a[0]
  index = 0
  for i in range(1,size):
    curr_min = min(a[i], curr_min + a[i])
    if curr_min < min_so_far:
      index = i
      min_so_far = curr_min 
  return index, min_so_far

index_right, sum_sub = maxSubArraySum(ls, len(ls))
index_right, sum_sub = minSubArraySum(ls, len(ls))

index_left = index_right
sum_tmp = ls_a[index_right]
while sum_tmp != sum_sub:
  index_left -= 1
  sum_tmp += ls_a[index_left]