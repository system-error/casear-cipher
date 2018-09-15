key = 1
text = 'Hello world'
encrypted_text = ""
table = []
print(ord(' '))
for char in text:
    if char.isalpha():
        if char.islower():
            chaar = ord(char)
            aplphabet = ((ord(char) - ord('a') + key) % 26) + ord('a')
            # if aplphabet > ord('z'):
            #     aplphabet -= 26
            newletter = chr(aplphabet)
            encrypted_text += "".join(newletter)
        else:
            chaar = ord(char)
            aplphabet = ((ord(char) - ord('A') + key) % 26) + ord('A')
            # if aplphabet > ord('z'):
            #     aplphabet -= 26
            newletter = chr(aplphabet)
            encrypted_text += "".join(newletter)            
    elif char == ' ':    
       encrypted_text += "".join(char)
    # table.append(newletter)
    

print(encrypted_text)