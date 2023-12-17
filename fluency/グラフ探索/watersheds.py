# Google code jam 2009 qualification round: watersheds

## 問題の概要はここに書いてある：https://codingcompetitions.withgoogle.com/codejam/round/0000000000432cc4/0000000000432bd8

def node_connected_component(G, s):
    ''' NetworkXのnode_connected_componentと同じ役割を果たす関数．
    ただし，入力のグラフは以下のsolutionで用意された形式に対応する． '''

    # set(集合)で重複した値は消される
    # {}で囲まれているもの

    visited_nodes = set([s])
    boundary_nodes = set([s])

    while len(boundary_nodes) > 0:
        v = boundary_nodes.pop()

        # key v(value)が1つずつ2に代入される
        for w in G[v]:
            if w not in visited_nodes:
                visited_nodes |= set([w])
                boundary_nodes |= set([w])
    return visited_nodes

def solution(H, W, altitude):
    # 頂点名(h,w)をキーとして，valueを[]（空リスト）とする
    G = {(h, w): [] for h in range(H) for w in range(W)} 
    
    # 隣接する頂点のリストを値とする辞書で無向グラフを表す．
    # より標高の低いマスを探索する
    for h in range(H):
        for w in range(W):

            # altitudeにはそれぞれの区画の高さを保存する
            # 最低標高マスを現マス標高で一度初期化（池ごと）
            altitude_of_lowest_neighbor = altitude[h][w]
            
            #探索処理の順序：北➡西➡東➡南
            # 北
            # 1行目ではない and 上マス標高 < 現マス標高
            if h > 0 and altitude[h - 1][w] < altitude_of_lowest_neighbor:
                # 最小標高マス == 上マス
                altitude_of_lowest_neighbor = altitude[h - 1][w]
                # 大小関係なく隣接しているため、tuple型で隣接頂点を保存
                neighbor = (h - 1, w)
            
            # 西
            # 1列目ではない and 左マス標高 < 現マス標高
            if w > 0 and altitude[h][w - 1] < altitude_of_lowest_neighbor:
                # 最小標高マス == 左マス
                altitude_of_lowest_neighbor = altitude[h][w - 1]
                neighbor = (h, w - 1)

            # 東
            # 最終列目ではない and 右マス標高 < 現マス標高
            if w < W - 1 and altitude[h][w + 1] < altitude_of_lowest_neighbor:
                # 最小標高マス == 右マス
                altitude_of_lowest_neighbor = altitude[h][w + 1]
                neighbor = (h, w + 1)
            
            # 南
            # 最終行目ではない and 下マス標高 < 現マス標高
            if h < H - 1 and altitude[h + 1][w] < altitude_of_lowest_neighbor:
                # 最小標高マス == 下マス
                altitude_of_lowest_neighbor = altitude[h + 1][w]
                neighbor = (h + 1, w)
            
            # ここまでで隣接する区画の高さが自分の区画よりも真に小さいならば，
            if altitude_of_lowest_neighbor < altitude[h][w]:
                # その一番低い区画を自分の隣接頂点に加え，
                G[(h, w)].append(neighbor)
                # 同時に，自分を，その一番低い区画の隣接頂点に加える．
                G[neighbor].append((h, w)) 
    
    # aのunicode番号を取得
    unicode_point = ord('a')
    
    # 空文字列を成分とする行列（リストのリスト）を解の初期値とする.
    #[w個空白を作成]が縦にh個ある
    sol = [['' for w in range(W)] for h in range(H)]

    # それぞれの行hに関して，
    for h in range(H):
        # それぞれの列wに関して，
        for w in range(W):
            # すでに解として何らかの文字が設定されているならば，(=空白ではなかったら)
            if sol[h][w] != '':
                # いずれかの「池」に属すると判定されたあとなので，処理を省略する．
                continue
            
            # 上記の自作の関数で連結成分（の頂点集合）を得る．
            # 区画(h, w)が属するグラフ連結成分（の頂点集合）をcompとする．
            comp = node_connected_component(G, (h, w))
            
            # その連結成分の頂点に対応する区画それぞれに，
            for hh, ww in comp:
                # 引数に渡した数値をコードとするunicode文字を返す
                sol[hh][ww] = chr(unicode_point)
            # Unicode番号を1増やす. すなわち,アルファベット順で次の文字の番号にする．
            unicode_point += 1
    # こうして作った行列（リストのリスト）を返す．
    return sol

# 1行ずつ入力していくとプログラムを実行してくれる形式
# Tをテストケースの数とする．
T = int(input())

# テストケース1からTまで繰り返す．
for case_number in range(1, T + 1):
    # HとWを行数と列数とする．
    H, W = map(int, input().split())
    
    # altitudeにそれぞれの区画の高さを保存する．
    altitude = []
    for h in range(H):
        row = list(map(int, input().split()))
        altitude.append(row)
    
    # solutionで得られた，それぞれのテストケースの解をsolとする．
    sol = solution(H, W, altitude)

    print(f'Case #{case_number}:')
    # 得られた解を，行ごとに，
    for h in range(H):
        # 空白を挟んで1つの文字列にして表示する．
        print(' '.join(sol[h]))