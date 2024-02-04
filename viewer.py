N,A,B=map(int,input().split())
maps=[]
for i in range(N):
    if i%2==1:
        maps.append(["P" for _ in range(N)])
    else:
        maps.append(["x" for _ in range(N)])

def prints():
    print("-"*N)
    for i in range(N):
        print("".join(maps[i]))

# prints()

for i in range(A):
    if i*2<N:
        for j in range(N):
            maps[j][i*2]="x"
        maps[i*2][i*2]="R"
    else:
        # print()
        for j in range(N):
            maps[j][i*2-N-(N%2)+1]="x"
            maps[i*2-N-(N%2)+1][j]="x"
        maps[i*2-N-(N%2)+1][i*2-N-(N%2)+1]="R"

prints()

print(N//2)
print((N+1)//2) #ここでミスってた
print(N-A)
print(min((N+1)//2,N-A)*(N-A)>=B)
