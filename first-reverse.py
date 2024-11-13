def FirstReverse(text):
  # corrigindo o valor para considerar 0 
  size = len(text)-1
  reverse = ""

  while(size >= 0):
    reverse += text[size]
    size -= 1

  return reverse

print(FirstReverse(input()))
