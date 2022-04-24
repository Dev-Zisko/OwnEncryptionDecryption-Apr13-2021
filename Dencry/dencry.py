import string
import random

passphraseFile = "passphrase.txt"
numbersecretFile = "numbersecret.txt"
messageFile = "message.txt"

def getFile(fileSelected):
    file = open(fileSelected, "r")
    for line in file.readlines():
        data = line
    file.close()
    return data

def textToCode(char):
    if(char == "a"):
        return "001"
    elif(char == "b"):
        return "002"
    elif(char == "c"):
        return "003"
    elif(char == "d"):
        return "004"
    elif(char == "e"):
        return "005"
    elif(char == "f"):
        return "006"
    elif(char == "g"):
        return "007"
    elif(char == "h"):
        return "008"
    elif(char == "i"):
        return "009"
    elif(char == "j"):
        return "010"
    elif(char == "k"):
        return "011"
    elif(char == "l"):
        return "012"
    elif(char == "m"):
        return "013"
    elif(char == "n"):
        return "014"
    elif(char == "ñ"):
        return "015"
    elif(char == "o"):
        return "016"
    elif(char == "p"):
        return "017"
    elif(char == "q"):
        return "018"
    elif(char == "r"):
        return "019"
    elif(char == "s"):
        return "020"
    elif(char == "t"):
        return "021"
    elif(char == "u"):
        return "022"
    elif(char == "v"):
        return "023"
    elif(char == "w"):
        return "024"
    elif(char == "x"):
        return "025"
    elif(char == "y"):
        return "026"
    elif(char == "z"):
        return "027"
    elif(char == " "):
        return "028"

def convertTextToCode(text):
    i = 0
    convert = []
    while(i < len(text)):
        convert.append(textToCode(text[i]))
        i += 1
    return convert

def convertMessageToArray(message, numbersecret):
    i = 0
    count = 0
    convert = []
    cut = ""
    while(i < len(message)):
        if(count < 3):
            cut = cut + message[i]
            count += 1
        if(count == 3):
            convert.append(cut)
            cut = ""
            count = 0
        i += 1
    ns = int(numbersecret) * 2
    i = ns
    state = True
    msg = []
    count = 0
    while(i < len(convert)):
        if(state):
            msg.append(convert[i])
            count += 1
            if(count == int(numbersecret)):
                state = False
                count = 0
        else:
            count += 1
            if(count == ns):
                state = True
                count = 0
        i += 1
    return msg

def codeToText(char):
    if(char == "001"):
        return "a"
    elif(char == "002"):
        return "b"
    elif(char == "003"):
        return "c"
    elif(char == "004"):
        return "d"
    elif(char == "005"):
        return "e"
    elif(char == "006"):
        return "f"
    elif(char == "007"):
        return "g"
    elif(char == "008"):
        return "h"
    elif(char == "009"):
        return "i"
    elif(char == "010"):
        return "j"
    elif(char == "011"):
        return "k"
    elif(char == "012"):
        return "l"
    elif(char == "013"):
        return "m"
    elif(char == "014"):
        return "n"
    elif(char == "015"):
        return "ñ"
    elif(char == "016"):
        return "o"
    elif(char == "017"):
        return "p"
    elif(char == "018"):
        return "q"
    elif(char == "019"):
        return "r"
    elif(char == "020"):
        return "s"
    elif(char == "021"):
        return "t"
    elif(char == "022"):
        return "u"
    elif(char == "023"):
        return "v"
    elif(char == "024"):
        return "w"
    elif(char == "025"):
        return "x"
    elif(char == "026"):
        return "y"
    elif(char == "027"):
        return "z"
    elif(char == "028"):
        return " "

def dencryMethod(passphrase, message):
    global numbersecret
    i = 0
    msg = []
    psp = []
    while(i < len(message)):
        number = ""
        if(message[i][0] == "0"):
            pass
        else:
            number = number + message[i][0]
        if(message[i][1] == "0"):
            number = number + message[i][2]
        else:
            number = number + message[i][1] + message[i][2]
        msg.append(number)
        i += 1
    i = 0
    while(i < len(passphrase)):
        number = ""
        if(passphrase[i][0] == "0"):
            pass
        else:
            number = number + passphrase[i][0]
        if(passphrase[i][1] == "0"):
            number = number + passphrase[i][2]
        else:
            number = number + passphrase[i][1] + passphrase[i][2]
        psp.append(number)
        i += 1
    i = 0
    j = 0
    convert = []
    while(i < len(msg)):
        if(j < len(psp)):
            convert.append(int(msg[i]) - int(psp[j]) - int(numbersecret) - int(numbersecret))
            j += 1
        if(j == len(psp)):
            j = 0
        i += 1
    i = 0
    finalConvert = []
    while(i < len(convert)):
        if(int(convert[i]) < 10):
            finalConvert.append("00" + str(convert[i]))
        else:
            finalConvert.append("0" + str(convert[i]))
        i += 1
    i = 0
    msgDecry = ""
    while(i < len(finalConvert)):
        msgDecry = msgDecry + str(codeToText(finalConvert[i]))
        i += 1
    return msgDecry

passphrase = getFile(passphraseFile)
numbersecret = getFile(numbersecretFile)
messageSecret = getFile(messageFile)
passphraseConvert = convertTextToCode(passphrase)
messageArray = convertMessageToArray(messageSecret, numbersecret)
messageFinal = dencryMethod(passphraseConvert, messageArray)
print(messageFinal)