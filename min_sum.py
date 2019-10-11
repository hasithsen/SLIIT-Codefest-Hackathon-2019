#/usr/bin/env python3
  
# github.com/hasithsen
# 10-11-2019
# Sum of minimum pair
  
import sys 

def get_arr(arr, len_):
  try:
    numbers = input()
    for i in range(len_):
      #print(int(numbers.split(" ")[i].strip()), end=" ")
      arr.append(int(numbers.split(" ")[i].strip()))
  except:
    print("Sorry, an error occured")
  return arr

def main():
  arr1 = []
  arr2 = []
  len_ = int(input())
  arr1 = get_arr(arr1, len_)
  arr2 = get_arr(arr2, len_)

  sum_ = 0
  min_ = arr1[0] + arr2[0] # optimize for min_
  for i in range(len_):
    for j in range(len_):
      sum_ = arr1[i] + arr2[j] 
      if min_ > sum_:
        min_ = sum_ # update min_ value
  
  print(min_)

if __name__ == "__main__":
  main()