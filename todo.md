# Enigma Project Guideline

## Planning

1. *Understand the Enigma machine:* Familiarize yourself with the workings of the original Enigma machine. Learn about its components, such as the rotors, reflector, plugboard, and how they interact to encrypt and decrypt messages.

2. *Design your Enigma machine class:* Create a class that represents the Enigma machine. This class will encapsulate the behavior of the machine, including rotor configurations, current rotor positions, and encryption/decryption logic.

3. *Implement the rotor mechanism:* Each rotor in the Enigma machine rotates with every key press. Implement a class to represent a rotor, including its wiring configuration, position, and the logic for rotating it.

4. *Create the plugboard:* The plugboard allows swapping of letters before and after the rotor mechanism. Implement a class to represent the plugboard, which will handle letter substitutions.

5. *Build the encryption and decryption logic:* Implement methods in the Enigma machine class to perform encryption and decryption. These methods should handle the flow of data through the rotor mechanism, reflector, and plugboard.

6. *Handle input and output:* Decide how you want to receive input and display output. You can choose to read input from the command line or a file, and display the output similarly.

7. *Create a user interface (optional):* If you want a graphical interface, consider using a GUI library like Tkinter to create a user-friendly interface for inputting text, configuring rotor settings, and displaying the encrypted/decrypted output.

8. *Test your implementation:* Write test cases to validate the correctness of your implementation. Ensure that the encryption and decryption processes produce the expected results.

9. *Expand and experiment (optional):* Once you have a working Enigma machine emulator, you can further enhance it by adding features like additional rotor types, configurable rotor settings, or even simulating historical Enigma machine variants.

Remember to refer to historical documentation and resources on Enigma machines to ensure the accuracy of your implementation. It's also helpful to break down the problem into smaller tasks and implement them incrementally. This approach allows you to test and debug each component before integrating them into the final implementation.

## Ideas

List of suggestions to be made after the main code is completed. Feel free to write anything.

- Use lib `tkinter` to create a GUI ❌
- Create a web application for our project. We can use Flask/Django for that ❌