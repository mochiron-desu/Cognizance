f_ini = open("onelinefile.txt", "r")
f_tar = open("Filename2.csv", "w")

inp = f_ini.read()
z = 0
i = 0

while i < len(inp):
    text = ""
    while inp[i].isdigit():
        i += 1
    else:
        text = text + inp[z:i] + ","
        z = i
    while inp[i].isalpha():
        i += 1
    else:
        text = text + inp[z:i] + ","
        z = i
    while not inp[i].isalpha():
        i += 1
    else:
        text = text + inp[z:i] + ","
        z = i
    while i < len(inp) and inp[i].isalpha():
        i += 1
    else:
        text = text + inp[z:i]
        z = i
    f_tar.write(text)
    f_tar.write("\n")
