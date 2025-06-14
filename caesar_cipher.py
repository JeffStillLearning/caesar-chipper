class CaesarCipher:
    """
    Caesar Cipher implementation for encryption and decryption
    """
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def encrypt(self, text, shift):
        """
        Encrypt text using Caesar Cipher
        
        Args:
            text (str): Text to encrypt
            shift (int): Number of positions to shift (1-25)
            
        Returns:
            str: Encrypted text
        """
        if not isinstance(shift, int) or shift < 1 or shift > 25:
            raise ValueError("Shift must be an integer between 1 and 25")
        
        result = ""
        
        for char in text:
            if char.upper() in self.alphabet:
                # Get position in alphabet
                old_pos = self.alphabet.index(char.upper())
                # Calculate new position with wrap-around
                new_pos = (old_pos + shift) % 26
                # Get new character
                new_char = self.alphabet[new_pos]
                
                # Preserve original case
                if char.islower():
                    result += new_char.lower()
                else:
                    result += new_char
            else:
                # Keep non-alphabetic characters unchanged
                result += char
                
        return result
    
    def decrypt(self, text, shift):
        """
        Decrypt text using Caesar Cipher
        
        Args:
            text (str): Text to decrypt
            shift (int): Number of positions to shift back (1-25)
            
        Returns:
            str: Decrypted text
        """
        if not isinstance(shift, int) or shift < 1 or shift > 25:
            raise ValueError("Shift must be an integer between 1 and 25")
        
        result = ""
        
        for char in text:
            if char.upper() in self.alphabet:
                # Get position in alphabet
                old_pos = self.alphabet.index(char.upper())
                # Calculate new position with wrap-around (subtract for decryption)
                new_pos = (old_pos - shift) % 26
                # Get new character
                new_char = self.alphabet[new_pos]
                
                # Preserve original case
                if char.islower():
                    result += new_char.lower()
                else:
                    result += new_char
            else:
                # Keep non-alphabetic characters unchanged
                result += char
                
        return result
    
    def brute_force_decrypt(self, text):
        """
        Try all possible shifts to decrypt text

        Args:
            text (str): Text to decrypt

        Returns:
            list: List of tuples (shift, decrypted_text)
            where shift represents the decrypt key used
        """
        results = []

        # Try all possible decrypt keys from 1 to 25
        for shift in range(1, 26):
            decrypted = self.decrypt(text, shift)
            results.append((shift, decrypted))

        return results

    def brute_force_encrypt(self, text):
        """
        Try all possible shifts to encrypt text

        Args:
            text (str): Text to encrypt

        Returns:
            list: List of tuples (shift, encrypted_text)
            where shift represents the encrypt shift used
        """
        results = []

        # Try all possible encrypt shifts from 1 to 25
        for shift in range(1, 26):
            encrypted = self.encrypt(text, shift)
            results.append((shift, encrypted))

        return results
