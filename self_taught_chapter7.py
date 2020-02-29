# 1.
movie_list = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for movie in movie_list:
    print(movie)

# 2.
for i in range(25, 51):
    print(i)

# 3.
for i, movie in enumerate(movie_list):
    print(i, movie)

# 4.
import random
num_list = list(range(1, 7))
while True:
    print('終了するには q を入力してください')
    n = input('1~6の数字を入力してください:')
    m = random.choice(num_list)
    if n = 'q':
        break
    elif int(n) == m:
        print('当たり!')
    elif n in num_list:
        print('はずれ!')
    else:
        print('1~6の数字を入力するか、qで終了します')

# 5.
num_list_one = [8, 19, 148, 4]
num_list_two = [9, 1, 33, 83]
for i in num_list_one:
    for j in num_list_two:
        print(i * j)
