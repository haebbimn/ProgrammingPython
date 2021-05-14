# def solution(arr):
#    left, right = 0, len(arr)-1
#    while left < len(arr)/2:
#        arr[left], arr[right] = arr[right], arr[left]
#        left += 1
#        right -= 1
#    return arr
#
# #The following is code to output testcase.
# arr = [1, 4, 2, 3] # input arr
# ret = solution(arr)
#
# #Press Run button to receive output.
# print("Solution: return value of the function is ", ret, " .")

#5번

#6번
def solution(scores):
   count = 0
   for s in scores:
       if 650 <= s or s < 800:
           count += 1
   return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")