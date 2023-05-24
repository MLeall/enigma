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
        return encrypted_message

    def decrypt(self, message):
        """
        Since the Enigma machine uses a symmetric encryption algorithm, the encryption and decryption processes are essentially the same.
        Return a decrypted version of the message provided by the user.
        """
        return self.encrypt(message)