from Crypto import Random

# Replace "otp1.txt" with desired file name
s = open("cp-logo.bmp", "r").read()

rnd = Random.get_random_bytes(len(s))

x = []
for x1,x2 in zip(s,rnd):
    temp = "{:02x}".format(ord(x1)^ord(x2))
    print (temp)
    x.append(temp.decode("hex"))



# print (''.join(x))




