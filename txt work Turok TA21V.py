a = open("/Users/turok/Documents/School coding/TA-21V_Turok/a.txt", "r").read()
print(a)
b = open("/Users/turok/Documents/School coding/TA-21V_Turok/b.txt", "r").read()
print(b)


c = (int(a)+int(b))
print(c)
f = open("/Users/turok/Documents/School coding/TA-21V_Turok/tulemus.txt", "w")
f.write(str(c))
f.close()


def writeToMiljon2r(a):
    f = open("/Users/turok/Documents/School coding/TA-21V_Turok/miljon2r.txt", "w")
    f.write(a)
    f.close()


if c < 1000000:
    writeToMiljon2r("Tulemus is smaller than a million")

else:
    writeToMiljon2r("Tulemus is bigger than a million")

if c < 20:
    for x in range(c):
        print("Tere!")
if c > 20:
    print("Tulemus is bigger than 20")

if c == 20:
    print("Tulemus equals 20")





