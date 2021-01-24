import pyttsx3

engine = pyttsx3.init()
file = open("penyimpanan.txt")
bacadong = file.readlines()
bacafile = bacadong
ngomong = engine.say(bacafile)
ngomong = engine.runAndWait()
print(ngomong)
