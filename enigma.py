class Enigma:
    # Enigma class should have the rotors logic, encryption and decryption logic and a management method to ensure consistency.
    def __init__(self) -> None:
        self.rotor_counter = 0
        self.decrypt_counter = 0
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
           
    def __rotate_rotor(self, mapping):
        """
        Return a new dictionary with the values one position to the right
        """
        keys = list(mapping.keys())
        values = list(mapping.values())
        rotated_values = [values[-1]] + values[:-1]
        return dict(zip(keys, rotated_values))
    
    def __reverse_rotate_rotor(self, mapping):
        keys = list(mapping.keys())
        values = list(mapping.values())
        rotated_values = values[1:] + [values[0]]
        return dict(zip(keys, rotated_values))

    def encrypt(self, message):
        """
        Return a encrypted version of the message provided
        """
        encrypted_message = ''
        for char in message:
            try:
                if char.isalpha():
                    encrypted_char = self.__encrypt_char(char.upper())
                    encrypted_message += encrypted_char
            except Exception:
                print(f'Input character must be alphabetic and non-special')
                return None
        return encrypted_message

    def __encrypt_char(self, char):
        """
        Encrypts a single character using the Enigma rotors
        """
        char = char.upper()
        
        mapped_char1 = self.rotor1_mapping[char]

        if self.rotor_counter >= 26:
            if self.rotor_counter >= 52:
                self.rotor1_mapping = self.__rotate_rotor(self.rotor1_mapping)
                self.rotor1_mapping = self.__rotate_rotor(self.rotor1_mapping)
                self.rotor1_mapping = self.__rotate_rotor(self.rotor1_mapping)
                
                mapped_char2 = self.rotor1_mapping[mapped_char1]
                self.rotor2_mapping = self.__rotate_rotor(self.rotor2_mapping)
                self.rotor2_mapping = self.__rotate_rotor(self.rotor2_mapping)

                mapped_char3 = self.rotor1_mapping[mapped_char2]
                self.rotor3_mapping = self.__rotate_rotor(self.rotor3_mapping)
                self.rotor_counter += 1    
            else:
                self.rotor1_mapping = self.__rotate_rotor(self.rotor1_mapping)
                self.rotor1_mapping = self.__rotate_rotor(self.rotor1_mapping)

                mapped_char2 = self.rotor1_mapping[mapped_char1]
                self.rotor2_mapping = self.__rotate_rotor(self.rotor2_mapping)

                mapped_char3 = self.rotor1_mapping[mapped_char2]
                self.rotor_counter += 1
        else:
            self.rotor1_mapping = self.__rotate_rotor(self.rotor1_mapping)
            mapped_char2 = self.rotor2_mapping[mapped_char1]
            mapped_char3 = self.rotor3_mapping[mapped_char2]
            self.rotor_counter += 1
    
        mapped_char = self.__reflector_mapping_output(mapped_char3)
        return mapped_char

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
                raise ValueError("Input character must be alphabetic and non-special")
        except KeyError:
            raise ValueError(f"Character {char} cannot be mapped")

    def __revesed_string(self, message):
        message = list(reversed(message))
        reversed_string = ''
        for char in message:
            reversed_string += char
        return reversed_string

    def decrypt(self, message):
        """
        Return the decrypted version of the message provided
        """
        message = self.__revesed_string(message)
        decrypted_message = ''
        for char in message:
            try:
                if char.isalpha():
                    decrypted_char = self.__decrypt_char(char.upper())
                    decrypted_message += decrypted_char
            except Exception:
                print(f'Input character must be alphabetic and non-special')
                return None
        return self.__revesed_string(decrypted_message)

    def __decrypt_char(self, char):
        """
        Decrypts a single character using the Enigma rotors
        """
        self.decrypt_counter = self.rotor_counter

        mapped_char3 = self.__reflector_mapping_output(char)

        if self.rotor_counter >= 26:
            if self.rotor_counter >= 52:
                self.rotor3_mapping = self.__reverse_rotate_rotor(self.rotor3_mapping)
                mapped_char2 = self.rotor3_mapping[mapped_char3]
                self.rotor2_mapping = self.__reverse_rotate_rotor(self.rotor2_mapping)
                mapped_char1 = self.rotor2_mapping[mapped_char2]
                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                mapped_char = self.rotor1_mapping[mapped_char1]
                self.decrypt_counter -= 1    
            else:
                mapped_char2 = self.rotor3_mapping[mapped_char3]
                self.rotor2_mapping = self.__reverse_rotate_rotor(self.rotor2_mapping)
                mapped_char1 = self.rotor2_mapping[mapped_char2]
                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                mapped_char = self.rotor1_mapping[mapped_char1]
                self.decrypt_counter -= 1
        else:
            mapped_char2 = self.rotor3_mapping[mapped_char3]
            mapped_char1 = self.rotor2_mapping[mapped_char2]
            self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
            mapped_char = self.rotor1_mapping[mapped_char1]
            self.decrypt_counter -= 1

        return mapped_char
