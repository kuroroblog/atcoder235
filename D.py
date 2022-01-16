from collections import deque

# 標準入力を受け付ける。
a, N = map(int, input().split())

# <方針>
# いずれかの操作をしても数字の桁数は減少しない。 ⏩ Nの最大値(10の6乗)を超えるまで、操作1, 操作2のどちらかができるまで行うと良い。

q = deque()

MAX_N = 10 ** 6

dist = [-1] * MAX_N

# 操作をせずに1に訪れたので、0を代入する。
dist[1] = 0

# 1からスタートするのでキューにその値を格納する。
q.append(1)

while len(q) > 0:
    x = q.popleft()
    tmp = x * a

    # Nの最大値を超えないかつ初めてtmpの値を訪れた場合。
    if tmp < MAX_N and dist[tmp] == -1:
        dist[tmp] = dist[x] + 1
        q.append(tmp)

    if x % 10 == 0 or x < 10:
        continue

    # x >= 10かつxが10で割り切れないときのみ以下の処理を行う。

    tmp = str(x)
    tmp = int(tmp[-1] + tmp[:-1])

    # Nの最大値を超えないかつ初めてtmpの値を訪れた場合。
    if tmp < MAX_N and dist[tmp] == -1:
        dist[tmp] = dist[x] + 1
        q.append(tmp)

print(dist[N])


