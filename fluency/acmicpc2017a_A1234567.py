def solve(n, m, price):
    '''中身はこれから作る予定'''
    return price


def answer(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    while True: # とにかく繰り返す
        #n = int(input_file.readline()) # 引数を整数にして返す関数intを利用
        line = input_file.readline() # まず1行読む
        line = line.split() # その1行を空白で区切ったリストにする
        n = int(line[0])
        m = int(line[1])
        if n == 0: # 品物数が0ならば，
            break # 繰り返しをやめる，すなわちこの関数を終了する．
        price = input_file.readline()
        price = price.split()
        for i in range(n):
            price[i] = int(price[i])
        output_file.write(str(solve(n, m, price)) + '\n')
    input_file.close()
    output_file.close()
    return