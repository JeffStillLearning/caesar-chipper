#!/usr/bin/env python3
"""
Test brute force untuk encrypt dan decrypt modes
"""

from caesar_cipher import CaesarCipher

def test_brute_force_modes():
    cipher = CaesarCipher()
    
    print('🔍 TESTING BRUTE FORCE MODES')
    print('=' * 50)
    
    original = 'Hello'
    
    print('1. ENCRYPT MODE - Brute Force Encrypt:')
    print(f'   Input: "{original}"')
    print('   Shows all possible encryptions:')
    
    encrypt_results = cipher.brute_force_encrypt(original)
    for shift, encrypted in encrypt_results[:5]:
        print(f'   Shift {shift:2d}: {encrypted}')
    print('   ...')
    
    # Show shift 3 specifically
    for shift, encrypted in encrypt_results:
        if shift == 3:
            print(f'   Shift {shift:2d}: {encrypted} ← Example')
            test_encrypted = encrypted
            break
    
    print()
    print('2. DECRYPT MODE - Brute Force Decrypt:')
    print(f'   Input: "{test_encrypted}" (encrypted with shift 3)')
    print('   Shows all possible decryptions:')
    
    decrypt_results = cipher.brute_force_decrypt(test_encrypted)
    for shift, decrypted in decrypt_results[:5]:
        marker = ' ← ORIGINAL' if decrypted == original else ''
        print(f'   Key {shift:2d}: {decrypted}{marker}')
    print('   ...')
    
    print()
    print('3. CONSISTENCY CHECK:')
    
    # Find which key gives back original
    correct_key = None
    for shift, decrypted in decrypt_results:
        if decrypted == original:
            correct_key = shift
            break
    
    if correct_key == 3:
        print('   ✅ CORRECT: Encrypt shift 3 → Decrypt key 3 gives original')
    else:
        print(f'   ❌ ERROR: Expected key 3, got key {correct_key}')
    
    print()
    print('4. EXPECTED BEHAVIOR:')
    print('   ENCRYPT MODE:')
    print('   - Input: "Hello"')
    print('   - Brute force shows: "Shift 1: Ifmmp", "Shift 2: Jgnnq", "Shift 3: Khoor", etc.')
    print('   - User can see all possible encryptions')
    print()
    print('   DECRYPT MODE:')
    print('   - Input: "Khoor" (encrypted text)')
    print('   - Brute force shows: "Key 1: Jgnnq", "Key 2: Ifmmp", "Key 3: Hello", etc.')
    print('   - Key 3 gives back original "Hello"')

if __name__ == "__main__":
    test_brute_force_modes()
