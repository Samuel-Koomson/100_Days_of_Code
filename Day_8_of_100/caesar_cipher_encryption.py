"""
Pseudocode
1. a variable containing, all the letters of the alphabets is created
2. a variable that gives us direction whether we are encoding or decoding is created and this takes inputs
3. two input variables text and shift are created to serve as parameter arguments.
4. the encryption function is defined with two parameters
5. an empty string is created that will hold the encripted text
6. we then loop through the inputed string to find out the index of each character from the alphabet variable
7. we then add the index of the character to the number of spaces we want to shift our character forward and assign it to a variable.
8. the new character becomes the alphabet at the index of the new position after the shift
9. we then do string concatenation to add our characters to form the string we want
10. we call the encrypt function and pass the input arguments to it.
11. we may have issues when we need to call numbers that are closer to the end of the list, so to avoid that we duplicate the list. this works because the index function only looks up the first occurrence of a character at a time.
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, shift_space):
  encrypted_code = ""
  for char in message:
    char_position = alphabet.index(char)
    new_char_position = char_position + shift_space
    new_char = alphabet[new_char_position]
    encrypted_code += new_char
  print(f"The encrypted text is {encrypted_code}")
encrypt(text, shift)
    
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
