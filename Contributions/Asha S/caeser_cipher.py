alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    text=''
    for char in plain_text:  
        index=(alphabets.index(char)+shift_key)%26
        text+=alphabets[index]
    print(f"Encrypted message => {text}")

def decryption(plain_text,shift_key):
    text=''
    for char in plain_text:
        index=(alphabets.index(char)-shift_key)%26
        text+=alphabets[index]
    print(f"Decrypted message => {text}")

def caeser_cipher():
    type=input("Type 'encrypt' for encryption or type 'decrypt' for decryption :\n")
    
    if type=='encrypt':
        plain_text=input('Enter the message :\n')
        shift_key=int(input("Enter shift key :\n"))
        encryption(plain_text,shift_key) 
    else:
        cipher_text=input('Enter the message :\n')
        shift_key=int(input("Enter shift key :\n"))
        decryption(cipher_text,shift_key)
caeser_cipher()
while True:
    
    user_input=input("Type 'yes' continue , 'no' to exit :\n")
    if user_input=='yes':
        caeser_cipher() 
    else:
        print('************** End ***************')
        break


    
    
    

