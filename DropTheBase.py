import re
import base64
import os
from optparse import OptionParser

def clearscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    print " _____               _______ _          ____                  "
    print "|  __ \             |__   __| |        |  _ \                 "
    print "| |  | |_ __ ___  _ __ | |  | |__   ___| |_) | __ _ ___  ___  "
    print "| |  | | '__/ _ \| '_ \| |  | '_ \ / _ \  _ < / _` / __|/ _ \ "
    print "| |__| | | | (_) | |_) | |  | | | |  __/ |_) | (_| \__ \  __/ "
    print "|_____/|_|  \___/| .__/|_|  |_| |_|\___|____/ \__,_|___/\___| "
    print "                 | |                                          "
    print "                 |_|                                          "
    print "-----------------------------------------"
    print "/ This program recursively decodes base64 \\"
    print "| text. If there are multiple layers of   |"
    print "| encoding, each encoded instance will be |"
    print "\ printed and numbered.                   /"
    print "-----------------------------------------"
    print "        \   ^__^"
    print "         \  (oo)\_______"
    print "            (__)\       )\/\\"
    print "                ||----w |"
    print "                ||     ||"

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
                print "\t\t\t\t\t" + decString
                #print "\t\t\t\t\t*************************"
                detect(decString)

parser = OptionParser()
parser.add_option("-d", "--decode", dest="potentialBase64String",
                  help="string to search and decode", metavar="potentially encoded string")
(options, args) = parser.parse_args()

count = 1
base64regex = "(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})"

# set encString to 'None' if no argument was provided
encString = str(options.potentialBase64String)

if encString == 'None':
    clearscreen()
    encString = str(raw_input("\nPaste string to be decoded: "))

else:
    encString = options.potentialBase64String
detect(encString)
