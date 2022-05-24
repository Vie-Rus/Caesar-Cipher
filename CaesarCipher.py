# Caesar Cipher - May 24, 2022
# Written by V I E R U S
# Caesar Cipher will encrypt and decrypt your inputted message if its in all caps
#--------------------------------------------------------------------------------------------------------------------
#Class Caesar Cipher
class CaesarCipher:

    def __init__(self, shift=3):                                #Def Init with parameters of self and shift default to 3
        encoder = [None] *26                                    #Tempory array for encryption
        decoder = [None] *26                                    #Tempory array for decryption
        for k in range(26):                                     #In range of the capital alphabet (26 Letters)
            encoder[k] = chr((k + shift) % 26 + ord('A'))       #Encoder
            decoder[k] = chr((k - shift) % 26 + ord('A'))       #Decoder
        self._forward = ''.join(encoder)                    
        self._backward = ''.join(decoder)                   

    def encrypt(self, EncryptMessage):
        return self._transform(EncryptMessage, self._forward)   #Calls on init self.forward to encrypt your message

    def decrypt(self, DecryptMessage):
        return self._transform(DecryptMessage, self._backward)  #Calls on init self backward to decrypt your message

    def _transform(self, original, code):
        message = list(original)
        for k in range(len(message)):
            if message[k].isupper():                            #If your message is upper case then the program will continue
                j = ord(message[k]) - ord('A')                  #Index from 0 to 25, to count all letters in the alphabet
                message[k] = code[j]                            #This will replace the character in your message
        return ''.join(message)

#Main
if __name__ == '__main__' :
    cipShift = CaesarCipher()                                  #Cipher will shift the amount of times you enter in the parameters, if not it will shift to 3 by default
    userMessage= input("Enter your message in all caps to be encrypted: ")
    enMessage = cipShift.encrypt(userMessage)
    print('Encrypted your message is: ', enMessage)
    deMessage = cipShift.decrypt(enMessage)
    print('Decrypted your message is: ', deMessage)