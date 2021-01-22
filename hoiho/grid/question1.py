#grid 알고리즘 공부
#큰수의 법칙

def solution(size, num, max, data):
  #배열을 가장 큰 수부터 정렬
  data_list = sorted(data, reverse=True)

  answer, count = 0, 0
  while True :
    if count > num :
      break

    for i in range(max):
      answer += data_list[0]
      count += 1

    answer += data_list[1]
    count += 1
 
  return answer

if __name__ == '__main__':
  
  size, num, max = map(int, input().split())
  data = list(map(int, input().split()))

  answer = solution(size, num, max, data)
  print(f"정답은 {answer}")
