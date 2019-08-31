n=int(input())
res= list(map(int,input().split()))
lst=max([res.count(i) for i in res])
print(lst)