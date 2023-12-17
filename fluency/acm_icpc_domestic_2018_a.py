
def solution(n, a):
    average = sum(a) / n
  # 平均以下の所得の人数を数えるための変数を用意し，初期値を0とする.
    count = 0
  # それぞれの所得a_iに関して、所得が平均以下ならcountに+1する
    for a_i in a:
        if a_i <= average:
            count += 1
  # 平均以下の所得人数を返して終了する.
    return count

def answer(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    while True:
        # input_fileから入力された人数（の文字列）を整数に変換してnに代入する.
        n = int(input_file.readline())
        if n == 0:
            break
    # input_fileから入力されたn人分の所得文字列を空白で分割して、整数に変換したものを、さらにリストにしてaに代入する.
        a = list(map(int, input_file.readline().split()))
        output_file.write(f'{solution(n, a)}\n')
    input_file.close()
    output_file.close()
    return
# ファイル名（絶対パス）が長いので，一旦変数に代入しておく.
input_data_file_name = 'Income inequality_input.txt'
output_data_file_name = 'Income inequality_output.txt'
answer(input_data_file_name, output_data_file_name)