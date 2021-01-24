"""Detect primitive roots of a prime module."""
import sys

from mathext import euler_phi, relative_primes, is_prime

MODULE = 99989
# MODULE = 31

if __name__ == '__main__':
    if not is_prime(MODULE):
        sys.exit()
    print('Module:', MODULE)
    print('This module has', euler_phi(MODULE - 1), 'primitive roots.')
    print('Probing the first primitive root ...')
    for a in range(2, MODULE - 1):
        print('Caandidate:', a)
        for k in range(1, MODULE - 1):
            x = pow(a, k, MODULE)
            if k < (MODULE - 1) and x == 1:
                print(a, 'is not a primitive root.')
                break
        else:
            print(a, 'is a primitive root for module', MODULE)
            pw0 = a
            break
    rp = relative_primes(MODULE - 1)
    print('The set of totients of the totient count is:', rp)
    pw = []
    for k in rp:
        pw.append(pow(pw0, k, MODULE))
    print('Primitive roots:', sorted(pw))


# last line of code
