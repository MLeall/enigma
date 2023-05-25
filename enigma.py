class Enigma:
    # Enigma class should have the rotors logic, encryption and decryption logic and a management method to ensure consistency.
    def __init__(self) -> None:
        self.rotors_position = [0 , 0 , 0]
        # Default mapping for rotors 1, 2, 3:
        self.rotor1_mapping = {
            'A': 'G', 'B': 'R', 'C': 'S', 'D': 'J', 'E': 'K',
            'F': 'X', 'G': 'A', 'H': 'V', 'I': 'T', 'J': 'D',
            'K': 'E', 'L': 'M', 'M': 'L', 'N': 'U', 'O': 'P',
            'P': 'F', 'Q': 'Z', 'R': 'B', 'S': 'C', 'T': 'I',
            'U': 'N', 'V': 'H', 'W': 'Y', 'X': 'Q', 'Y': 'W',
            'Z': 'O'
        }
        self.rotor2_mapping = {
            'A': 'Y', 'B': 'E', 'C': 'G', 'D': 'L', 'E': 'B',
            'F': 'U', 'G': 'C', 'H': 'P', 'I': 'T', 'J': 'Z',
            'K': 'Q', 'L': 'D', 'M': 'X', 'N': 'A', 'O': 'W',
            'P': 'H', 'Q': 'K', 'R': 'S', 'S': 'R', 'T': 'I',
            'U': 'F', 'V': 'N', 'W': 'O', 'X': 'M', 'Y': 'V',
            'Z': 'J'
        }
        self.rotor3_mapping = {
            'A': 'Z', 'B': 'C', 'C': 'B', 'D': 'O', 'E': 'P',
            'F': 'U', 'G': 'S', 'H': 'J', 'I': 'T', 'J': 'H',
            'K': 'Q', 'L': 'M', 'M': 'L', 'N': 'Y', 'O': 'D',
            'P': 'E', 'Q': 'K', 'R': 'X', 'S': 'G', 'T': 'I',
            'U': 'F', 'V': 'A', 'W': 'R', 'X': 'F', 'Y': 'N',
            'Z': 'W'
        }

    def encrypt(self, message):
        """
        Return a encrypted version of the message provided
        """
        encrypted_message = ''
        for char in encrypted_message:
            if char.upper().isalpha():
                encrypted_char = '' # method responsible for process and encrypt the char. Still need to be coded.

                encrypted_message += encrypted_char
            # else block or possible try/except block
        return encrypted_message

    def decrypt(self, message):
        """
        Return a decrypted version of the message provided
        """
        pass
    
    def __process_char(self, char):
        pass

    def __reflector_mapping_output(self, char):
        """
        Return the char after reflector mapping
        """
        try:
            if char.isalpha():
                reflector_mapping = {
                    'A': 'T', 'B': 'E', 'C': 'K', 'D': 'W', 'E': 'B', 
                    'F': 'P', 'G': 'S', 'H': 'V', 'I': 'N', 'J': 'Z',
                    'K': 'C', 'L': 'M', 'M': 'L', 'N': 'I', 'O': 'Y',
                    'P': 'F', 'Q': 'U', 'R': 'X', 'S': 'G', 'T': 'A',
                    'U': 'Q', 'V': 'H', 'W': 'D', 'X': 'R', 'Y': 'O', 
                    'Z': 'J'
                }
                return reflector_mapping[char.upper()]
            else:
                raise ValueError("Input characther must be alphabetic and non-special")
        except KeyError:
            raise ValueError(f"Character {char} cannot be mapped")
        
    def __rotate_rotor(self, mapping):
        """
        Return a new dictionary with the values one position to the right
        """
        keys = list(mapping.keys())
        values = list(mapping.values())
        rotated_values = [values[-1]] + values[:-1]
        return dict(zip(keys, rotated_values))
