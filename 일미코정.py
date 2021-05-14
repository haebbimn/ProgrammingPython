#for i in range(0,4) : print(i)
#for i in range(6) : print(i)
#for i in range(0) : print(i)
#for i in range(10, 14) : print(i)
#
# for i in range(2,9):
# 	print(i)
#
# print(" ")
#
# for _ in range(2,5):
# 	print(_)
#
# print("\n\n")
# for k in range(2,9):
# 	print(k)

# def 보조함수(month, day):
#    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#    total = 0;
#    for i in range(month, day):
#        total += month
#    total += day
#    return total - 1
#
# def solution(start_month, start_day, end_month, end_day):
#    start_total = 보조함수(start_month, start_day)
#    end_total = 보조함수(end_month, end_day)
#    return end_total - start_total
#
# # testcase를 위한 output
# start_month = 1
# start_day = 2
# end_month = 2
# end_day = 2
# ret = solution(start_month, start_day, end_month, end_day)
#
# # Run을 누르면 받게되는 output.
# print("Solution: return value of the function is", ret, ".")
# from numpy import double
#
#
# def solution(price, grade):  # S 5프로, G 10프로, V 15프로
#
#
# # 코드 작성공간
# (double)salePrice1 = price1 * 0.05
# (double)salePrice2 = price2 * 0.15
# answer
#
# print("price | grade | Sale”)
# print("-----------------------------")
# print(price1 + "|" + grade1 + "|" +  answer)
# print(price2 + "|"+ grade2 + "|" + answer)
#
#
# return answer
#
# # testcase를 위한 output
# price1 = 2500
# grade1 = "V"
# ret1 = solution(price1, grade1)
#
# # Press Run button to receive output.
# print("Solution: return value of the function is", ret1, ".")
#
# price2 = 96900
# grade2 = "S"
# ret2 = solution(price2, grade2)
#
# # Press Run button to receive output.
# print("Solution: return value of the function is", ret2, ".")


#
# def 보조함수_a(arr):
#    counter = [0 for _ in range(1001)]
#    for x in arr:
#        counter[x] += 1
#    return counter
#
# def 보조함수_b(arr):
#    ret = 0
#    for x in arr:
#        if ret < x:
#            ret = x
#    return ret
#
# def 보조함수_c(arr):
#    INF = 1001
#    ret = INF
#    for x in arr:
#        if x != 0 and ret > x:
#            ret = x
#    return ret
#
# def solution(arr):
#    counter = 보조함수_a(arr)
#    max_cnt = 보조함수_b(arr)
#    min_cnt = 보조함수_c(arr)
#    return max_cnt // min_cnt
#
# #The following is code to output testcase.
# arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
# ret = solution(arr)
#
# #Press Run button to receive output.
# print("Solution: return value of the function is", ret, ".")

#----테스트 풀이----

def solution(price, grade):
    reduced_price = 0
    if grade == "S":
        reduced_price = price * 0.05
    if grade == "G":
        reduced_price = price * 0.10
    if grade == "V":
        reduced_price == price *0.15
        return price - reduced_price

price1 = 2500
grade1="V"
ret1 = solution(price1, grade1)
print("Solution: return value of the funtion is", ret1,".")