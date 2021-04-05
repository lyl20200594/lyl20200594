p = 11
q = 13
n = p * q
phi_n = (p-1) * (q-1)

e = 7
print(p, q)

d = 0
mode = 0
while True:
    d += 1
    mod = (e * d) % phi_n
    if mod == 1:
        break

# Encryption
# C = p^e mode n

plain = "Hello World"
plain_list = [ord(x) for x in plain]

ciper = []
for i in plain_list:
    x = (i ** e) % n
    ciper.append(int(x))

# Decryption
# P = C^d mode n

decryted = []
for i in ciper:
    x = (i ** d) % n
    decryted.append(int(x))

print('plaintext', plain_list)
print('cyper text', ciper)
print('decryted text', decryted)

decryted_text = ''.join([chr(x) for x in decryted])
print(decryted_text)



# lyl20200594
