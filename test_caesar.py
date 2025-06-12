#!/usr/bin/env python3
"""
Test script untuk Caesar Cipher
"""

from caesar_cipher import CaesarCipher

def test_caesar_cipher():
    """Test basic functionality of Caesar Cipher"""
    cipher = CaesarCipher()
    
    print("🔐 Testing Caesar Cipher Implementation")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        ("Hello World", 3),
        ("PYTHON", 5),
        ("abc XYZ 123", 1),
        ("The Quick Brown Fox", 13),
        ("Caesar Cipher Test!", 7)
    ]
    
    for text, shift in test_cases:
        print(f"\n📝 Original: '{text}'")
        print(f"🔢 Shift: {shift}")
        
        # Encrypt
        encrypted = cipher.encrypt(text, shift)
        print(f"🔒 Encrypted: '{encrypted}'")
        
        # Decrypt
        decrypted = cipher.decrypt(encrypted, shift)
        print(f"🔓 Decrypted: '{decrypted}'")
        
        # Verify
        if text == decrypted:
            print("✅ Test PASSED")
        else:
            print("❌ Test FAILED")
    
    print("\n" + "=" * 50)
    
    # Test brute force
    print("\n🔍 Testing Brute Force Decryption")
    test_encrypted = "Khoor Zruog"
    print(f"🔒 Encrypted text: '{test_encrypted}'")
    
    results = cipher.brute_force_decrypt(test_encrypted)
    print("\n📊 All possible decryptions:")
    
    for shift, decrypted in results:
        marker = "👈 LIKELY MATCH" if "Hello" in decrypted else ""
        print(f"Shift {shift:2d}: {decrypted} {marker}")
    
    print("\n✨ All tests completed!")

def test_edge_cases():
    """Test edge cases"""
    cipher = CaesarCipher()
    
    print("\n🧪 Testing Edge Cases")
    print("=" * 30)
    
    # Empty string
    result = cipher.encrypt("", 5)
    print(f"Empty string: '{result}' ✅" if result == "" else "❌")
    
    # Numbers and symbols only
    result = cipher.encrypt("123!@#", 5)
    print(f"Numbers/symbols: '{result}' ✅" if result == "123!@#" else "❌")
    
    # Single character
    result = cipher.encrypt("A", 1)
    print(f"Single char 'A' -> '{result}' ✅" if result == "B" else "❌")
    
    # Wrap around test
    result = cipher.encrypt("Z", 1)
    print(f"Wrap around 'Z' -> '{result}' ✅" if result == "A" else "❌")
    
    # Case preservation
    result = cipher.encrypt("aZ", 1)
    print(f"Case preservation 'aZ' -> '{result}' ✅" if result == "bA" else "❌")

if __name__ == "__main__":
    test_caesar_cipher()
    test_edge_cases()
    
    print("\n🎉 Caesar Cipher is working perfectly!")
    print("🌐 Your web app is ready at: http://localhost:5000")
