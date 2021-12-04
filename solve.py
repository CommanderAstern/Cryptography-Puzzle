#First we get the encrypted message from the vaccination card using a QR Scanner.

message ='R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ=='

#decrypting using base64

#Base64 decoding from scratch

def base64_decode(message):
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res1 = ''
    res = ''
    for i in range(len(message)-2):
        temp = bin(key.find(message[i]))[2:]
        if len(temp) < 6:
            temp = '0'*(6-len(temp)) + temp
        res1 += temp
    for i in range(0,len(res1),8):
        res += chr(int(res1[i:i+8],2))
    return res
    

base64_decoded = base64_decode(message)
print(base64_decoded)

#Result is :Great job. Julius Caeser was born in the 100 BC:\nPDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F\nOPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY'

decoded = "PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F OPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY"

#we can use ceasers cipher to decrypt the message

def ceaser_decrypt(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decoded = ""
    for i in message:
        if i in alphabet:
            index = alphabet.find(i)
            new_index = (index - key) % 26
            decoded += alphabet[new_index]
        else:
            decoded += i
    return decoded

# Using Brute force to find the key
# for i in range(26):
#     print(i,ceaser_decrypt(decoded, i))

# Found the key to be 22
print(ceaser_decrypt(decoded, 22))

#Result is THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC

decoded = 'STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC'
#Using Playfair Cipher to decrypt the message

def findloc(c,matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==c:
                return i,j

def playfair(message):
    key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    res = ''
    # conver key into 5*5 matrix
    matrix = [list(key[i*5:i*5+5]) for i in range(0, len(key)//5)]
    for i in range(0, len(message), 2):
        # find location of both characters
        x1, y1 = findloc(message[i], matrix)
        x2, y2 = findloc(message[i+1], matrix)
        if x1 == x2:
            res += matrix[x1][(y1+4)%5] + matrix[x2][(y2+4)%5]
        elif y1 == y2:
            res += matrix[(x1+4)%5][y1] + matrix[(x2+4)%5][y2]
        else:
            res += matrix[x1][y2] + matrix[x2][y1]
    return res
print()
print(playfair(decoded))

# We Get Message as RSAENCRYPTNUMBERTWOHUNDREDFOURTYTHREEWITHNVALUEASTWOTHOUSANDFOURHUNDREDANDNINETEENANDEVALUEASELEVENX
# Which can be made out to be the following:
# RSA Encrypt Number 243 with N value 2419 and E value 11

def RSA(num,n,e):
    return (num**e)%n

print(RSA(243,2419,11))

# We Get the Answer as: 1942, which we can use to unlock the safe
# In the safe, we get the following message:
# TM, DTZ KTZSI RJ😔. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?🤨

decoded = 'TM, DTZ KTZSI RJ😔. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?🤨'
# Using Brute force to find the key
# for i in range(26):
#     print(i,ceaser_decrypt(decoded, i))
# Key is found to be 5
print()
print(ceaser_decrypt(decoded, 5))

# We get the final message: OH, YOU FOUND ME😔. CONGRATS. THIS IS THE ENDGOAL. OR IS IT?🤨
# Well Hopefuly its the Final Message.