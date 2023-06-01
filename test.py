from enigma import Enigma

test_object = Enigma()
print()
a = test_object.encrypt('Bem vinde a criptografia')
print(f'CRIPTOGRAFADO: {a}')


b = test_object.decrypt(a)
print(f'DESCRIPTOGRAFADO: {b}')