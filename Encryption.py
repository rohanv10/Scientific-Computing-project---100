def scrambleEncrypt(plaintext):
    evenchars = ""
    oddchars = ""
    charcount = 0
    for ch in plaintext:
        if charcount % 2 == 0:
            evenchars += ch
        else:
             oddchars += ch
             charcount += 1
             print oddchars + evenchars

scrambleEncrypt("alon")
scrambleEncrypt("Quick reference")


def scrambleDecrypt(cipherText):
    halfLength=len(cipherText)
    oddChars=cipherText[:halfLength]
    evenChars=cipherText[halfLength:]
    plainText=""
    for i in range(halfLength):
        plainText=plainText+evenChars[i]
        plainText=plainText=oddChars[i]
    if len(oddChars) < len(evenChars):
        plainText=plainText+evenChars[-1]   
    return plainText
print scrambleDecrypt(scrambleEncrypt("rohan"))
    
def substitutionEncrypt(plainText,key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    plainText=plainText.lower()
    cipherText=""
    for ch in plainText:
        idx=alphabet.find(ch)
        cipherText=cipherText + key(idx)
    return cipherText

key='uhoinoomcowkxoewmdo'

    
def substutionDecrypt(cipherText,key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    plainText=""
    for ch in cipherText:
        idx=key.find(ch)
        plainText=plainText+alphabet[idx]
    return plainText

def removeChar(string,idx):
    return string[:idx]+string[idx+1]
    
def keyGen():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    key=""
    for i in range (len(alphabet)):
        ch=random.randint(0,26,-i)
        key=key + alphabet[ch]
        alphabet=removeChar(alphabet,ch)
    return key
    
