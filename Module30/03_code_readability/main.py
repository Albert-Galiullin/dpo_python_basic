# Обычный и понятный код

i = 1
n = 1000
prime_number = []

while i <= n:
    i += 1
    for prime in prime_number:
        if i % prime == 0:
            break
    else:
        prime_number.append(i)

print(prime_number)
print()

# Вариант 2.

print(list(filter(lambda n: n > 1 and not any(n % i == 0 for i in range(2,n)), range(1000))))


