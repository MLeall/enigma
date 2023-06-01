class Enigma:
    # Enigma class should have the rotors logic, encryption and decryption logic and a management method to ensure consistency.
    def __init__(self) -> None:
        self.rotor_counter = 0
        self.decrypt_counter = 0
        # Default mapping for rotors 1, 2, 3:
        self.rotor1_mapping = {
            'O': 'S', 'H': 'V', 'E': 'R', 'Y': 'U', 'V': 'H', 'K': 'A', 'P': 'N', 
            'L': 'B', 'M': 'G', 'X': 'J', 'W': 'D', 'U': 'Y', 'T': 'F', 'Q': 'Z', 
            'I': 'C', 'B': 'L', 'S': 'O', 'J': 'X', 'Z': 'Q', 'F': 'T', 'A': 'K', 
            'N': 'P', 'C': 'I', 'G': 'M', 'D': 'W', 'R': 'E'
        }
        self.rotor2_mapping = {
            'T': 'P', 'R': 'A', 'V': 'L', 'D': 'N', 'B': 'G', 'J': 'X', 'N': 'D', 
            'F': 'O', 'K': 'Q', 'O': 'F', 'Z': 'S', 'Y': 'C', 'L': 'V', 'I': 'W', 
            'W': 'I', 'C': 'Y', 'M': 'U', 'G': 'B', 'H': 'E', 'Q': 'K', 'U': 'M', 
            'E': 'H', 'A': 'R', 'P': 'T', 'X': 'J', 'S': 'Z'
        }
        self.rotor3_mapping = {
            'V': 'X', 'S': 'N', 'T': 'E', 'O': 'F', 'X': 'V', 'F': 'O', 'J': 'D', 
            'A': 'G', 'C': 'R', 'I': 'M', 'M': 'I', 'H': 'P', 'K': 'W', 'U': 'Y', 
            'Q': 'L', 'Y': 'U', 'R': 'C', 'W': 'K', 'D': 'J', 'G': 'A', 'Z': 'B', 
            'L': 'Q', 'N': 'S', 'P': 'H', 'E': 'T', 'B': 'Z'
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

        if self.rotor_counter > 26:
            if self.rotor_counter > 52:
                self.rotor3_mapping = self.__reverse_rotate_rotor(self.rotor3_mapping)
                mapped_char2 = self.__find_key_by_value(self.rotor3_mapping, mapped_char3)

                self.rotor2_mapping = self.__reverse_rotate_rotor(self.rotor2_mapping)
                self.rotor2_mapping = self.__reverse_rotate_rotor(self.rotor2_mapping)
                mapped_char1 = self.__find_key_by_value(self.rotor2_mapping, mapped_char2)

                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                mapped_char = self.__find_key_by_value(self.rotor1_mapping, mapped_char1)

                self.decrypt_counter -= 1    
            else:
                mapped_char2 = self.__find_key_by_value(self.rotor3_mapping, mapped_char3)

                self.rotor2_mapping = self.__reverse_rotate_rotor(self.rotor2_mapping)
                mapped_char1 = self.__find_key_by_value(self.rotor2_mapping, mapped_char2)

                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
                mapped_char = self.__find_key_by_value(self.rotor1_mapping, mapped_char1)
                
                self.decrypt_counter -= 1
        else:
            mapped_char2 = self.__find_key_by_value(self.rotor3_mapping, mapped_char3)
            mapped_char1 = self.__find_key_by_value(self.rotor2_mapping, mapped_char2)
            self.rotor1_mapping = self.__reverse_rotate_rotor(self.rotor1_mapping)
            mapped_char = self.__find_key_by_value(self.rotor1_mapping, mapped_char1)
            self.decrypt_counter -= 1

        return mapped_char

    def __find_key_by_value(self, dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None
