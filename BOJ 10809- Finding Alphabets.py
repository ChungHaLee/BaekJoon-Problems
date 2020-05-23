import sys
word = sys.stdin.readline()
alphabet_dict = {'a':-1,'b':-1,'c':-1,'d':-1,'e':-1,'f':-1,'g':-1,'h':-1,'i':-1,'j':-1,'k':-1,'l':-1,'m':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,'s':-1,'t':-1,'u':-1,'v':-1,'w':-1,'x':-1,'y':-1,'z':-1}

word_lst = []
for i in word:
    word_lst.append(i)

word_lst.remove('\n')


for i in word_lst:
    if i == 'a':
        alphabet_dict['a'] = word_lst.index('a')
    if i == 'b':
        alphabet_dict['b'] = word_lst.index('b')
    if i == 'c':
        alphabet_dict['c'] = word_lst.index('c')
    if i == 'd':
        alphabet_dict['d'] = word_lst.index('d')
    if i == 'e':
        alphabet_dict['e'] = word_lst.index('e')
    if i == 'f':
        alphabet_dict['f'] = word_lst.index('f')
    if i == 'g':
        alphabet_dict['g'] = word_lst.index('g')
    if i == 'h':
        alphabet_dict['h'] = word_lst.index('h')
    if i == 'i':
        alphabet_dict['i'] = word_lst.index('i')
    if i == 'j':
        alphabet_dict['j'] = word_lst.index('j')
    if i == 'k':
        alphabet_dict['k'] = word_lst.index('k')
    if i == 'l':
        alphabet_dict['l'] = word_lst.index('l')
    if i == 'm':
        alphabet_dict['m'] = word_lst.index('m')
    if i == 'n':
        alphabet_dict['n'] = word_lst.index('n')
    if i == 'o':
        alphabet_dict['o'] = word_lst.index('o')
    if i == 'p':
        alphabet_dict['p'] = word_lst.index('p')
    if i == 'q':
        alphabet_dict['q'] = word_lst.index('q')
    if i == 'r':
        alphabet_dict['r'] = word_lst.index('r')
    if i == 's':
        alphabet_dict['s'] = word_lst.index('s')
    if i == 't':
        alphabet_dict['t'] = word_lst.index('t')
    if i == 'u':
        alphabet_dict['u'] = word_lst.index('u')
    if i == 'v':
        alphabet_dict['v'] = word_lst.index('v')
    if i == 'w':
        alphabet_dict['w'] = word_lst.index('w')
    if i == 'x':
        alphabet_dict['x'] = word_lst.index('x')
    if i == 'y':
        alphabet_dict['y'] = word_lst.index('y')
    if i == 'z':
        alphabet_dict['z'] = word_lst.index('z')

for i in alphabet_dict:
    print(alphabet_dict[i], end=' ')