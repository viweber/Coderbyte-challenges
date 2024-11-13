def FirstFactorial(num):
  fac = 1

  while(num > 0):
    fac *= num
    num -= 1

  return fac

# keep this function call here 
print(FirstFactorial(int(input())))
