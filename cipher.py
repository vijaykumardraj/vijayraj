import sys
import math
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getmode():
    print("Do you want to encrypt(e) or decrtypt(d)")
    mode = (input().lower())
    if mode in ["e", "encrypt", "d", "decrypt"]:
        return(mode)
    else:
        sys.exit("wrong input")
def getmessage():
    print("Enter your message")
    message = input()
    return (message)

def getkey():
    print("Enter key to Encrypt or Decrypt")
    key = int(input())
    return(key)
    

def encdec(mode,message,key):
    translated = ""
    if mode == "e":
        for symbol1 in message:
 #           print(symbol1)
            translated = translated + chr(ord(symbol1) + key)
    elif mode == "d":
        for symbol1 in message:
  #          print(symbol1)
            translated = translated + chr(ord(symbol1)- key)
    return (translated)
  
mode = getmode()
print(mode)
message = getmessage()
print("You entered : " + message)
key = getkey()
print(key)
translated = encdec(mode,message,key)
print("Your encrypted message: " + translated)
print("press any key to exit")
input()
