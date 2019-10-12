#!/usr/bin/env python3

# github.com/hasithsen
# 10-11-2019
# Decipher a substitution-ciphered message with 20 characters at most

import sys

def handle_err(msg):
  print(msg)
  sys.exit()

def decipher(cipher, offset):
  cipher_ords = [ord(i) for i in cipher] # get ords of cipher letters
  plain_ords = [o - offset for o in cipher_ords] # offset each cipher ord to get corresponding plain text ord 
  plain_chars = [chr(i) for i in plain_ords] # get letters corresponding to each plain text ord
  plaintext = ''.join(plain_chars) # create a string joining obtained plan text letters in plain_chars list
  return plaintext

def main():
  cipher = ""
  try:
    cipher = input()
  except:
    handle_err("Sorry, invalid input")

  if len(cipher) > 20:
    handle_err("error")
  
  print(decipher(cipher, 3)) # assume an offset of 3 when deciphering

if __name__ == "__main__":
  main()