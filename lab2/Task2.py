from Crypto import Random

# Replace "otp1.txt" with desired file name
s = open("otp1.txt", "r").read()

rnd = Random.get_random_bytes(len(s))

x = []
for x1,x2 in zip(s,rnd):
    x.append("{:02x}".format(ord(x1)^ord(x2)))

ret = (''.join(x)).decode("hex")

# Write to file ciphertext
open("encrypt1.txt","w").write(''.join(x))

# Verify
q = []
for x1,x2 in zip(ret,rnd):
    q.append("{:02x}".format(ord(x1) ^ ord(x2)))

orig = (''.join(q)).decode("hex")

# Uncomment to check for original message
# print (orig)







