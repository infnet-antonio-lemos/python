primes = []
tentative = 1
while len(primes) < 10:
  divisores = set()
  for i in range(1, tentative):
    if (tentative % i == 0):
      divisores.add(i)
  if (len(divisores) == 1):
    primes.append(tentative)
  tentative+=1
  
print(primes)