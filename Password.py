#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac
import hashlib
import secret


class Password:
    def encrypt_password(self,password_string,salt)
        salted_pass=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,10000).hex()
        return salted_pass
    

    def hash_check(self, cleartext_password, salted_pass,salt):
        pasword_enc=encrypt_password(cleartext_password,salt)
        if (hmac.compare_digest(salted_pass,encrypt_password):
            print("Yes")
        else:
            print("No")    
            
    #def pass_salting(num_length=8):
        #return secret.token_bytes(num_length)
   
    #def password_encoding(password_string):
        #enc_password= password_string.encode('utf-8')
        #return enc_password
    
    
    

#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes
#def hash_password(self, password_string):
        #hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        #return hashed_password
