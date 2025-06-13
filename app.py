from flask import Flask, render_template, request, jsonify
from caesar_cipher import CaesarCipher
import json

app = Flask(__name__)
cipher = CaesarCipher()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    """Process encryption/decryption request"""
    try:
        data = request.get_json()
        
        text = data.get('text', '')
        shift = int(data.get('shift', 1))
        operation = data.get('operation', 'encrypt')
        
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        if operation == 'encrypt':
            result = cipher.encrypt(text, shift)
        elif operation == 'decrypt':
            result = cipher.decrypt(text, shift)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({
            'success': True,
            'result': result,
            'original': text,
            'shift': shift,
            'operation': operation
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

@app.route('/brute_force', methods=['POST'])
def brute_force():
    """Brute force analysis - try all possible shifts for encrypt or decrypt"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        mode = data.get('mode', 'decrypt')  # Default to decrypt for backward compatibility

        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400

        if mode == 'encrypt':
            # For encrypt mode, show all possible encryptions
            results = cipher.brute_force_encrypt(text)
        else:
            # For decrypt mode, show all possible decryptions
            results = cipher.brute_force_decrypt(text)

        return jsonify({
            'success': True,
            'results': results,
            'mode': mode
        })

    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    print("🔐 Caesar Cipher Web App Starting...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🚀 Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
