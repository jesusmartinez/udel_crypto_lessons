import random

# As in lesson3_part2_rsa_details.py
def is_Prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


modulus = '00a77975db01fd340ed69297aa41ecca9dda1ba0d3532058faeec3d8e4eb6ceb83e262bd0c6b0097deb6c44100bd351c524af77c5bd3ea4152362e7da4a20ef009ca3997a5423f9ce089a3eaed973dcb495ccd76dd1896603b67f893a33d95e85ea36484ce33fff91af2f3a1b7baa2a426f76ed48322eea275397cc466886174e2c1d55a7a319a80900a6d1c89e2ce842f509762d6c7c89185e0df3abc2c0a71be1e5e1030d77478359c5ca7c2357bc6e4216ee2d399e58fe5337165a50f91e084ac3126a9408b8fa31252c8c12955e51628a991339a3555bf100b0e6f00874e11b8a0188f723668a6ae92bd3c3ecd11a6f79021dbba7bf3bce16e901842df6835'
m = int(modulus, 16)
e = 65537
private_exponent = '669a44392bebcb73f7c391c58e641af24088c2ac157670ed3350ab55fc621b9c0e1b3e05189d216e21fcf47216792e63c0680539610858829c8d390e9ef695daf998f52e1afb4c0a48693369e249ca7ca4ad80500e5b3a93caac010f76909bef371d433beda1ba24e789999f2d69ad35ee4b6948fa22c7471834374335f4b71da327d3921e541bf746b09617bf303fa70b0d119fb40216075bf0b53bc94ae96d926fd1908eda7cd0615da4988d164244fdc174cc02621f71acc62f71d1b8e00392f52956cd563a3777f249e522f4a7587519a4e62eeeae5506e8b60f1fbe33d58fd73e9309f4708fa44505a198990a29c85600da1c39a799327d20930db2c1c1'
d = int(private_exponent, 16)
print('d: ', d)
prime1 = '00dd78dd7613ad2c7f4e14bb85aaec7b23fc0ee112b446dca57b9b768f4058712d66ccfd96c23c98334ffc48db59e542e58c65db14c32e285daa4aae5801a52f35c1ac6bd8ab04f42106103fc4976a83e6ed13bc58505f33feec5d8f3402690f784c17ff7c435f665a63f0d1ddacd05cc232d77f46e1ee2818b016cb526dab8f91'
p = int(prime1, 16)
print('p: ', p)
prime2 = '00c19580f0088a6defbacf3becf1c10dbc2e692bd867aedc53f5a26dbbdbfca8e6486ce3a5aa500fa1b3ac39b41010259f6a348e2265d2c702a26b8129b627cc9687dd89c71948c38678c45ce1af03a01858c127eabd065ed5757d2c8c653a44fa0c005383d1190f71d58725c33b643d91b800ab4d9000f0854d018561d3198465'
q = int(prime2, 16)
print('q: ', q)

n = p * q
print('n: ', n)
phi_of_N = (p - 1) * (q - 1)
print('phi: ', phi_of_N)

x = e * d
res = x % phi_of_N
print('n = p . q')
print('e . q = 1 mod (p -1) . (q - 1)', res)
print('Is p prime?', is_Prime(p))
print('Is 1 prime?', is_Prime(q))
