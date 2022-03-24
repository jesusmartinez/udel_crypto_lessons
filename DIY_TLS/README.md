Module 5 and 6: DIY TLS

1) Created file alice.py and bob.py
2) Run alice.py to verify results
3) Alice generates ECC curve and signs it with RSA DS. Alice generates public and private keys
4) Bob validates ECC curve. Bob generates public and private keys
5) Alice and Bob share secret key
6) Alice encrypts and sends file 'quotesOrig.txt' to Bob using AES GCM mode
7) Bob decrypts file and saves it with a new timestamp