class Enigma:
    """
    Enigma class should have the rotors logic, encryption and decryption logic and a management method to ensure consistency.
    """
    def __init__(self) -> None:
        pass

    def encrypt(self, message):
        """
        This method is responsible for iterate the message provide by user and use (still_to_be_coded_method) to process each char of the message.
        Return a encrypted version of the message provided by the user.
        """
        encrypted_message = ''
        for i in encrypted_message:
            if i.isalpha():
                encrypted_char = '' # method responsible for process and encrypt the char. Still need to be coded.

                encrypted_message += encrypted_char
            # else block or possible try/except block
        return encrypted_message

    def decrypt(self, message):
        """
        Since the Enigma machine uses a symmetric encryption algorithm, the encryption and decryption processes are essentially the same.
        Return a decrypted version of the message provided by the user.
        """
        return self.encrypt(message)
    
    def reflector_output(self, char):
        """
        The reflector_output method simulate an reflector mapping to ensures that the encryption process is reversible.
        It creates a reciprocal mapping, meaning each input contact is paired with a corresponding output contact, and vice versa.
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