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

def sumEncry(text):
    global numbersecret
    if(text == "001"):
        convert = 1 + int(numbersecret)
    elif(text == "002"):
        convert = 2 + int(numbersecret)
    elif(text == "003"):
        convert = 3 + int(numbersecret)
    elif(text == "004"):
        convert = 4 + int(numbersecret)
    elif(text == "005"):
        convert = 5 + int(numbersecret)
    elif(text == "006"):
        convert = 6 + int(numbersecret)
    elif(text == "007"):
        convert = 7 + int(numbersecret)
    elif(text == "008"):
        convert = 8 + int(numbersecret)
    elif(text == "009"):
        convert = 9 + int(numbersecret)
    elif(text == "010"):
        convert = 10 + int(numbersecret)
    elif(text == "011"):
        convert = 11 + int(numbersecret)
    elif(text == "012"):
        convert = 12 + int(numbersecret)
    elif(text == "013"):
        convert = 13 + int(numbersecret)
    elif(text == "014"):
        convert = 14 + int(numbersecret)
    elif(text == "015"):
        convert = 15 + int(numbersecret)
    elif(text == "016"):
        convert = 16 + int(numbersecret)
    elif(text == "017"):
        convert = 17 + int(numbersecret)
    elif(text == "018"):
        convert = 18 + int(numbersecret)
    elif(text == "019"):
        convert = 19 + int(numbersecret)
    elif(text == "020"):
        convert = 20 + int(numbersecret)
    elif(text == "021"):
        convert = 21 + int(numbersecret)
    elif(text == "022"):
        convert = 22 + int(numbersecret)
    elif(text == "023"):
        convert = 23 + int(numbersecret)
    elif(text == "024"):
        convert = 24 + int(numbersecret)
    elif(text == "025"):
        convert = 25 + int(numbersecret)
    elif(text == "026"):
        convert = 26 + int(numbersecret)
    elif(text == "027"):
        convert = 27 + int(numbersecret)
    elif(text == "028"):
        convert = 28 + int(numbersecret)
    return convert

def codeToEncry(passphrase, message):
    psp = sumEncry(passphrase)
    msg = sumEncry(message)
    convert = psp + msg
    if(convert < 10):
        finalConvert = "00" + str(convert)
    else:
        finalConvert = "0" + str(convert)
    return finalConvert

def convertCodeToEncry(passphrase, message):
    i = 0
    j = 0
    convert = []
    while(i < len(message)):
        if(j < len(passphrase)):
            convert.append(codeToEncry(passphrase[j], message[i]))
            j += 1
        if(j == len(passphrase)):
            j = 0
        i += 1
    return convert

def chooseRandom(passphrase):
    randomSelect = textToCode(random.choice(string.ascii_lowercase))
    passphraseSelect = random.choice(passphrase)
    rd = sumEncry(randomSelect)
    psp = sumEncry(passphraseSelect)
    convert = rd + psp
    if(convert < 10):
        finalConvert = "00" + str(convert)
    else:
        finalConvert = "0" + str(convert)
    return finalConvert

def encryMethod(passphrase, message):
    global numbersecret
    msg = []
    maxMessage = len(message)
    count = 0
    validation = True
    while(validation):
        i = 0
        while(i < int(numbersecret)):
            msg.append(chooseRandom(passphrase))
            msg.append(chooseRandom(passphrase))
            i += 1
        i = 0
        while(i < int(numbersecret)):
            msg.append(message[0])
            element = message[0]
            message.pop(0)
            message.append(element)
            i += 1
            count += 1
            if(count == maxMessage):
                validation = False
                break
    i = 0
    while(i < int(numbersecret)):
        msg.append(chooseRandom(passphrase))
        msg.append(chooseRandom(passphrase))
        i += 1
    return msg

def sendMessage(msg):
    finalMessage = ''.join(msg)
    file = open(messageFile, "w")
    file.write(finalMessage)
    file.close()

passphrase = getFile(passphraseFile)
numbersecret = getFile(numbersecretFile)
message = input("Escriba el mensaje a enviar: ")
passphraseConvert = convertTextToCode(passphrase)
messageConvert = convertTextToCode(message)
messageEncry = convertCodeToEncry(passphraseConvert, messageConvert)
print(messageEncry)
messageFinal = encryMethod(passphraseConvert, messageEncry)
print(messageFinal)
sendMessage(messageFinal)
print("Su mensaje se ha generado correctamente, envie el archivo al destinario.")

# NUMERO SECRETO HASTA 20