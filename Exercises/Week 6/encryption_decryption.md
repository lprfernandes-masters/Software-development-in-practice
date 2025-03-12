https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

# To encrypt and decrypt a message/file:

1. Import fernet from cryptography

   from cryptography.fernet import Fernet

2. Generate a key and write it to a file

   def write_key():

   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
   key_file.write(key)

3. Create a method to read the key and load it

   def write_key():
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
   key_file.write(key)

4. Encode a string to bytes

   message = "some secret message".encode()

5. Initialize the fernet class with the key

   f = Fernet(key)

6. Encrypt the message

   encrypted = f.encrypt(message)

7. Decrypt the message

   decrypted_message = f.decrypt(encrypted)
