def genPrimes():
    prime_list = []
    def find_prime(prime_list, x):
      for p in prime_list:
        if (x % p) != 0:
          pass
        else:
          return False
      return True
    for x in range(2, 100000000):
        if find_prime(prime_list, x) == True:
            yield x
            prime_list.append(x)
