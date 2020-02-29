# 1.
import os

test_path1 = os.path.join('/users', 'moromotoki', 'desktop', 
                          'self_taught_programmer', 'test_file.txt')
with open(test_path, encoding='utf-8') as f:
    f.read()

# 2.
n = input('あなたの好きな色は何色ですか?:')
test_path2 = os.path.join('/users', 'moromotoki', 'desktop', 'self_taught_programmer')
with open(test_path2, 'w', encoding='utf-8') as f:
    f.write(n)

# 3.
import csv
list_in_list = [['Top Gun', 'Risky Business', 'Minority Report']
                ['Titanic', 'The Revenant', 'Inception']
                ['Training Day', 'Man on Fire', 'Flight']]
with open(test_path2, 'w', encoding='utf-8') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(list_in_list)

# 4.
list_in_list_inj = [['トップ・ガン', 'リスキー。ビジネス', 'マイノリティ・リポート'], 
                    ['タイタニック', 'レヴェナント', 'インセプション'], 
                    ['トレーニング・デイ', 'マン・オン・ファイア', 'フライト']]
with open(test_path2, 'w', encoding='utf-8') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(list_in_list_inj)

