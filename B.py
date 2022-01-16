# 標準入力を受け付ける。
N = int(input())

h_list = list(map(int, input().split()))

ans = 0
# 左から順番に台を見ていく。
for h in h_list:
    # H(i)の台とH(i + 1)の台を比較する。
    # H(i) < H(i + 1)の場合、次の右の台を確認する。
    if ans < h:
        ans = h
    else:
        break

# H(i) >= H(i + 1)の場合、H(i)の値を答えとして出力する。
print(ans)
