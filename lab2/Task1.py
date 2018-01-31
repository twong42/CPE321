#Task 1

str1 = raw_input("String 1: ")
str2 = raw_input("String 2: ")

if (len(str1) != len(str2)):
    print("Strings are of different length. Exitting\n")
    exit(0)

x = []
for x1,x2 in zip(str1,str2):
    x.append("{:02x}".format(ord(x1)^ord(x2)))

print (''.join(x))