from nsa import PhotoPlay

from java.io import *

key = "0123456789abcdef"
plainText = "This is test text"

def encrypt(plainText, key):
  return planText
  
def decrypt(cipherText, Key):
  return cipherText
  
def main():
  print "calling main" 
  print "plain:",plainText
  cipher = encrypt(plainText,key)
  print "cipher:",cipher

  decrypted = decrypt(cipher, key)
  print "decrypt:",decrypted
  

if __name__ == '__main__':
  main()



