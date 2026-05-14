from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text1,shift1):
    encrypted=""
    for i in text1:
        if i not in alphabet:
            encrypted+=i
        else:
            index=alphabet.index(i)
            new_index=index+shift1
            if new_index>25:
                new_index=new_index-25
                encrypted=encrypted+alphabet[new_index-1]
            elif new_index<=25:
                encrypted = encrypted + alphabet[new_index]
    return encrypted

# Global chat history stored in memory
chat_history = []

@app.route('/')
def index():
    return render_template('messenger.html')

@app.route('/messages')
def get_messages():
    return jsonify(chat_history)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    text = data.get('text', '').lower()
    shift = int(data.get('shift', 0)) % 26
    sender_id = data.get('sender_id', 'unknown')
    
    ciphertext = encrypt(text, shift)
    
    message = {
        "id": str(uuid.uuid4()),
        "sender_id": sender_id,
        "plaintext": text,
        "ciphertext": ciphertext,
        "shift": shift
    }
    
    chat_history.append(message)
    
    # Keep memory clean
    if len(chat_history) > 100:
        chat_history.pop(0)
        
    return jsonify({"status": "success", "message": message})

if __name__ == '__main__':
    # host='0.0.0.0' enables local WiFi connections (anyone on the same network can access it via your IP address)
    app.run(host='0.0.0.0', port=5000, debug=True)
