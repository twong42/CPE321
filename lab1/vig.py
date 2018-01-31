
class Letter():
    def __init__(self, letter, f):
        self.letter = letter
        self.f = f

def shift(list, s):
    return list[s:] + list[:s]

def multAlpha(l1, l2):
    tot = 0
    for i in range(26):
        tot += l1[i].f * l2[i].f
    return tot


f = open("vigerne_medium_encrypt.txt", "r")

freq = []
expected = []
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
A = a[:]
count = 0
engl = [0.08176, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772,
        0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978,
        0.02360, 0.00150, 0.01974, 0.00074]
n = 9

for i in range (26):
    A[i] = A[i].upper()
    freq.append(Letter(a[i],0))
    expected.append((Letter(a[i],engl[i])))

s = f.read()

for i in range (n):
    count = 0
    max = 0
    spot = 0
    tot = 0

    temp = ""
    for c in s.lower():
        if c.isalpha():
            if (count - i) % n == 0:
                freq[a.index(c)].f += 1
            count += 1
    for j in range (26):
        freq[j].f = freq[j].f/ float(count)
    for j in range (26):
        tot = multAlpha(shift(freq,j),expected)
        if max < tot:
            max = tot
            spot = j
    print ('max : %s, letter : %s, %s' % (max, a[spot - 1], spot))

key = [3,1,3,20,1,3,5,1,5]

trans = ""
count = 0
for c in s:
    if (c.isalpha()):
        if c.isupper():
            c = A[(A.index(c) + (26-key[count % n]))%26]
        else:
            c = a[(a.index(c) + (26-key[count % n]))%26]
        count += 1
    trans += c

print (trans)