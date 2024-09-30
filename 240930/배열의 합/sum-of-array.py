n = 4

A = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in A:
    result = 0
    for j in i:
        result += j
    print(result)