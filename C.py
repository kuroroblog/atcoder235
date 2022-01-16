# 標準入力を受け付ける。
N, Q = map(int, input().split())

A = list(map(int, input().split()))

# dict型を用いて、数列を管理する。
# key : [num1, num2, ...]でデータ格納する。
# keyには、数列に格納される数字が入る。
# [num1, num2, ...]には、keyが数列内で登場する、位置を格納する。
number_list = {}

for i in range(len(A)):
    if number_list.get(A[i]) is None:
        # i + 1は配列のidxを考慮するため。
        number_list[A[i]] = [i + 1]
    else:
        # i + 1は配列のidxを考慮するため。
        number_list[A[i]].append(i + 1)

for _ in range(Q):
    x, k = map(int, input().split())

    # クエリのxが、数列に格納される数字を選択しなかった場合は、-1を出力する。
    if number_list.get(x) is None:
        print(-1)
        continue

    # k - 1 >= 数列の中にあるxの数だった場合、-1を出力する。
    # k - 1なのは、配列のidxを考慮するため。
    if k - 1 >= len(number_list[x]):
        print(-1)
        continue

    print(number_list[x][k - 1])
