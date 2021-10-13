from os import system as cmd

f = open("path.txt", "a+")
f.seek(0)

if f.read() == "":
    f.write(input("Example: C:\Program Files(x86)\Origin\n'Origin.exe' file path : "))

f.seek(0)
path = f.read()

f.close()

cmd(f"{path}\Origin.exe /StartOffline")