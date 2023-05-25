from enigma import Enigma

test_object = Enigma()
d = {
        'A': 'T', 'B': 'E', 'C': 'K', 'D': 'W', 'E': 'B', 
        'F': 'P', 'G': 'S', 'H': 'V', 'I': 'N', 'J': 'Z',
        'K': 'C', 'L': 'M', 'M': 'L', 'N': 'I', 'O': 'Y',
        'P': 'F', 'Q': 'U', 'R': 'X', 'S': 'G', 'T': 'A',
        'U': 'Q', 'V': 'H', 'W': 'D', 'X': 'R', 'Y': 'O', 
        'Z': 'J'
    }
print(d.values())
print(test_object.rotate_rotor(d).values())