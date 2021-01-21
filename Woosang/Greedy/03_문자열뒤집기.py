# 입력값이 전부 0 or 1이 되는 두가지 경우 비교
s = input()

cnt0, cnt1 = 0, 0
# cnt0 => 전부 0으로!! 
# cnt1 => 전부 1로!! 

if s[0] == "1":
    cnt0 += 1
    # 1을 0으로 바꿈(cnt0 += 1)
elif s[0] == "0":
    cnt1 += 1
    # 0을 1로 바꿈(cnt += 1)

for i in range(len(s)-1): # 마지막 확인을 위해 len(s) - 1
    if s[i] != s[i+1]:
        if s[i+1] == "1":
            # 비교한 값 == 1이면 0으로 바꿈(cnt0 += 1)
            cnt0 += 1
        elif s[i+1] == "0":
            # 비교한 값 == 0이면 1로 바꿈(cnt1 += 1)
            cnt1 += 1

print(cnt0, cnt1)# s를 0이랑 1로 바꿨을 때의 두경우 중 작은 수 반환

## s = "1001100"
## 결과값 = 2
