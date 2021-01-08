import sys
word = sys.stdin.readline()

word = word.lower()

alphabet_dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

for i in word:
    if i == 'a':
        alphabet_dict['a'] += 1
    if i == 'b':
        alphabet_dict['b'] += 1
    if i == 'c':
        alphabet_dict['c'] += 1
    if i == 'd':
        alphabet_dict['d'] += 1
    if i == 'e':
        alphabet_dict['e'] += 1
    if i == 'f':
        alphabet_dict['f'] += 1
    if i == 'g':
        alphabet_dict['g'] += 1
    if i == 'h':
        alphabet_dict['h'] += 1
    if i == 'i':
        alphabet_dict['i'] += 1
    if i == 'j':
        alphabet_dict['j'] += 1
    if i == 'k':
        alphabet_dict['k'] += 1
    if i == 'l':
        alphabet_dict['l'] += 1
    if i == 'm':
        alphabet_dict['m'] += 1
    if i == 'n':
        alphabet_dict['n'] += 1
    if i == 'o':
        alphabet_dict['o'] += 1
    if i == 'p':
        alphabet_dict['p'] += 1
    if i == 'q':
        alphabet_dict['q'] += 1
    if i == 'r':
        alphabet_dict['r'] += 1
    if i == 's':
        alphabet_dict['s'] += 1
    if i == 't':
        alphabet_dict['t'] += 1
    if i == 'u':
        alphabet_dict['u'] += 1
    if i == 'v':
        alphabet_dict['v'] += 1
    if i == 'w':
        alphabet_dict['w'] += 1
    if i == 'x':
        alphabet_dict['x'] += 1
    if i == 'y':
        alphabet_dict['y'] += 1
    if i == 'z':
        alphabet_dict['z'] += 1

value_lst = alphabet_dict.values()
max_value = max(value_lst)
max_key = max(alphabet_dict, key=lambda x: alphabet_dict[x])
cnt = 0

for v in value_lst:
    if v == max_value:
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(max_key.upper())