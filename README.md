# Cryptography-Puzzle
Solution to the Cryptography Puzzle

First we get the encrypted message from the vaccination card using a QR Scanner.

message='R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ=='

Due to the presence of = at the end of the message we can guess it is in Base64

After Decrypting via Base64, we get

Result is :Great job. Julius Caeser was born in the 100 BC:\nPDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F\nOPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY'

we can use ceasers cipher to decrypt the message and find the key via brute force

The key is found to the 22

Result is: THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC

decoded = 'STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC'

We Get Message as RSAENCRYPTNUMBERTWOHUNDREDFOURTYTHREEWITHNVALUEASTWOTHOUSANDFOURHUNDREDANDNINETEENANDEVALUEASELEVENX

Which can be made out to be the following:
RSA Encrypt Number 243 with N value 2419 and E value 11

we can use (num**e)%n for RSA Encryption

We Get the Answer as: 1942, which we can use to unlock the safe

In the safe, we get the following message:
TM, DTZ KTZSI RJ😔. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?🤨

We can use brute force to find the key(Ceaser Cipher)
Key is found to be 5

We get the final message: OH, YOU FOUND ME😔. CONGRATS. THIS IS THE ENDGOAL. OR IS IT?🤨
Well Hopefuly its the Final Message.
