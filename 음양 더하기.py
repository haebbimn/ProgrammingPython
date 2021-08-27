def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        #True에 해당하는 요소(item)는 뺀다
        if s[i] is True:
            answer += a[i]
            # False에 해당하는 요소(item)는 뺀다
        else:
            answer -= a[i]

    return answer


a = [4, 7, 12]
s = [True, False, True]
print(solution(a, s))