# PubCrypt: python librairy about public key cryptography

DISCLAIMER: This librairy isn't cryptographically secure and do NOT provide a real secure key pair generator.

## 📢 Update:

Features:
- function for generating public and privet key
- primitive function: encryption, decryption, signature and signature checking
- recovery prime factors from the public and privet key

In-coming:
- pkcs scheme encryption/decryption/signature
- file format PEM
- aks primality test
- and after maybe more modules

## 📄 Documentation

rsa:
- generate(nBits, e=65537)
- primitive_exp(m, exp, n)
- prime_recovery(n, e, d)

primality:
- get_prime_factors(pBits, e)
- miller_rabin(w, wLen, r)

util:
- invmod(z, a): modular inverse
- gcd(x,y): great common divisor
- lcm(x, y): less common multiple
- pair_wise_consistency_test(n, e, d)
- isqrt(x): square root
- perfect_square(c): check if the number is a perfect square (a number of the form: x**2)
- RBG: Random Bytes Generator
- RNG: Random Number Generator
- int_to_bytes(x: int): converting an integer to a byre string
- bytes_to_int(xbytes: bytes): converting a byte string to an integer


## 🔗 Author
Find me on:
- [Twitter](https://twitter.com/Bl4om_Archie)
- [Reddit](https://www.reddit.com/user/archie_bloom)
- [Discord server](https://discord.gg/D2wGP62)


## 📜 Acknowledgements

 - [NIST FIPS 186-4: Digital Signature Standard (DSS)](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.186-4.pdf)
 - [NIST SP 800-56Br2: Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf)
 - [PKCS #1 Version 2.2: RSA Cryptography Specifications draft-moriarty-pkcs1-01](https://datatracker.ietf.org/doc/pdf/draft-moriarty-pkcs1-01.pdf)
 - [RosettaCode](https://rosettacode.org/wiki/Rosetta_Code)
