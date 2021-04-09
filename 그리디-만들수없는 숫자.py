num = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1 # 일단 타겟을 1로 설정.

for i in data:
    if target < i: #만약 타겟보다 집합안의 수가 더 크다면, 타겟은 만들 수 없게됨
        break
    target += i #하지만 타겟보다 집합안의 수가 작거나 같다면 타겟이 꼭 만들어지진 않더라도, ( 여기선 꼭만들어짐 왜냐하면 1차이로 계산하기 때문) 결국 타겟에 가까워지게됨
    
                #이런 방식으로 1부터 만들 수 있는 집합을 늘려나가면 된다.
                # +=i의 이유는 만약에 0,1,2,...x까지 만들 수 있는 상태라면 i가 추가됐을때 0+i부터 x+i까지 만들 수 있기 때문임.
                #여기서 생각해볼 것은 0+i가 target보다 큰가? 아니면 x+i가 target보다 작은가?를 생각해보면 됨.
print(target)
