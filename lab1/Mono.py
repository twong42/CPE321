
class Letter():
    def __init__(self, letter, f):
        self.letter = letter
        self.f = f

f = open("mono_easy_encrypt.txt", "r")

freq = []
expected = []
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
A = a[:]
count = 0
engl = [0.08176, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772,
        0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978,
        0.02360, 0.00150, 0.01974, 0.00074]
chi = 0

for i in range (26):
    A[i] = A[i].upper()
    freq.append(Letter(a[i],0))
    expected.append((Letter(a[i],0)))

s = f.read()

for c in s.lower():
    if c.isalpha():
        freq[(a.index(c))].f += 1
        count += 1
for i in range (26):
    expected[i].f = engl[i] * count

freq.sort(key=lambda letter:letter.f, reverse=True)
expected.sort(key=lambda letter:letter.f, reverse=True)

for i in range (26):
    print ('%s, %s' % (freq[i].letter, freq[i].f))
    print('expected %s, %s' % (expected[i].letter, expected[i].f))

key = ["*"] * 26
key[a.index("x")] = "e"
key[a.index("a")] = "t"
key[a.index("h")] = "h"
key[a.index("v")] = "a"
key[a.index("c")] = "o"
key[a.index("y")] = "s"
key[a.index("s")] = "i"
key[a.index("j")] = "n"
key[a.index("d")] = "r"
key[a.index("e")] = "d"
key[a.index("i")] = "b"
key[a.index("g")] = "l"
key[a.index("f")] = "m"
key[a.index("o")] = "w"
key[a.index("p")] = "g"
key[a.index("r")] = "u"
key[a.index("m")] = "c"
key[a.index("u")] = "y"
key[a.index("b")] = "f"
key[a.index("t")] = "j"
key[a.index("w")] = "k"
key[a.index("n")] = "v"
key[a.index("l")] = "p"
key[a.index("z")] = "x"


trans = ""
for c in s:
    if (c.isalpha()):
        if c.isupper():
            c = key[A.index(c)].upper()
        else:
            c = key[a.index(c)]
    trans += c
print (trans)