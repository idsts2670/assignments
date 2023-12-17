import importlib

def solve(n, score_list):
  '''中身はこれから作る'''
  return score_list

def answer3(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')

    # とにかく繰り返す
    while True:
        # 引数を数値(整数)にして返す関数intを利用
        n = int(input_file.readline())
        if n == 0:
            # 繰り返しをやめる。この関数を終了する
            break
        score = []
        for i in range(n): # nに記載されている回数分繰り返す
            line = input_file.readline()
            score = score + [int(line)] # 数値に変換してscoreリストに追加する
        sums = sum(score) - max(score) - min(score) # リスト内の合計からリスト内の最大値と最小値を引くことで両値を除外する
        averages = sums / (n-2) # 最大値と最小値を除いた平均値を求める
        output_file.write(str(int(averages)) + '\n') # 平均点の端点を切り捨て、アウトプットファイルに書き込む
    
    input_file.close()
    output_file.close()
    return