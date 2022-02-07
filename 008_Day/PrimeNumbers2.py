def prime_checker(number):
    is_prime = True
    for i in range(2,number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime number")
    else:
        print("Its not a prime number")

n = 110
# n = int(input("Check this number: "))
prime_checker(number=n)