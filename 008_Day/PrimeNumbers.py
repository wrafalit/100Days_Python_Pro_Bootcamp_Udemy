def prime_checker(number):
    for i in range(2,number):
        if number % i == 0:
            print('Its not a prime number')
            break
    else:
        print("Its prime number")

n = 110
# n = int(input("Check this number: "))
prime_checker(number=n)