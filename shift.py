def rot13(cipherlist):
    for x in cipherlist:
        # skim2.append(chr(97+x-1))
        print(chr(97 + 13 + x - 1), end="")
        # print(97+x-1)


def shift(cipherlist):
    for x in cipherlist:
        print(chr(97 + x - 1), end="")


def caeser(cipherlist):
    for y in range(26):
        print()
        for x in cipherlist:
            print(chr(97 + (y + ord(x)) % 26), end="")


skim = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
cipherstring = "gvswwmrkxlivyfmgsrhvbcxzyz"
caeser(cipherstring)
# shift(skim)
