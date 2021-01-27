#p.322 Q8

#@time_check
def solution(n):
    sum_num = 0
    sort_n = sorted(n)

    for data in sort_n : 
        try : 
            sum_num += int(data)       
        except :
            index = sort_n.index(data)
            break
    
    answer = ''.join(sort_n[index:])+ str(sum_num)
    
    return answer
    
if __name__ == '__main__':
    n = input()
    print(solution(n))
