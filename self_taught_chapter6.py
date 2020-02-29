# 1.
for string in ['カミュ']:
    print(string)

# 2.
s = input('文書の種類を入力してください:')
t = input('宛名を入力してください:')
print('私は昨日{}を書いて、{}に送った!'.format(s, t))

# 3.
print('alders Huxley was born in 1894.'.capitalize())

# 4.
print('どこで? だれが? いつ?'.split())

# 5.
l = ' '.join(['The', 'fox', 'jumped', 'over', 'the', 'fence', '.'])
print(l.replace(l[-2], ''))

# 6.
print('A screaming comes across the sky.'.replace('s', '$'))

# 7.
print('Hemingway'.index('m'))

# 8.
## through

# 9.
print('three' + ' ' + 'three' + ' ' + 'three')
print(('three ' * 3).rstrip())

# 10.
sample = '四月の晴れた寒い日で、時計がどれも十三時を打っていた。'
print(sample[:10])
