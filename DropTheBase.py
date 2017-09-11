import re
import base64
import os

def clearscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def detect(encString):
    suspect = re.findall(base64regex, encString)
    decode(suspect)
def decode(suspect):
    for i in suspect:
        global count
        decString=base64.b64decode(i)
        if all(ord(char) < 128 for char in decString):
            if len(decString) > 3:
                print "\n\t\t\t\t\tBase64 encoded instance " + str(count)
                print "\t\t\t\t\t*************************"
                count+=1
                print decString
                print "\t\t\t\t\t*************************"
                detect(decString)
#            else:
#                print "\n\t\t\t\t\tBase64 encoded instance " + str(count)
#                print "\t\t\t\t\t*************************"
#                print decString

clearscreen()

print " _____               _______ _          ____                  "
print "|  __ \             |__   __| |        |  _ \                 "
print "| |  | |_ __ ___  _ __ | |  | |__   ___| |_) | __ _ ___  ___  "
print "| |  | | '__/ _ \| '_ \| |  | '_ \ / _ \  _ < / _` / __|/ _ \ "
print "| |__| | | | (_) | |_) | |  | | | |  __/ |_) | (_| \__ \  __/ "
print "|_____/|_|  \___/| .__/|_|  |_| |_|\___|____/ \__,_|___/\___| "
print "                 | |                                          "
print "                 |_|                                          "


os.system('cowsay This program recursively decodes base64 text. If there are multiple layers of encoding, each encoded instance will be printed and numbered.')

while True:
    count = 1
    base64regex = "(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})"
    encString = str(raw_input("\nPaste string to be decoded: "))
    detect(encString)


