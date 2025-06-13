// DOM Elements
const encryptBtn = document.getElementById('encryptBtn');
const decryptBtn = document.getElementById('decryptBtn');
const inputText = document.getElementById('inputText');
const outputText = document.getElementById('outputText');
const shiftSlider = document.getElementById('shiftSlider');
const shiftValue = document.getElementById('shiftValue');
const processBtn = document.getElementById('processBtn');
const bruteForceBtn = document.getElementById('bruteForceBtn');
const clearBtn = document.getElementById('clearBtn');
const copyBtn = document.getElementById('copyBtn');
const btnText = document.getElementById('btnText');
const bruteForceResults = document.getElementById('bruteForceResults');
const bruteForceList = document.getElementById('bruteForceList');
const loadingOverlay = document.getElementById('loadingOverlay');
const toast = document.getElementById('toast');

// State
let currentMode = 'encrypt';

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    updateShiftValue();
    setupEventListeners();
    
    // Auto-focus on input
    inputText.focus();
    
    // Show welcome message
    showToast('Welcome to Caesar Cipher! 🔐', 'success');
});

// Event Listeners
function setupEventListeners() {
    // Mode toggle
    encryptBtn.addEventListener('click', () => setMode('encrypt'));
    decryptBtn.addEventListener('click', () => setMode('decrypt'));
    
    // Shift slider
    shiftSlider.addEventListener('input', updateShiftValue);
    
    // Buttons
    processBtn.addEventListener('click', processText);
    bruteForceBtn.addEventListener('click', bruteForceDecrypt);
    clearBtn.addEventListener('click', clearAll);
    copyBtn.addEventListener('click', copyToClipboard);
    
    // Real-time processing disabled - only process on button click
    // inputText.addEventListener('input', debounce(autoProcess, 500));
    
    // Enter key processing
    inputText.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            processText();
        }
    });
}

// Mode Management
function setMode(mode) {
    currentMode = mode;
    
    // Update button states
    encryptBtn.classList.toggle('active', mode === 'encrypt');
    decryptBtn.classList.toggle('active', mode === 'decrypt');
    
    // Update process button text
    btnText.textContent = mode === 'encrypt' ? 'Encrypt' : 'Decrypt';
    
    // Update process button icon
    const icon = processBtn.querySelector('i');
    icon.className = mode === 'encrypt' ? 'fas fa-lock' : 'fas fa-unlock';
    
    // Hide brute force results when switching modes
    bruteForceResults.style.display = 'none';

    // Clear both input and output when switching modes
    inputText.value = '';
    outputText.value = '';
    showToast(`Switched to ${mode} mode. Enter new text to process.`, 'info');
}

// Shift Value Update
function updateShiftValue() {
    shiftValue.textContent = shiftSlider.value;

    // Clear output when shift changes - user needs to click process again
    if (outputText.value.trim()) {
        outputText.value = '';
        showToast('Shift value changed. Click process to see new result.', 'info');
    }
}

// Main Processing Function
async function processText() {
    const text = inputText.value.trim();
    
    if (!text) {
        showToast('Please enter some text to process', 'error');
        inputText.focus();
        return;
    }
    
    const shift = parseInt(shiftSlider.value);
    
    showLoading(true);
    
    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                shift: shift,
                operation: currentMode
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            outputText.value = data.result;
            showToast(`Text ${currentMode}ed successfully! 🎉`, 'success');
            
            // Hide brute force results
            bruteForceResults.style.display = 'none';
        } else {
            showToast(data.error || 'An error occurred', 'error');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showToast('Network error. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Auto Process (for real-time updates)
async function autoProcess() {
    const text = inputText.value.trim();
    
    if (!text) {
        outputText.value = '';
        return;
    }
    
    const shift = parseInt(shiftSlider.value);
    
    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                shift: shift,
                operation: currentMode
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            outputText.value = data.result;
        }
        
    } catch (error) {
        // Silently fail for auto-processing
        console.error('Auto-process error:', error);
    }
}

// Brute Force Decryption
async function bruteForceDecrypt() {
    const text = inputText.value.trim();
    
    if (!text) {
        showToast('Please enter some text for brute force decryption', 'error');
        inputText.focus();
        return;
    }
    
    showLoading(true);
    
    try {
        const response = await fetch('/brute_force', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayBruteForceResults(data.results);
            showToast('Brute force analysis complete! 🔍', 'success');
        } else {
            showToast(data.error || 'An error occurred', 'error');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showToast('Network error. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Display Brute Force Results
function displayBruteForceResults(results) {
    bruteForceList.innerHTML = '';
    
    results.forEach(([shift, decrypted]) => {
        const item = document.createElement('div');
        item.className = 'brute-force-item';
        item.innerHTML = `
            <div class="shift-badge">Key ${shift}</div>
            <div class="decrypted-text" style="flex: 1; font-family: monospace;">${decrypted}</div>
            <div class="hint-text" style="font-size: 0.8em; color: #666; margin-left: 10px;">
                (decrypt key: ${shift})
            </div>
        `;
        
        // Click to use this result
        item.addEventListener('click', () => {
            outputText.value = decrypted;
            shiftSlider.value = shift;
            updateShiftValue();
            showToast(`Applied decrypt key ${shift} - Result copied to output`, 'success');
        });
        
        bruteForceList.appendChild(item);
    });
    
    bruteForceResults.style.display = 'block';
    bruteForceResults.scrollIntoView({ behavior: 'smooth' });
}

// Clear All
function clearAll() {
    inputText.value = '';
    outputText.value = '';
    bruteForceResults.style.display = 'none';
    inputText.focus();
    showToast('Cleared all text', 'success');
}

// Copy to Clipboard
async function copyToClipboard() {
    const text = outputText.value;
    
    if (!text) {
        showToast('No text to copy', 'error');
        return;
    }
    
    try {
        await navigator.clipboard.writeText(text);
        showToast('Copied to clipboard! 📋', 'success');
        
        // Visual feedback
        copyBtn.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(() => {
            copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
        }, 1000);
        
    } catch (error) {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        
        showToast('Copied to clipboard! 📋', 'success');
    }
}

// Loading Overlay
function showLoading(show) {
    loadingOverlay.classList.toggle('show', show);
}

// Toast Notifications
function showToast(message, type = 'success') {
    toast.textContent = message;
    toast.className = `toast ${type}`;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Keyboard Shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl+E for encrypt mode
    if (e.ctrlKey && e.key === 'e') {
        e.preventDefault();
        setMode('encrypt');
    }
    
    // Ctrl+D for decrypt mode
    if (e.ctrlKey && e.key === 'd') {
        e.preventDefault();
        setMode('decrypt');
    }
    
    // Ctrl+B for brute force
    if (e.ctrlKey && e.key === 'b') {
        e.preventDefault();
        bruteForceDecrypt();
    }
    
    // Ctrl+L for clear
    if (e.ctrlKey && e.key === 'l') {
        e.preventDefault();
        clearAll();
    }
});

// Add some fun easter eggs
let konamiCode = [];
const konamiSequence = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'KeyB', 'KeyA'
];

document.addEventListener('keydown', function(e) {
    konamiCode.push(e.code);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }
    
    if (konamiCode.join(',') === konamiSequence.join(',')) {
        showToast('🎉 Konami Code activated! You are a true cryptographer! 🔐', 'success');
        document.body.style.animation = 'rainbow 2s infinite';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 5000);
        konamiCode = [];
    }
});

// Add rainbow animation for easter egg
const style = document.createElement('style');
style.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;
document.head.appendChild(style);
