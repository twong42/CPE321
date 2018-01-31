
f = open("caesar_easy_2_encrypted.txt", "r")

count = [0] * 26
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
A = a[:]

for i in range (0,25):
    A[i] = A[i].upper()


s = f.read()

for x in range(1,25):
    trans = ""
    for c in s:
        if (c.isalpha()):
            if c.isupper():
                c = A[(A.index(c) + x) % 26]
            else:
                c = a[(a.index(c) + x) % 26]
        trans += c
    print ('Key #%s' % (x))
    print (trans)



