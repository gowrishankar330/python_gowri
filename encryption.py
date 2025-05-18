import random
import string

chars = string.punctuation + string.digits + string.ascii_lowercase 
chars = list(chars)
key = chars.copy()
random.shuffle(key)
#print(f"chars={chars}")
#print(f"keys={key}")

#encryption

text = input("enter your text: ")
cyber_text = ""
for x in text:
    if x in chars:
        index = chars.index(x)
        cyber_text = cyber_text + key[index]
    else:
        cyber_text = cyber_text + x
print(f"youe text is {text}")
print(f"your encrypted text is {cyber_text}")

#decryption

encrypted_text = input("enter your encrypted text: ")
text = ""
for x in encrypted_text:  
           index = key.index(x)
           text = text + chars[index]
print(f"your encrypted text is {encrypted_text}")
print(f"youe text is {text}")
