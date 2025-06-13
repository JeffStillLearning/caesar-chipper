#!/usr/bin/env python3
"""
Debug Caesar Cipher logic
"""

from caesar_cipher import CaesarCipher

def debug_caesar():
    cipher = CaesarCipher()
    
    print('🔍 DEBUGGING CAESAR CIPHER LOGIC')
    print('=' * 50)
    
    # Test basic encrypt
    print('1. Testing ENCRYPT function:')
    original = 'Hello'
    encrypted = cipher.encrypt(original, 3)
    print(f'   encrypt("Hello", 3) = "{encrypted}"')
    print('   Expected: "Khoor" (H→K, e→h, l→o, l→o, o→r)')
    print(f'   Correct: {"✅" if encrypted == "Khoor" else "❌"}')
    print()
    
    # Test basic decrypt
    print('2. Testing DECRYPT function:')
    test_encrypted = "Khoor"
    decrypted = cipher.decrypt(test_encrypted, 3)
    print(f'   decrypt("Khoor", 3) = "{decrypted}"')
    print('   Expected: "Hello"')
    print(f'   Correct: {"✅" if decrypted == "Hello" else "❌"}')
    print()
    
    # Test consistency
    print('3. Testing CONSISTENCY (encrypt then decrypt):')
    original2 = 'ABC'
    encrypted2 = cipher.encrypt(original2, 3)
    decrypted2 = cipher.decrypt(encrypted2, 3)
    print(f'   Original: "{original2}"')
    print(f'   Encrypted: "{encrypted2}"')
    print(f'   Decrypted back: "{decrypted2}"')
    print(f'   Round-trip correct: {"✅" if original2 == decrypted2 else "❌"}')
    print()
    
    # Test brute force
    print('4. Testing BRUTE FORCE:')
    print(f'   Input for brute force: "{encrypted}"')
    results = cipher.brute_force_decrypt(encrypted)
    
    print('   Results:')
    for shift, result in results[:5]:
        marker = ' ← ORIGINAL' if result == original else ''
        print(f'   Key {shift:2d}: "{result}"{marker}')
    
    print('   ...')
    
    # Check if any key gives original
    correct_key = None
    for shift, result in results:
        if result == original:
            correct_key = shift
            break
    
    if correct_key:
        print(f'   ✅ Key {correct_key} gives original "{original}"')
    else:
        print('   ❌ No key gives original result!')
    
    print()
    print('5. ANALYSIS:')
    if encrypted == "Khoor" and decrypted == "Hello" and correct_key == 3:
        print('   ✅ All logic is CORRECT')
        print('   ✅ encrypt(Hello, 3) → Khoor')
        print('   ✅ decrypt(Khoor, 3) → Hello') 
        print('   ✅ brute_force(Khoor) → Key 3: Hello')
    else:
        print('   ❌ There is an issue with the logic')
        print(f'   - Encrypt result: {encrypted} (expected: Khoor)')
        print(f'   - Decrypt result: {decrypted} (expected: Hello)')
        print(f'   - Brute force key: {correct_key} (expected: 3)')

if __name__ == "__main__":
    debug_caesar()
