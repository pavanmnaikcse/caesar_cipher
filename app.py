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
    if request.method == 'POST':
        text = request.form.get('text', '').lower()
        shift = int(request.form.get('shift', 0))
        direction = request.form.get('direction', 'encode')
        
        if direction == 'encode':
            result = encrypt(text, shift)
        elif direction == 'decode':
            result = decrypt(text, shift)
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
