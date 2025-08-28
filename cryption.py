#so this file will contain my reusable Function for my dashboard
#why Function? So that other files can import and call it, so as to get the decrypted rows back as data, not just printing them.



from cryptography.fernet import Fernet      #the cyrptography module gives simple, strong symmeric encryption (same key to encrypt and decrypt)
import os           #Checks if a file exists in operating system



def decrypt_log(filepath, key_path):
#this Fuction will decrypt an encrypted log file and return  a list of dictionaries.
# a dictionary look like - {"timestamp": "blabla", "status": "bla"}


#this conditionals will check if files exist in the os
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Log file not found: {filepath}")
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"key file not found: {key_path}")
    
#this will load the encryption key
    with open(key_path, "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)        #this Fernet() object is from the cryptography library - the "key" is subjected to the "Fernet" functions which is either encrypt or decrypt
    rows = []

#this will open the log_file
    with open(filepath, "rb") as log_file:

        #list out each log entries
        for i, line_of_log in enumerate(log_file, start=1):
            #this will strip off spaces 
            line_of_log = line_of_log.strip()
            #print(repr(line_of_log)) 
                
            if not line_of_log:
                continue
            try: 
                #this will decrpt the log entries
                decrypted = fernet.decrypt(line_of_log).decode() 
                info, status, time = decrypted.split(" ", 2)
                rows.append({"info": info, "status": status, "timestamp": time})

            
            except Exception:
               rows.append({"timestamp": None, "status": "[DECRYPTION FAILED]"})
               # continue

    return rows


if __name__ == "__main__":
    result = decrypt_log("login_log_encrypt.txt", "secret.key")
    for row in result:
        print(row)



     