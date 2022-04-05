
def room_connected_component(G, s):
    # 一度確認した部屋（頂点）を再度確認しないように（計算量を減らすために）記録する
    visited = {s}
    # 訪れた部屋が他の部屋とつながっていた場合、この変数に追加して再度確認
    remain = {s}

    # remainが存在している限りループする（=remainが空になったら(=つながりの最後の地点,部屋に到着したら)）
    while remain:
        z = remain.pop()

        # Gの中の部屋の位置情報を1個ずつ取り出す（複数あった場合でも1個ずつみていく）
        for yx in G[z]:
            
            # remainから取り出した隣接部屋が訪れたかどうか確認し、訪れていなかったらvisisted, remainに追加する
            if yx not in visited:
                visited |= {yx}
                remain |= {yx}

    return visited


def solution(n, altitude):
    G = {(h, w): [] for h in range(n) for w in range(n)}
    
    # 各部屋がどこの部屋と繋がっているのかの情報を保存するfor文
    # h, wは部屋の座標
    for h in range(n):
        for w in range(n):

            # 一旦neighborという箱に存在しない座標を据え置く
            neighbor = (-1, -1)
            num = altitude[h][w] + 1

            # 北
            if h > 0 and altitude[h - 1][w] == num:
                neighbor = (h - 1, w)

            # 西
            elif w > 0 and altitude[h][w - 1] == num:
                neighbor = (h, w - 1)
            # 東
            elif w < n - 1 and altitude[h][w + 1] == num:
                neighbor = (h, w + 1)

            # 南
            elif h < n - 1 and altitude[h + 1][w] == num:
                neighbor = (h + 1, w)

            if neighbor != (-1, -1):
                G[(h, w)].append(neighbor)

    
    # 部屋番号
    r = 10000
    # 繋がりの数
    cnt = 0

    for y in range(n):
        for x in range(n):

            if not G[(y, x)]:
                connection = {()}
            else:
                connection = room_connected_component(G, (y, x))

            # 部屋の連結数は一緒で、これまでの結果より部屋番号自体が小さい場合、小さいほうで更新
            if cnt == len(connection) and altitude[y][x] < r:
                r = altitude[y][x]
            
            # これまでの部屋の連結数より、今回のほうが大きかったら、大きい方で更新
            elif cnt < len(connection):
                r = altitude[y][x]
                cnt = len(connection)
            

    return r, cnt


# 入力処理
for i in range(int(input())):
    n = ""
    while n == "":
        n = input()
    n = int(n)
    altitude = [list(map(int, input().split())) for _ in range(n)]
    r, d = solution(n, altitude)
    print(f'Case #{i + 1}: {r} {d}')
