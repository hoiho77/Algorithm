#p.321 Q7

#@time_check
def solution(n):
    split_p = int(len(n)/2)
    sum_1 = sum(list(map(int, [i for i in n[:split_p]])))
    sum_2 = sum(list(map(int, [j for j in n[split_p:]])))
    return "LUCKY" if sum_1 == sum_2 else "READY"

if __name__ == '__main__':
    n = input()
    print(solution(n))
