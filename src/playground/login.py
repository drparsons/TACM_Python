""""
Password encrypt check
Does not decrypt
"""

#passlib has a pure python hash function which is great is OS doesn't support

import os
from passlib.context import CryptContext

 
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    #passlib default handles rounds and salts; we're overriding for more control and uniqueness
    pbkdf2_sha256__default_rounds=300000,
    pbkdf2_sha256__salt_size = 32
    )

 

#pwd_context.to_dict() #one way to save config
cfg = pwd_context.to_string() #INI style string for text file saving/edit
print(cfg) 

#Load back from string
#pwd_context = CryptContext.from_string(cfg)
#Load from ini file
#pwd_context = CryptContext.from_path("/some/path/on/local/system")
#Load() and Load_path() can overwite to replace existing state

 
#oracle10 hash requires user
from passlib.hash import pbkdf2_sha256
#This is very good method, if someone try to decode brute force they'd need both salt and rounds

mySalt = os.urandom(32)
myRounds = 300000
custom_pbkdf2 = pbkdf2_sha256.using(salt=mySalt, rounds=myRounds)
custom=(custom_pbkdf2.hash("password"))

"""

Below proves that doesn't matter which of the 3 methods you do
they call all verify each other. Only difference is how long 
it takes to encrypt (and how hard for hackers to decrypt)

"""

print('Custom PBKDF2')
print(custom)
print(custom_pbkdf2.verify("password", custom))
print(custom_pbkdf2.verify("password","$pbkdf2-sha256$300000$6fYeo6wr9wrM6.bTWX7494tpXRJ6.opg51Wly5hE91o$dwFAjcTnaYu1ia4QvcfIqErtyyiCITeJ7WujtUUeB8Q"))
print(custom_pbkdf2.verify("password","$pbkdf2-sha256$300000$xKQtGEYg0OZNF1vowlM2dmPOvKHbzl1hPvwS3rfC35k$rI1iCI0y9znFnMJ7HgGzdMl0Nh5ULcEhp1maipNMCRc"))
print(' ')
normal = pbkdf2_sha256.hash("password")
print('Default')
print(normal)
print(pbkdf2_sha256.verify("password", normal))
print(' ')
print('Normal checking custom')
print(pbkdf2_sha256.verify("password", custom))
custom2 = pwd_context.hash("password")
print(custom)
print(pwd_context.verify("password", custom2))
print(custom_pbkdf2.verify("password", custom2))
print(pbkdf2_sha256.verify("password", custom2))
print(pwd_context.verify("password", custom))
print(pwd_context.verify("password", normal))
print(pwd_context.verify("password", '$pbkdf2-sha256$29000$90SIdAUhVTrmwdwZlxn3bq2Jp.axfCZ.WZwAP/olfQk$xzsC.haiaSAChjdBnQ.bCOmcsHovfX2jw/Ku4hnfY0k'))


"""
ENCRYPT and DECRYPT METHOD
"""

import rsa
#fernet works similar but it's one key vs a public private key
#   from cryptography.fernet import Fernet
#   key = Fernet.generate_key()
#   fernet = Fernet(key)
#   encMessage = fernet.encrypt(message.encode())

 
# generate public and private keys with 
# rsa.newkeys method,this method accepts 
# key length as its parameter
# key length should be atleast 16

publicKey, privateKey = rsa.newkeys(512)
print(publicKey) #public key to encrypt, can be shared
print(privateKey) #private key to decrypt, private

 
# this is the string that we will be encrypting
message = "hello geeks"

  
# rsa.encrypt method is used to encrypt 
# string with public key string should be 
# encode to byte string before encryption 
# with encode method

encMessage = rsa.encrypt(message.encode(), 
                         publicKey)

  
print("original string: ", message)
print("encrypted string: ", encMessage)
  

# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

  
print("decrypted string: ", decMessage)