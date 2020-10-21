# Elliptic Curve Diffie-Hellman
It is a key-exchange system and is a variant of the Diffie-Hellman protocol. It uses elliptic curve cryptography.

## Working

Consider two parties Alice and Bob who want to share a secret with each other. They use the elliptic curve given by x<sup>3</sup> + ax + b mod p. 
Alice sends Bob her public key: N<sub>alice</sub> * P, where N<sub>alice</sub> is an integer(which should be very large for good reasons) and is Alice's private key and P is a point on the curve above.
Bob also sends his public key :N<sub>bob</sub> * P, to Alice.

Bob, upon receiving Alice's public key, calculates the shared key or secret by multiplying his private key to it. Hence the shared secret is N<sub>bob</sub>*(N<sub>alice</sub> * P).
Similarly, Alice calculates the shared secret : N<sub>alice</sub>*(N<sub>bob</sub> * P)

It can be seen easily that the two calculated shared secrets are the same.

### Security:
The system makes use of the fact that it is very hard to solve the elliptic curve discrete logarithm problem. That is, given a point (x*P) and the point P, both on an elliptic curve. It is hard to retrieve x.

## Attacks
There are many attacks on this protocol which exploit some aspects. For example, the choice of the elliptic curve parameters is very important,along with the private keys.
Private keys must obviously be large else they are easily susceptible to brute forcing. In addition, the curve must be chosen such that an attacker Eve is not able to recover either parties' private keys by calculating a discrete logarithm as shown below:

```
from sage.all import *
E = EllipticCurve(GF(9739), [479, 1768]) # Elliptic curve defined by the equation: x^3 + 479x + 1768 mod 9739
G = E.gens()[0] # Say this is the point P.
P = 7 * G # Just for example purposes, we've chosen one of the private keys as 7. It is much much larger in practical cases.
print(discrete_log(P, G, G.order(), operation = '+'))
```
       
