from flask import Flask, render_template, request

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

def decrypt(text2,shift2):
    decrypted=""
    for i in text2:
        if i not in alphabet:
            decrypted += i
        else:
            index=alphabet.index(i)
            new_index=index-shift2
            if new_index<0:
                new_index=new_index+25
                decrypted=decrypted+alphabet[new_index+1]
            elif new_index<=25:
                decrypted = decrypted + alphabet[new_index]
    return decrypted

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    original_text = ""
    theme = request.args.get('theme', 'professional')
    direction_val = 'encode'
    shift_val = 0
    
    if request.method == 'POST':
        original_text = request.form.get('text', '')
        shift_val = int(request.form.get('shift', 0))
        direction_val = request.form.get('direction', 'encode')
        theme = request.form.get('theme', 'professional')
        
        shift = shift_val % 26
        
        if direction_val == 'encode':
            result = encrypt(original_text.lower(), shift)
        elif direction_val == 'decode':
            result = decrypt(original_text.lower(), shift)
            
    if theme == 'whatsapp':
        template = 'whatsapp.html'
    elif theme == 'hacker':
        template = 'index.html'
    else:
        template = 'professional.html'
        
    return render_template(template, result=result, original_text=original_text, theme=theme, direction=direction_val, shift=shift_val)

if __name__ == '__main__':
    app.run(debug=True)
