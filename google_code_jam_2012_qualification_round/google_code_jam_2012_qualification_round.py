'''Google code jam 2012 qualification roundの[Speaking in tongues](https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b33/0000000000432cd2)を解いてみる．

入力: 小文字アルファベットと空白からなるGoogle語の文字列𝐺
出力: Google語の文字列𝐺を英語に変換した文字列𝑆
である'''

''' Speaking in tonguesのsampleの入出力例からグー英辞書を作る関数'''


def google_english_dictionary(input_file_name, output_file_name):
    # 出力例のファイルも「読み込み」で開く．
    # ここではグー英辞書の作成のために，出力例のファイルも「読み込み」で開いている
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'r')

    # グーグル英語辞書のために空の辞書を用意する
    ge_dict = {}
    # readline()で最初の1文に記載のテストケース数を読み取る
    T = int(input_file.readline())
    for t in range(T):
        # 入力データのGoogle語の文字列を1行読み込み、末尾（改行含む）空白文字は取り除いておく
        google_string = input_file.readline().strip()

        # 出力データは一旦、caseナンバーの部分と英語の部分を：で分割する
        case_number_string, english_string = output_file.readline().split(':')
        # english_string内の末尾（改行含む）空白文字は取り除いておく.
        english_string = english_string.strip()

        # グーグル語と英語の文字列の長さは同じはずなので，グーグル語のそれぞれの文字に関して，
        for i in range(len(google_string)):
            # グーグル文字を辞書キーとして、対応する英文字を辞書の値として覚える
            ge_dict[google_string[i]] = english_string[i]

    input_file.close()
    output_file.close()
    # 作ったグー英辞書を出力して終了する．
    return ge_dict

input_data_file_name = 'speaking_in_tongues_sample_input.txt'
output_data_file_name = 'speaking_in_tongues_sample_output.txt'
ge_dict = google_english_dictionary(ianput_data_file_name, output_data_file_name)

# 手作業で辞書に加える
ge_dict['z'] = 'q'
ge_dict['q'] = 'z'

# 1行標準入力から読み込んで，それをテストケース数とする.
T = int(input())

# テストケース数だけ繰り返す．
for t in range(T):
    # グーグル語の文字列を1行読み込む．
    google_string = input()
    # 英語文字列を空文字列として初期化する．
    english_string = ''
    # グーグル語のそれぞれの文字gに関して，
    for g in google_string:
        # グーグル語のgに対応する英文字を末尾に加える．
        english_string += ge_dict[g]

    # こうしてできた英文字列を解答として標準出力に表示する．
    print(f'Case #{t + 1}: {english_string}')

# 解答例(改善ver.)
def google_english_dictionary_using_zip(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name)
    ge_dict = {}
    T = int(input_file.readline())
    for t in range(T):
        google_string = input_file.readline().strip()
        case_number_string, english_string = output_file.readline().split(':')
        english_string = english_string.strip()

        # ここで，組み込み関数zipを使って,グーグル語の文字gと対応する英語の文字eのそれぞれに関して，
        for g, e in zip(google_string, english_string):
            # 対応する英文字を辞書の値として覚える.
            ge_dict[g] = e

    # zとqについても辞書に追加する
    ge_dict['z'] = 'q'
    ge_dict['q'] = 'z'

    input_file.close()
    output_file.close()

    return ge_dict

