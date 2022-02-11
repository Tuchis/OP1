""" Program, that can encode and decode messages, using Caesar's
code
"""

def caesar_encode(message, key):
    """Encoding function

    Args:
        message (str): The message, that has to be encoded
        key (int): Key, that uses in encoding

    Returns:
        str: encoded message
    >>> caesar_encode("computer", 3)
    'frpsxwhu'
    """
    encoded_message = ""
    for letter in message:
        character = ord(letter)
        key = key % 26
        if 65 <= character <= 90:
            character += key
            if character < 65:
                character += 26
            elif character > 90:
                character -= 26
        elif 97 <= character <= 122:
            character += key
            if character < 97:
                character += 26
            elif character > 122:
                character -= 26
        letter = chr(character)
        encoded_message += letter
    return encoded_message

def caesar_decode(message, key):
    """Decoding function

    Args:
        message (str): The message, that has to be decoded
        key (int): Key, that uses in decoding

    Returns:
        str: decoded message
    >>> caesar_decode("frpsxwhu", 3)
    'computer'
    """
    decoded_message = ""
    for letter in message:
        character = ord(letter)
        key = key % 26
        if 65 <= character <= 90:
            character -= key
            if character < 65:
                character += 26
            elif character > 90:
                character -= 26
        elif 97 <= character <= 122:
            character -= key
            if character < 97:
                character += 26
            elif character > 122:
                character -= 26
        letter = chr(character)
        decoded_message += letter
    return decoded_message
