#!/usr/bin/env python3

# github.com/hasithsen
# 10-11-2019
# Find isolated nodes in a path

import sys

def handle_err(i):
  if i == 1:
    print("Sorry, only integers are accepted")
  else:
    print("Sorry, an error occured")
  sys.exit()

def main():
  try:
    j_count = int(input())
    if j_count > 10:
      handle_err(0)
  except ValueError:
    handle_err(1)
  except:
    handle_err(0)
  
  j_unsafe = []
  for i in range(j_count):
    try:
      j_info = input() # line of input
      node = j_info.split(" ")[0]
      connections = j_info.split(" ")[1] # connected nodes list
      # check node isolation
      conn_count = len(connections.split(","))
      if (conn_count) == 1:
        j_unsafe.append(node)
    except:
      handle_err(0)
  
  if len(j_unsafe) == 0:
    print("none")
  else:
    print(",".join([str(j) for j in j_unsafe]))
    
if __name__ == "__main__":
  main()