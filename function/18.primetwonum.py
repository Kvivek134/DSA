#write a funtion to returen all  prime numbers between two numbers
def prime_numbers_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(prime_numbers_between(10, 20))