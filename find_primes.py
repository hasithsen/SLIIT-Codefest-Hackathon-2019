#/usr/bin/env python3

# github.com/hasithsen
# 10-11-2019
# Find prime numbers in a given range

count = 0
lower = []
higher = []

try:
  count = int(input()) # "Please enter number of ranges: "
except ValueError:
  print("Sorry, only integers are accepted.")
except:
  print("Sorry, an error occured.")

for i in range(count):
  try:
    l, h = input().split() # "Please enter lower and upper limits : "
    lower.append(int(l))
    higher.append(int(h))
  except ValueError:
    print("Sorry only integers are accepted.")
  except:
    print("Sorry, an error occured.")


for i in range(count):
  prime_count = 0
  for num in range(lower[i],higher[i] + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
           prime_count += 1 
  print(prime_count)