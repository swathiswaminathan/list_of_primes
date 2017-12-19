def find_primelist(num):
    """Given a num, find the list of prime numbers"""

    if num == 1 or num == 0:
        return None

    i = 2
    while i <= num:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            print " %s is prime" % i
        i += 1

find_primelist(12)
