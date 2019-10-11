#!/usr/bin/env python3

# github.com/hasithsen
# 10-11-2019
# Decipher a substitution-ciphered message with 20 characters at most

import sys

def handle_err(msg):
  print(msg)
  sys.exit()

def decipher(cipher, offset):
  cipher_ords = [ord(i) for i in cipher]
  plain_ords = [o - offset for o in cipher_ords]
  plain_chars = [chr(i) for i in plain_ords]
  plaintext = ''.join(plain_chars)
  return plaintext

def main():
  alpha__letter_count = 26
  cipher = ""
  try:
    cipher = input()
  except:
    handle_err(0)
  
  if len(cipher) > 20:
    handle_err("error")
  
  print(decipher(cipher, 3))

if __name__ == "__main__":
  main()