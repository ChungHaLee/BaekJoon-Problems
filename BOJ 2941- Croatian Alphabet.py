croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for a in croatian_alphabet:
    word = word.replace(a, '*')

print(len(word))