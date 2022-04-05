# ACM-ICPC 2017 日本国内予選 問題A: 太郎君の買物
# 解答例1

# 入力のn, m, aが与えられた時、予算以内で最大となる2つの商品の組み合わせの値を返す
## nは品物の個数、mは予算、aは品物の価格リスト
## 問題の設定から，品物の価格は少なくとも1なので，品物の価格の和の最大値は少なくとも2である．
def solution(n, m, a):
  
  # 品物の価格の和の最大値を保存する変数を用意し，初期値として0を代入する．
  maximum_total_prices = 0
  
  # iが0~n-2(最後から2つ前)に関して以下をループする
  for i in range(n-1):
    # jがi+1~n-1に関して以下をループする
    for j in range(i+1, n):
      # リストaのi番目とj番目の品物の合計をsum_of_pricesとする
      sum_of_prices = a[i] + a[j]
      # sum_of_pricesが予算m以下の場合以下を実施
      if sum_of_prices <= m:
        # sum_of_pricesが品物の価格和の最大値maximum_total_pricesより大きい場合:
        if sum_of_prices > maximum_total_prices:
          # sum_of_pricesを新しく最大値に据え置く
          maximum_total_prices = sum_of_prices
  # 全ての品物の組み合わせを試しても、最大値が0のままの（=予算以下の組み合わせがない）時
  if maximum_total_prices == 0:
    # 文字列NONEを返してこの関数を終了する.
    return 'NONE'
  # 最大値が0より大きいとき（=予算以下の組み合わせの最大値が見つかったとき）maximum_total_pricesの値を返す
  return maximum_total_prices

def answer(input_file_name, output_file_name):
  input_file = open(input_file_name)
  output_file = open(output_file_name, 'w')
  while True:
    # 1行目をスペース1個分で分割し、nに品物の個数、mに予算を代入する
    n, m = input_file.readline().split()
    # n, mは文字列のままなので整数にする
    n = int(n)
    m = int(m)
    # 品物の個数が0ならばbreak
    if n == 0:
      break
    # 2行目の品物の価格リストをスペース1個分で分割
    a = input_file.readline().split()
    
    # n = 品物数（全ての品物）に関して以下を実行
    for i in range(n):
      # 文字列を整数型に変換
      a[i] = int(a[i])
    # solution関数を使用して、最大となる2組の商品の組み合わせを出す
    output_file.write(f'{solution(n, m, a)}\n')
  return

# ファイル名（絶対パス）が長いので，一旦変数に代入しておく．
input_data_file_name = 'taro_purchase_input.txt'
output_data_file_name = 'taro_purchase_output.txt'

answer(input_data_file_name, output_data_file_name)

"""# 解答例1(改善ver.)

標準モジュールitertoolsの関数combinationsとブール演算子andを用いて改善した関数another_solutionを以下に定義する.
"""

import itertools

def another_solution(n, m, a):
  maximum_total_prices = 0
  # itertoolsのcombinationsを使用して、商品の価格リストの中から全ての組み合わせを出す
  for a_i, a_j in itertools.combinations(a, 2):
    sum_of_prices = a_i + a_j
    if sum_of_prices <= m and sum_of_prices > maximum_total_prices:
      maximum_total_prices = sum_of_prices
    if maximum_total_prices == 0:
      return 'NONE'
  return maximum_total_prices

"""組み込み関数mapとブール演算子andを用いて改善した関数another_answerを以下に定義する."""

def another_answer(input_file_name, output_file_name):
  input_file = open(input_file_name)
  output_file = open(output_file_name, 'w')
  while True:
    n, m = map(int, input_file.readline().split())
    if n == 0 and m == 0:
      break
    # input_fileから入力された文字列を空白で分割し、整数型に変換.
    a = list(map(int, input_file.readline().split()))
    
    #another_solution関数を使用して、最大となる2組の商品の組み合わせを出力する
    output_file.write(f'{another_solution(n, m, a)}\n')
  return

another_answer(input_data_file_name, output_data_file_name)

