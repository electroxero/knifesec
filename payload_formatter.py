#!/usr/bin/python
import sys


print(" _____                _           ___  ___                      ______                         _   _            ")                                                                                                                     
print("|  ___|              (_)          |  \/  |                      |  ___|                       | | | |           ")                                                                                                                     
print("| |__ _ __ ___  _ __  _ _ __ ___  | .  . | __ _  ___ _ __ ___   | |_ ___  _ __ _ __ ___   __ _| |_| |_ ___ _ __ ")                                                                                                                     
print("|  __| '_ ` _ \| '_ \| | '__/ _ \ | |\/| |/ _` |/ __| '__/ _ \  |  _/ _ \| '__| '_ ` _ \ / _` | __| __/ _ \ '__|")                                                                                                                     
print("| |__| | | | | | |_) | | | |  __/ | |  | | (_| | (__| | | (_) | | || (_) | |  | | | | | | (_| | |_| ||  __/ |   ")                                                                                                                     
print("\____/_| |_| |_| .__/|_|_|  \___| \_|  |_/\__,_|\___|_|  \___/  \_| \___/|_|  |_| |_| |_|\__,_|\__|\__\___|_|   ")                                                                                                                     
print("               | |                                                                                              ")                                                                                                                     
print("               |_|                                                                                              ")                                                                                                                     
print("\n")

print ("By @Electroxero\n \n")

print "Script Invocation : ", sys.argv[0] + "\n"

if len(sys.argv) != 3:
    print "Usage : python %s <base64_powershell> <output_string_length> \n" % (sys.argv[0])
    sys.exit(0)
print "The arguments are: " , str(sys.argv)

s = sys.argv[1]

l = int(sys.argv[2])

for x in range(0,len(s),l):

    if x == 0:
        print "HN = \"" + s[x:x + l] + "\""
    else:

        print "HN = HN + \"" + s[x:x + l] + "\""
