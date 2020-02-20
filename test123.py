def digits(n):
  count = 0
  while n > 0:
    count += 1
    n // 10
  print(count)

digits(25) 